
from utils import loadJson, indexById, groupByField
from constants import CHAR_SKILL_DEPOT_JSON, CHAR_SKILLS_JSON, CHAR_TALENTS_JSON, CHAR_PROUD_SKILL_JSON
from characters.dataobj import CharConstellation, CharPassive, CharTalentStats, CharTalent, Character
from common.ascensions import formatCosts
from translate.textmap import lang
from common.text import clearFormat

import re
import logging

params_reg = re.compile(r'\{param(\d+):([A-Z0-9]+)\}')

logger = logging.getLogger(__name__)

skill_depot = indexById(loadJson(CHAR_SKILL_DEPOT_JSON))
skills = indexById(loadJson(CHAR_SKILLS_JSON))
talents = loadJson(CHAR_TALENTS_JSON)
proud_skills = groupByField(loadJson(CHAR_PROUD_SKILL_JSON), 'proudSkillGroupId')


def readSkillsConstellations(char: Character) :
    logger.debug("Reading skills and constellations for %s (%s)", char.hoyo_id, char.name)
    # Search for the entry corresponding to the character in the skill depot
    depot = skill_depot[char.skill_depot_id]
    # Talents 
    char.talents.normal_attack   = readSkill(depot['skills'][0])
    char.talents.elemental_skill = readSkill(depot['skills'][1])
    char.talents.elemental_burst = readSkill(depot['energySkill'])
    if depot['skills'][2] != 0 :
        char.talents.alternate_sprint = readSkill(depot['skills'][2], True)
    if depot['skills'][3] != 0 :
        logger.info('Fourth skill slot (id: %d) used by character %s (%d)', depot['skills'][3], char.name, char.hoyo_id)
    # Passives
    char.passives = [
        __g_readSimpleSkill(talent['proudSkillGroupId'], talent['needAvatarPromoteLevel'] if 'needAvatarPromoteLevel' in talent else None)
        for talent in depot['inherentProudSkillOpens']
        if 'proudSkillGroupId' in talent
    ]
    char.passives = [x for x in char.passives if x is not None]
    # Constellations
    char.constellations = __g_readConstellations(depot['talents'])
    __g_readTalentBonuses(char)


# Read the constellations of a character from the object that stores all the constellations
def __g_readConstellations(const_ids: "list[int]") -> "list[CharConstellation]" :
    res = []
    constellations = {c['talentId']: c for c in talents if c['talentId'] in const_ids}
    if len(constellations) != 6 :
        logger.warning('Expected 6 constellations, found %d', len(constellations))
    for cst_id in const_ids :
        cst = constellations[cst_id]
        cst_res = CharConstellation()
        # talent_id = cst_id
        cst_res.name_hash = cst['nameTextMapHash']
        cst_res.desc_hash = cst['descTextMapHash']
        cst_res.icon = cst['icon']
        cst_res.name = lang(cst_res.name_hash)
        cst_res.desc = clearFormat(lang(cst_res.desc_hash))
        res.append(cst_res)
    return res


# Read a passive from the object that stores all the skills
# Note : skill is the generic term for passive + talent
def __g_readSimpleSkill(psg_id: int, ascension: int = None) :
    skill_search = proud_skills[psg_id]
    if len(skill_search) > 1 :
        logger.warning('Multiple skills found with group id %d (expected one)', psg_id)
    skill = skill_search[0]
    res = CharPassive()
    res.name_hash = skill['nameTextMapHash']
    res.desc_hash = skill['descTextMapHash']
    res.icon = skill['icon']
    res.ascension = ascension
    if res.name_hash not in lang :
        return None
    res.name = lang(res.name_hash)
    res.desc = clearFormat(lang(res.desc_hash))
    return res


# Read a talent from the object that stores all the skills
def readSkill(skill_id: int, is_sprint = False) -> CharTalent :
    skill = skills[skill_id]
    # triggerID ?
    res = CharTalent()
    res.name_hash = skill['nameTextMapHash']
    res.desc_hash = skill['descTextMapHash']
    res.charge_num = skill['maxChargeNum']
    res.icon = skill['skillIcon']
    # cost = skill['costElemVal']
    # cooldown = skill['cdTime']
    res.name = lang(res.name_hash)
    res.desc = clearFormat(lang(res.desc_hash))
    # A talent is associated with a "proud skill group" that contains one entry
    # per level this talent can have, with the stats of this talent
    expected_num = 1 if is_sprint else 15
    res.costs, res.stats = __g_readProudSkillGroup(skill['proudSkillGroupId'], expected_num)
    return res
    

# Reads the entries of a proud skill group to get the stats + ascension costs of a talent at each level
def __g_readProudSkillGroup(psg_id: int, expected_num: int) -> "tuple[list[dict[str,int]],CharTalentStats]" :
    group = proud_skills[psg_id]
    group.sort(key = lambda psk: psk['level'])
    if len(group) != expected_num :
        logger.warning('Expected %d proud skills in group %d, found %d', expected_num, psg_id, len(group))
    costs = []
    stats = CharTalentStats()
    stats.values = []
    for psk in group :
        cost, mora_cost, stat = __g_readProudSkill(psk)
        costs.append(formatCosts(cost, mora_cost))
        if stats.names is None :
            stats.names = list(stat.keys())
        stats.values.append(list(stat.values()))
    return costs[1:10], stats
        

# Reads an individual entry (i.e. level) in the proud skill group
# This entry will be called a "proud skill"
def __g_readProudSkill(psk: dict) -> "tuple[dict[str,int],int,dict[str,str]]" :
    cost = {
        c['id']: c['count']
        for c in psk['costItems']
        if 'id' in c and 'count' in c
    }
    mora_cost = psk['coinCost'] if 'coinCost' in psk else 0
    stats = __g_readStats(psk['paramDescList'], psk['paramList'])
    return cost, mora_cost, stats
# nameTextMapHash ?
# descTextMapHash ?
# unlockDescTextMapHash ?
# breakLevel must be the level required to unlock, not very useful here
# proudSkillType => 3 for burst, ...


# Reads the stats for a proud skill
def __g_readStats(desc: "list[int]", values: "list[float]") -> "dict[str,str]" :
    res = {}
    for d in desc :
        if d in lang :
            __g_readParam(lang(d), values, res)
    return res


# Reads an individual stat in a proud skill
# A stat has a description with the format {name}|{value}
# The value has a special format that requires to read numbers
# at certain indexes in a list
# These numbers also need to be formatted, which is done in a separate method
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


# Formats a number for the value of a stat entry
# The values have a type described by a string
# The exact specifications of the type are unclear
# but this code should be about right
def __g_formatValue(val: float, type: str) -> str :
    # I is for an integer (no decimals)
    if type == 'I' :
        return str(int(val))
    # a P at the end is for a percentage, so we multiply the value by 100
    if type.endswith('P') :
        val = val * 100
    # at this point, we consider only floating point values w/ 2 digit precision
    res = str(round(val, 2))
    # we remove the useless tailing zeroes
    while res.endswith('0') :
        res = res[:-1]
    if res.endswith('.') :
        res = res[:-1]
    # if we have a percentage, we add the percent sign at the end
    # (else it is most likely a float, so we don't need to do naything else)
    if type.endswith('P') :
        res = f"{res}%"
    return res


# Computes which constellation give talent levels
def __g_readTalentBonuses(char: Character) :
    if char.constellations is None :
        return
    c3 = char.constellations[2].desc
    c5 = char.constellations[4].desc
    skill_increase_text = f"Increases the Level of {char.talents.elemental_skill.name} by 3."
    burst_increase_text = f"Increases the Level of {char.talents.elemental_burst.name} by 3."
    if c3.startswith(skill_increase_text) :
        char.increase_skill = 3
        char.increase_burst = 5
        if not c5.startswith(burst_increase_text) :
            logger.warning("Found skill increase at C3 but no burst increase at C5 for %s (%s)", char.hoyo_id, char.name)
        return
    elif c5.startswith(skill_increase_text) :
        char.increase_skill = 5
        char.increase_burst = 3
        if not c3.startswith(burst_increase_text) :
            logger.warning("Found skill increase at C5 but no burst increase at C3 for %s (%s)", char.hoyo_id, char.name)
        return
    unobtainable_constellation = 'The time has not yet come for this person\'s corner of the night sky to light up.'
    if c3 != unobtainable_constellation or c5 != unobtainable_constellation :
        logger.warning("Could not find talent increases for character %s (%s)", char.hoyo_id, char.name)
