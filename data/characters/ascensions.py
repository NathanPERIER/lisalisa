from constants import CHAR_ASCENSIONS_JSON, ITEM_MORA_ID, PropType
from utils import loadJson

import logging

logger = logging.getLogger(__name__)

ascensions = loadJson(CHAR_ASCENSIONS_JSON)


def readAscensions(characters: dict) :
    data = {}
    for asc in ascensions :
        __g_readAscension(asc, data)
    for char in characters.values() :
        promote_id = char['promote_id']
        if promote_id not in data :
            logger.warning('Ascensions not found for %s (%d)', char['name'], char['hoyo_id'])
        else :
            char['ascensions'] = __g_formatCharAscensions(data[promote_id])
    

def __g_readAscension(asc: dict, data: dict) :
    promote_id = asc['avatarPromoteId']
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
    if 'scoinCost' in asc :
        cost[ITEM_MORA_ID] = asc['scoinCost']
    data[promote_id].append({
        'level': asc['promoteLevel'] if 'promoteLevel' in asc else 0,
        'maxLvl': asc['unlockMaxLevel'],
        'props': props,
        'cost': cost
    })

def __g_formatCharAscensions(ascensions: list) -> dict :
    if len(ascensions) == 7 :
        ascensions = ascensions[1:]
    else :
        logger.warning('Expected 6 ascensions (7 items), got %d items', len(ascensions))
    ascensions.sort(key = lambda asc: asc['level'])
    # TODO translate the item ids (hoyo_id)
    costs = [asc['cost'] for asc in ascensions]
    props = [
        {
            'values': asc['props'], 
            'until': asc['maxLvl']
        }
        for asc in ascensions
    ]
    return {
        'costs': costs,
        'props': props
    }
