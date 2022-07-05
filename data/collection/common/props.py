
from enum import Enum

class PropType(Enum) :
    FIGHT_PROP_BASE_HP         = 'Base HP'
    FIGHT_PROP_BASE_ATTACK     = 'Base ATK'
    FIGHT_PROP_BASE_DEFENSE    = 'Base DEF'
    FIGHT_PROP_HP              = 'HP'
    FIGHT_PROP_ATTACK          = 'ATK'
    FIGHT_PROP_DEFENSE         = 'DEF'
    FIGHT_PROP_HP_PERCENT      = 'HP%'
    FIGHT_PROP_ATTACK_PERCENT  = 'ATK%'
    FIGHT_PROP_DEFENSE_PERCENT = 'DEF%'
    FIGHT_PROP_CRITICAL_HURT   = 'Crit DMG%'
    FIGHT_PROP_CRITICAL        = 'Crit Rate%'
    FIGHT_PROP_CHARGE_EFFICIENCY = 'Energy Recharge%'
    FIGHT_PROP_ELEMENT_MASTERY   = 'Elemental Mastery'
    FIGHT_PROP_PHYSICAL_ADD_HURT = 'Physical DMG%'
    FIGHT_PROP_HEAL_ADD          = 'Healing Bonus%'
    FIGHT_PROP_FIRE_ADD_HURT  = 'Pyro DMG%'
    FIGHT_PROP_WATER_ADD_HURT = 'Hydro DMG%'
    FIGHT_PROP_ICE_ADD_HURT   = 'Cryo DMG%'
    FIGHT_PROP_ELEC_ADD_HURT  = 'Electro DMG%'
    FIGHT_PROP_WIND_ADD_HURT  = 'Anemo DMG%'
    FIGHT_PROP_ROCK_ADD_HURT  = 'Geo DMG%'
    FIGHT_PROP_GRASS_ADD_HURT = 'Dendro DMG%'
    FIGHT_PROP_FIRE_SUB_HURT  = 'Pyro Res%'
