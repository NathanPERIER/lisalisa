
from utils import loadJson, indexById, groupByField
from constants import ARTIFACT_SETS_JSON, ARTIFACT_EQUIP_JSON
from translate.textmap import lang
from common.dataobj.artifact import ArtifactSet, ArtifactSetEquip

import logging

logger = logging.getLogger(__name__)


def __g_filterSets(sets: "list[dict[str,any]]") -> "list[dict[str,any]]" :
	filtered = [
		art_set for art_set in sets
		if 'DisableFilter' not in art_set or art_set['DisableFilter'] != 1
	]
	return indexById(filtered, 'setId')

sets = __g_filterSets(loadJson(ARTIFACT_SETS_JSON))
equips = groupByField(loadJson(ARTIFACT_EQUIP_JSON), 'id')


def readArtifactSet(set_id: dict) -> ArtifactSet :
	art_set = sets[set_id]
	res = ArtifactSet()
	res.hoyo_id = art_set['setId']
	res.equip_id = art_set['EquipAffixId']
	# Bonuses
	need_nums = art_set['setNeedNum']
	equip_data = equips[res.equip_id]
	if len(need_nums) != len(equip_data) :
		logger.warning("Found %d equips for artifact set %d, expected %d", 
							len(equip_data), res.hoyo_id, len(need_nums))
	equip_data.sort(key = lambda x: x['level'] if 'level' in x else 0)
	res.bonuses = [
		__g_readEquip(equip, need_num)
		for need_num, equip in zip(need_nums, equip_data)
	]
	return res


def __g_readEquip(equip: dict, need_num: int) -> ArtifactSetEquip :
	res = ArtifactSetEquip()
	res.hoyo_id = equip['affixId']
	res.name_hash = equip['nameTextMapHash']
	res.desc_hash = equip['descTextMapHash']
	res.nb_req = need_num
	res.name = lang(res.name_hash)
	res.desc = lang(res.desc_hash)
	return res

