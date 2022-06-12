from constants import CHAR_ASCENSIONS_JSON
from utils import loadJson

from enum import Enum

class PropType(Enum) :
    FIGHT_PROP_BASE_HP         = 'Base HP'
    FIGHT_PROP_BASE_ATTACK     = 'Base ATK'
    FIGHT_PROP_BASE_DEFENSE    = 'Base DEF'
    FIGHT_PROP_HP_PERCENT      = 'HP%'
    FIGHT_PROP_ATTACK_PERCENT  = 'ATK%'
    FIGHT_PROP_DEFENSE_PERCENT = 'DEF%'
    FIGHT_PROP_CRITICAL_HURT   = 'Crit DMG%'
    FIGHT_PROP_CRITICAL        = 'Crit Rate%'
    FIGHT_PROP_CHARGE_EFFICIENCY = 'Energy Recharge%'
    FIGHT_PROP_ELEMENT_MASTERY   = 'Elemental Mastery'
    FIGHT_PROP_PHYSICAL_ADD_HURT = 'Physical DMG%'    # TODO ?
    FIGHT_PROP_HEAL_ADD          = 'Healing Bonus%'   # TODO ?
    FIGHT_PROP_FIRE_ADD_HURT  = 'Pyro DMG%'
    FIGHT_PROP_WATER_ADD_HURT = 'Hydro DMG%'
    FIGHT_PROP_ICE_ADD_HURT   = 'Cryo DMG%'
    FIGHT_PROP_ELEC_ADD_HURT  = 'Electro DMG%'
    FIGHT_PROP_WIND_ADD_HURT  = 'Anemo DMG%'
    FIGHT_PROP_ROCK_ADD_HURT  = 'Geo DMG%'

MORA_ID = 'mora' # TODO find real id

ascensions = loadJson(CHAR_ASCENSIONS_JSON)


def readAscensions(characters: dict) :
    data = {}
    for asc in ascensions :
        __g_readAscension(asc, data)
    for char in characters.values() :
        promote_id = char['promote_id']
        if promote_id not in data :
            # TODO logging
            print(f"Warning : ascensions not found for {char['hoyo_id']}")
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
        cost[MORA_ID] = asc['scoinCost']
    data[promote_id].append({
        'level': asc['promoteLevel'] if 'promoteLevel' in asc else 0,
        'maxLvl': asc['unlockMaxLevel'],
        'props': props,
        'cost': cost
    })

def __g_formatCharAscensions(ascensions: list) -> dict :
    # TODO check that there are 6 ascensions (actually 7 items)
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
