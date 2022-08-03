
from constants import ITEM_MORA_ID
from translate.mhy import mhy_items
from common.props import PropType
from common.ascensions.dataobj import Ascensions, AscensionProps, AscensionLevel

import logging

logger = logging.getLogger(__name__)


def formatAscensions(ascensions: "list[AscensionLevel]", name: str, hoyo_id: int, promote_id: int, expected_nb = 6) -> Ascensions :
    if len(ascensions) != expected_nb + 1 :
        logger.warning('Expected %d ascensions (%d items) for %s (hoyo: %d / promote: %d), got %d items', 
						expected_nb, expected_nb+1, name, hoyo_id, promote_id, len(ascensions))
    ascensions.sort(key = lambda asc: asc['level'])
    res = Ascensions()
    res.costs = [
        formatCosts(asc.cost, asc.mora_cost)
        for asc in ascensions[1:]
    ]
    res.props = [
        AscensionProps.fromLevelData(asc)
        for asc in ascensions
    ]
    return res


def readAscension(asc: dict, data: "dict[int,list[AscensionLevel]]", promote_id_field: str, mora_cost_field: str) :
    promote_id = asc[promote_id_field]
    if promote_id not in data :
        data[promote_id] = []
    res = AscensionLevel()
    res.level  = asc['promoteLevel'] if 'promoteLevel' in asc else 0
    res.maxLvl = asc['unlockMaxLevel']
    props: "dict[str,float]" = {
        PropType[p['propType']].value: p['value'] if 'value' in p else 0.0
        for p in asc['addProps']
    }
    # Fix percentages not actually being percentages
    res.props = {
        prop: value * 100 if prop.endswith('%') else value
        for prop, value in props.items()
    }
    res.cost = {
        c['id']: c['count']
        for c in asc['costItems']
        if 'id' in c and 'count' in c
    }
    res.mora_cost = asc[mora_cost_field] if mora_cost_field in asc else 0
    data[promote_id].append(res)


def formatCosts(costs: "dict[int,int]", mora_cost: int) -> "dict[str,int]" :
    res = {
        mhy_items[item]: count 
        for item, count in costs.items()
    }
    if mora_cost > 0 :
        res[ITEM_MORA_ID] = mora_cost
    return res
