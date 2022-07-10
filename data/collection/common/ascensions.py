
from constants import ITEM_MORA_ID
from translate.mhy import mhy_items
from common.props import PropType

import logging

logger = logging.getLogger(__name__)


def formatAscensions(ascensions: list, name: str, hoyo_id: int, promote_id: int, expected_nb = 6) -> dict :
    if len(ascensions) != expected_nb + 1 :
        logger.warning('Expected %d ascensions (%d items) for %s (hoyo: %d / promote: %d), got %d items', 
						expected_nb, expected_nb+1, name, hoyo_id, promote_id, len(ascensions))
    ascensions.sort(key = lambda asc: asc['level'])
    costs = [
        formatCosts(asc['cost'], asc['mora_cost'])
        for asc in ascensions[1:]
    ]
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
    props: "dict[str,float]" = {
        PropType[p['propType']].value: p['value'] if 'value' in p else 0.0
        for p in asc['addProps']
    }
    # Fix percentages not actually being percentages
    props = {
        prop: value * 100 if prop.endswith('%') else value
        for prop, value in props.items()
    }
    cost = {
        c['id']: c['count']
        for c in asc['costItems']
        if 'id' in c and 'count' in c
    }
    mora_cost = asc[mora_cost_field] if mora_cost_field in asc else 0
    data[promote_id].append({
        'level': asc['promoteLevel'] if 'promoteLevel' in asc else 0,
        'maxLvl': asc['unlockMaxLevel'],
        'props': props,
        'cost': cost,
        'mora_cost': mora_cost
    })


def formatCosts(costs: "dict[int,int]", mora_cost: int) -> "dict[str,int]" :
    res = {
        mhy_items[item]: count 
        for item, count in costs.items()
    }
    if mora_cost > 0 :
        res[ITEM_MORA_ID] = mora_cost
    return res
