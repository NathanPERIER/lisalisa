
from utils import loadJson, indexById, groupByField
from constants import DOMAIN_DATA_JSON, DOMAIN_DAILY_JSON, DOMAIN_ENTRY_JSON, DOMAIN_EFFECTS_JSON, DOMAIN_POINTS_JSON
from translate.textmap import lang, hashForValue
from translate.mhy import mhy_cities
from world.dataobj import Domain, SubDomain
from common.rewards import getRewards

import re
import logging
from enum import Enum

logger = logging.getLogger(__name__)

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


def readDomains() -> "list[Domain]" :
	res = []
	subd = __g_readDailySubDungeons()
	subd_grouped: "dict[str,list[SubDomain]]" = groupByField(subd, 'ui_type')
	for ui_type, group in subd_grouped.items() :
		dungeon_type = group[0].type.value # Let's suppose they're all the same
		dungeon_entry = __g_findDungeonEntry(ui_type, dungeon_type)
		if dungeon_entry is not None :
			res.append(__g_formatDungeon(group, dungeon_entry))
	return res


def __g_formatDungeon(subd: "list[SubDomain]", entry: dict) -> Domain :
	res = Domain()
	res.hoyo_id = entry['id']
	logger.debug("Formatting dungeon %s", res.hoyo_id)
	# print(entry)
	res.scene_id = entry['sceneId']
	res.entry_id = entry['dungeonEntryId']
	res.desc_hash = entry['descTextMapHash']
	res.desc = lang(res.desc_hash)
	res.type = DungeonEntryType[entry['type']]
	# Find the point to get the domain name
	point_id = str(res.entry_id)
	if point_id in points :
		point = points[point_id]
		name_ui_key = point[DUNGEON_NAME_VAL_FIELD]
	else :
		name_ui_key = f"UI_DUNGEON_ENTRY_{res.entry_id}"
	logger.debug("Found key %s for dungeon with entry id %d", name_ui_key, res.entry_id)
	res.name_hash = hashForValue(name_ui_key)
	res.name = lang(res.name_hash)
	# Get the required AR for this domain (if any)
	search_req_ar = [
		x['param1'] for x in entry['satisfiedCond']
		if x['type'] == 'DUNGEON_ENTRY_CONDITION_LEVEL'
	]
	res.req_ar = max(search_req_ar) if len(search_req_ar) > 0 else None
	# We group the sub domains by name and sort them by level
	res.sub_domains: "list[list[SubDomain]]" = list(groupByField(subd, 'sub_name').values())
	for subd_group in res.sub_domains :
		subd_group.sort(key = lambda sd: sd.level)
	return res


def __g_findDungeonEntry(ui_type: str, dungeon_type: str) -> dict :
	logger.debug("Searching for dungeon entry %s (type %s)", ui_type, dungeon_type)
	entry_type = DungeonEntryType(dungeon_type).name
	search_dungeon = [
		x for x in entries
		if x['type'] == entry_type and x['picPath'] == ui_type
	]
	if len(search_dungeon) == 0 :
		logger.error("No entry of type %s found with pic %s", dungeon_type, ui_type)
		return None
	if len(search_dungeon) > 1 :
		logger.warning("Multiple entries of type %s found with pic %s", dungeon_type, ui_type)
	return search_dungeon[0]


# Reads all the sub-domains that exist
def __g_readDailySubDungeons() -> "list[SubDomain]" :
	res = []
	for subd_id, days in __g_getSubDungeonsList(dailies).items() :
		subd = __g_readSubDungeon(domains[subd_id])
		subd.days = days
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


def __g_readSubDungeon(subd: dict) -> SubDomain :
	res = SubDomain()
	res.hoyo_id   = subd['id']
	res.scene_id  = subd['sceneId']
	res.reward_id = subd['passRewardPreviewID']
	res.name_hash = subd['nameTextMapHash']
	res.name = lang(res.name_hash)
	res.city = mhy_cities[subd['cityID']]
	res.type = DailyDungeonType[subd['subType']]
	res.reco_types = [x for x in subd['recommendElementTypes'] if x != 'None']
	res.reco_level = subd['showLevel']
	res.req_ar = subd['limitLevel']
	# Get the sub-domain name and level (I, II, III, IV)
	m = level_reg.fullmatch(res.name)
	if m is None :
		logger.error("Name of sub-dungeon %d does not match the expected format (%s)", 
						res.hoyo_id, res.name)
	else :
		res.sub_name = m.group(1)
		res.level = SMALL_ROMAN[m.group(2)]
	# Get the effect(s) applied to players in this sub-domain
	res.effects_hash = [
		effects[int(e)]['descTextMapHash'] for e in subd['levelConfigMap']
	]
	res.effects = [lang(effect_hash) for effect_hash in res.effects_hash]
	# Retrieve the preview rewards
	rewards = getRewards(res.reward_id, True)
	for item_id, str_count in rewards.items() :
		# Basically the special items (talent lvl up, weapon enhancement) have a count that is
		# either the representation of a float or an empty string
		if len(str_count) == 0 or '.' in str_count :
			res.special_items.append(item_id)
		else :
			res.rewards[item_id] = int(str_count)
	# This will help grouping sub-domains together
	res.ui_type = subd['entryPicPath']
	return res
