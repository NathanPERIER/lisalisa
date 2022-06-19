
from utils import loadJson
from constants import WEAPON_ASCENSIONS_JSON
from common.ascensions import formatAscensions as __g_formatAscensions
from common.ascensions import readAscension    as __g_readAscension

import logging

logger = logging.getLogger(__name__)

ascensions = loadJson(WEAPON_ASCENSIONS_JSON)


PROMOTE_ID_FIELD = 'weaponPromoteId'
MORA_COST_FIELD  = 'coinCost'

# TODO keep only useful parameters in props
def readAscensions(weapons: dict) :
	data = {}
	for asc in ascensions :
		__g_readAscension(asc, data, PROMOTE_ID_FIELD, MORA_COST_FIELD)
	for weapon in weapons.values() :
		promote_id = weapon['promote_id']
		if promote_id not in data :
			logger.warning('Ascensions not found for %s (%d)', weapon['name'], weapon['hoyo_id'])
		else :
			expected = 6 if weapon['rarity'] >= 3 else 4
			weapon['ascensions'] = __g_formatAscensions(data[promote_id], weapon, expected)
