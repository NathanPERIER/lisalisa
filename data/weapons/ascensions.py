
from utils import loadJson
from constants import WEAPON_ASCENSIONS_JSON, ITEM_MORA_ID, PropType
from common.ascensions import formatAscensions as __g_formatAscensions

import logging

logger = logging.getLogger(__name__)

ascensions = loadJson(WEAPON_ASCENSIONS_JSON)


def readAscensions(weapons: dict) :
	data = {}
	for asc in ascensions :
		__g_readAscension(asc, data)
	for weapon in weapons.values() :
		promote_id = weapon['promote_id']
		if promote_id not in data :
			logger.warning('Ascensions not found for %s (%d)', weapon['name'], weapon['hoyo_id'])
		else :
			expected = 6 if weapon['rarity'] >= 3 else 4
			weapon['ascensions'] = __g_formatAscensions(data[promote_id], weapon, expected)
    

def __g_readAscension(asc: dict, data: dict) :
    promote_id = asc['weaponPromoteId']
    if promote_id not in data :
        data[promote_id] = []
    props = {
        PropType[p['propType']].value: p['value'] if 'value' in p else 0.0
        for p in asc['addProps']
    }
    cost = {
        c['id']: c['count']
        for c in asc['costItems']
        if 'id' in c and 'count' in c
    }
    if 'coinCost' in asc :
        cost[ITEM_MORA_ID] = asc['coinCost']
    data[promote_id].append({
        'level': asc['promoteLevel'] if 'promoteLevel' in asc else 0,
        'maxLvl': asc['unlockMaxLevel'],
        'props': props,
        'cost': cost
    })
	