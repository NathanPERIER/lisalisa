
from constants import ITEM_MORA_ID, PropType

import logging

logger = logging.getLogger(__name__)


def formatAscensions(ascensions: list, name: str, hoyo_id: int, promote_id: int, expected_nb = 6) -> dict :
    if len(ascensions) == expected_nb + 1 :
        ascensions = ascensions[1:]
    else :
        logger.warning('Expected %d ascensions (%d items) for %s (hoyo: %d / promote: %d), got %d items', 
						expected_nb, expected_nb+1, name, hoyo_id, promote_id, len(ascensions))
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


def readAscension(asc: dict, data: dict, promote_id_field: str, mora_cost_field: str) :
    promote_id = asc[promote_id_field]
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
    if mora_cost_field in asc :
        cost[ITEM_MORA_ID] = asc[mora_cost_field]
    data[promote_id].append({
        'level': asc['promoteLevel'] if 'promoteLevel' in asc else 0,
        'maxLvl': asc['unlockMaxLevel'],
        'props': props,
        'cost': cost
    })