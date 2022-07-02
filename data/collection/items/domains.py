
from asyncio.log import logger
from utils import loadJson, indexById, groupByField
from constants import DOMAIN_DATA_JSON, DOMAIN_DAILY_JSON, DOMAIN_ENTRY_JSON, DOMAIN_EFFECTS_JSON, DOMAIN_POINTS_JSON
from translate.textmap import lang, hashForValue
from translate.mhy import mhy_cities

import re
from enum import Enum

class DailyDungeonType(Enum) :
	DUNGEON_SUB_TALENT = 'talent'
	DUNGEON_SUB_WEAPON = 'weapon'

class DungeonEntryType(Enum) :
	DUNGEN_ENTRY_TYPE_AVATAR_TALENT  = 'talent'
	DUNGEN_ENTRY_TYPE_WEAPON_PROMOTE = 'weapon'

DUNGEON_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

SMALL_ROMAN = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
level_reg = re.compile(r'Domain of (?:Mastery|Forgery): ([a-zA-Z -]+) (I|II|III|IV)')

DUNGEON_NAME_VAL_FIELD = 'PFMFPKFDNEK'

domains = indexById(loadJson(DOMAIN_DATA_JSON))
dailies = loadJson(DOMAIN_DAILY_JSON)
entries = loadJson(DOMAIN_ENTRY_JSON)
effects = indexById(loadJson(DOMAIN_EFFECTS_JSON))
points  = loadJson(DOMAIN_POINTS_JSON)['points']


def readDomains() : # TODO rewards !!!
	res = []
	subd = __g_readDailySubDungeons()
	subd_grouped = groupByField(subd, 'ui_type')
	for ui_type, group in subd_grouped.items() :
		dungeon_type = group[0]['type'].value # Let's suppose they're all the same
		dungeon_entry = __g_findDungeonEntry(ui_type, dungeon_type)
		if dungeon_entry is not None :
			res.append(__g_formatDungeon(group, dungeon_entry))
	return res


def __g_formatDungeon(subd: list, entry: dict) -> "dict[str,any]" :
	res = {
		'hoyo_id': entry['id'],
		'scene_id': entry['sceneId'],
		'entry_id': entry['dungeonEntryId'],
		'desc_hash': entry['descTextMapHash'],
		'type': DungeonEntryType[entry['type']]
	}
	res['desc'] = lang(res['desc_hash'])
	# Find the point to get the domain name
	point = points[str(res['entry_id'])]
	res['name_hash'] = hashForValue(point[DUNGEON_NAME_VAL_FIELD])
	res['name'] = lang(res['name_hash'])
	# Get the required AR for this domain (if any)
	search_req_ar = [
		x['param1'] for x in entry['satisfiedCond']
		if x['type'] == 'DUNGEON_ENTRY_CONDITION_LEVEL'
	]
	res['req_ar'] = max(search_req_ar) if len(search_req_ar) > 0 else None
	# We group the sub domains by name and sort them by level
	res['sub_domains'] = list(groupByField(subd, 'sub_name').values())
	for subd_group in res['sub_domains'] :
		subd_group.sort(key = lambda sd: sd['level'])
	return res


def __g_findDungeonEntry(ui_type: str, dungeon_type: str) -> dict :
	entry_type = DungeonEntryType(dungeon_type).name
	search_dungeon = [
		x for x in entries
		if x['type'] == entry_type and x['picPath'] == ui_type
	]
	if len(search_dungeon) == 0 :
		logger.error("No entry of type %d found with pic %d", dungeon_type, ui_type)
		return None
	if len(search_dungeon) > 1 :
		logger.warning("Multiple entries of type %d found with pic %d", dungeon_type, ui_type)
	return search_dungeon[0]


# Reads all the sub-domains that exist
def __g_readDailySubDungeons() -> "list[dict[str,any]]" :
	res = []
	for subd_id, days in __g_getSubDungeonsList(dailies).items() :
		subd = __g_readSubDungeon(domains[subd_id])
		subd['days'] = days
		res.append(subd)
	return res


# Get the list of all the sub-domains with the days during which they are available
def __g_getSubDungeonsList(dailies: "list[dict]") -> "dict[int,list[str]]" :
	res: "dict[int,list[str]]" = {}
	for daily in dailies :
		for day in DUNGEON_DAYS :
			sub_dungeons = daily[day]
			for subd in sub_dungeons :
				if subd not in res :
					if subd != 0 :
						res[subd] = [day]
				else :
					res[subd].append(day)
	return res


def __g_readSubDungeon(subd: dict) -> "dict[str,any]" :
	res = {
		'hoyo_id': subd['id'],
		'scene_id': subd['sceneId'],
		'reward_id': subd['passRewardPreviewID'],
		'name_hash': subd['nameTextMapHash'],
		'city': mhy_cities[subd['cityID']],
		'type': DailyDungeonType[subd['subType']],
		'reco_types': [x for x in subd['recommendElementTypes'] if x != 'None'],
		'reco_level': subd['showLevel'],
		'req_ar': subd['limitLevel'],
		'ui_type': subd['entryPicPath']
	}
	res['name'] = lang(res['name_hash'])
	m = level_reg.fullmatch(res['name'])
	# Get the sub-domain name and level (I, II, III, IV)
	if m is None :
		logger.error("Name of sub-dungeon %d does not match the expected format (%s)", 
						res['hoyo_id'], res['name'])
	else :
		res['sub_name'] = m.group(1)
		res['level'] = SMALL_ROMAN[m.group(2)]
	# Get the effect(s) applied to players in this sub-domain
	res['effects_hash'] = [
		effects[int(e)]['descTextMapHash'] for e in subd['levelConfigMap']
	]
	res['effects'] = [lang(effect_hash) for effect_hash in res['effects_hash']]
	return res
