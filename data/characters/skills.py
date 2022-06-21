
from utils import loadJson
from constants import CHAR_SKILL_DEPOT_JSON, CHAR_SKILLS_JSON, CHAR_TALENTS_JSON, CHAR_PROUD_SKILL_JSON
from common.dataobj.character import Character
from common.ascensions import formatCosts
from translate.textmap import lang

import re
import logging

params_reg = re.compile(r'\{param(\d+):([A-Z0-9]+)\}')

logger = logging.getLogger(__name__)

skill_depot = loadJson(CHAR_SKILL_DEPOT_JSON)
skills = loadJson(CHAR_SKILLS_JSON)
talents = loadJson(CHAR_TALENTS_JSON)
proud_skills = loadJson(CHAR_PROUD_SKILL_JSON)


def readSkillsConstellations(char: Character) :
    depot_search = [x for x in skill_depot if x['id'] == char.skill_depot_id]
    if len(depot_search) != 1 :
        logger.error('No skills found for %s (%d)', char.name, char.hoyo_id)
        return
    depot = depot_search[0]
    skills = {
        'normal_attack': __g_readSkill(depot['skills'][0]),
        'elemental_skill': __g_readSkill(depot['skills'][1]),
        'elemental_burst': __g_readSkill(depot['energySkill']),
        'alternate_sprint': None
    }
    if depot['skills'][2] != 0 :
        skills['alternate_sprint'] = __g_readSkill(depot['skills'][2])
    if depot['skills'][3] != 0 :
        logger.info('Fourth skill slot (id: %d) used by character %s (%d)', depot['skills'][3], char['name'], char['hoyo_id'])
    char.talents = skills
    passives = [
        __g_readSimpleSkill(talent['proudSkillGroupId'], talent['needAvatarPromoteLevel'] if 'needAvatarPromoteLevel' in talent else None)
        for talent in depot['inherentProudSkillOpens']
        if 'proudSkillGroupId' in talent
    ]
    char.passives = passives
    char.constellations = __g_readConstellations(depot['talents'])


def __g_readConstellations(const_ids: "list[int]") -> list :
    res = []
    constellations = {c['talentId']: c for c in talents if c['talentId'] in const_ids}
    if len(constellations) != 6 :
        logger.warning('Expected 6 constellations, found %d', len(constellations))
    for const_id in const_ids :
        const = constellations[const_id]
        res.append({
            'name_hash': const['nameTextMapHash'],
            'name': lang[str(const['nameTextMapHash'])],
            'desc_hash': const['descTextMapHash'],
            'desc': lang[str(const['descTextMapHash'])]
        })
    return res


def __g_readSkill(skill_id: int) -> dict :
    skill_search = [x for x in skills if x['id'] == skill_id]
    if len(skill_search) != 1 :
        logger.error('No skill found with id %d', skill_id)
        return None
    skill = skill_search[0]
    # triggerID ?
    res = {
        'name_hash': skill['nameTextMapHash'],
        'desc_hash': skill['descTextMapHash'],
        'charge_num': skill['maxChargeNum']
        # 'cost': skill['costElemVal']
        # 'cooldown': skill['cdTime']
    }
    res['name'] = lang[str(res['name_hash'])]
    res['desc'] = lang[str(res['desc_hash'])]
    res['costs'], res['stats'] = __g_readProudSkillGroup(skill['proudSkillGroupId'])
    return res


def __g_readSimpleSkill(psg_id: int, ascension: int = None) :
    skill_search = [psk for psk in proud_skills if psk['proudSkillGroupId'] == psg_id]
    if len(skill_search) != 1 :
        logger.error('No skill found with group id %d', psg_id)
        return None
    skill = skill_search[0]
    res = {
        'name_hash': skill['nameTextMapHash'],
        'desc_hash': skill['descTextMapHash'],
        'ascension': ascension
    }
    res['name'] = lang[str(res['name_hash'])]
    res['desc'] = lang[str(res['desc_hash'])]
    return res
    

def __g_readProudSkillGroup(psg_id: int) -> "tuple[list,dict]" :
    group = [psk for psk in proud_skills if psk['proudSkillGroupId'] == psg_id]
    group.sort(key = lambda psk: psk['level'])
    if len(group) != 15 :
        logger.warning('Expected 15 proud skills in group %d, found %d', psg_id, len(group))
    costs = []
    stats = {
        'names': None,
        'values': []
    }
    for psk in group :
        cost, mora_cost, stat = __g_readProudSkill(psk)
        costs.append(formatCosts(cost, mora_cost))
        if stats['names'] is None :
            stats['names'] = list(stat.keys())
        stats['values'].append(list(stat.values()))
    return costs[1:10], stats
        

# nameTextMapHash ?
# descTextMapHash ?
# unlockDescTextMapHash ?
# breakLevel must be the level required to unlock, not very useful here
# proudSkillType => 3 for burst, ...
def __g_readProudSkill(psk: dict) -> "tuple[dict,int,dict]" :
    cost = {
        c['id']: c['count']
        for c in psk['costItems']
        if 'id' in c and 'count' in c
    }
    mora_cost = psk['coinCost'] if 'coinCost' in psk else 0
    stats = __g_readStats(psk['paramDescList'], psk['paramList'])
    return cost, mora_cost, stats

def __g_readStats(desc: "list[int]", values: "list[float]") -> dict :
    res = {}
    for d in desc :
        dsc = lang[str(d)]
        if len(dsc) > 0 :
            __g_readParam(dsc, values, res)
    return res

def __g_readParam(desc: str, values: "list[float]", params: dict) :
    desc_split = desc.split('|')
    if len(desc_split) != 2 :
        logger.warning('Bad param description format : %s', desc)
        return
    name = desc_split[0]
    desc_repl = desc_split[1]
    for i, fmt in params_reg.findall(desc_repl) :
        val = __g_formatValue(values[int(i)-1], fmt)
        desc_repl = params_reg.sub(val, desc_repl, 1)
    params[name] = desc_repl

def __g_formatValue(val: float, type: str) -> str :
    if type == 'I' :
        return str(int(val))
    if type.endswith('P') :
        val = val * 100
    res = str(round(val, 2))
    while res.endswith('0') :
        res = res[:-1]
    if res.endswith('.') :
        res = res[:-1]
    if type.endswith('P') :
        res = f"{res}%"
    return res