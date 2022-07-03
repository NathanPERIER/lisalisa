
import os
from enum import Enum

# Directories
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.dirname(THIS_DIR)
REPO_DIR = os.path.dirname(DATA_DIR)
DEST_DIR = os.path.join(DATA_DIR, 'rawdata')
BIN_DIR  = os.path.join(REPO_DIR, 'GenshinData/BinOutput')
EXCEL_DIR = os.path.join(REPO_DIR, 'GenshinData/ExcelBinOutput')


# Characters
CHAR_DATA_JSON        = os.path.join(EXCEL_DIR, 'AvatarExcelConfigData.json')
CHAR_INFO_JSON        = os.path.join(EXCEL_DIR, 'FetterInfoExcelConfigData.json')
CHAR_SKINS_JSON       = os.path.join(EXCEL_DIR, 'AvatarCostumeExcelConfigData.json')
CHAR_CURVES_JSON      = os.path.join(EXCEL_DIR, 'AvatarCurveExcelConfigData.json')
CHAR_ASCENSIONS_JSON  = os.path.join(EXCEL_DIR, 'AvatarPromoteExcelConfigData.json')
CHAR_SKILLS_JSON      = os.path.join(EXCEL_DIR, 'AvatarSkillExcelConfigData.json')
CHAR_SKILL_DEPOT_JSON = os.path.join(EXCEL_DIR, 'AvatarSkillDepotExcelConfigData.json')
CHAR_TALENTS_JSON     = os.path.join(EXCEL_DIR, 'AvatarTalentExcelConfigData.json')
CHAR_PROUD_SKILL_JSON = os.path.join(EXCEL_DIR, 'ProudSkillExcelConfigData.json')

# Weapons
WEAPON_DATA_JSON       = os.path.join(EXCEL_DIR, 'WeaponExcelConfigData.json')
WEAPON_CURVES_JSON     = os.path.join(EXCEL_DIR, 'WeaponCurveExcelConfigData.json')
WEAPON_ASCENSIONS_JSON = os.path.join(EXCEL_DIR, 'WeaponPromoteExcelConfigData.json')
WEAPON_ABILITY_JSON    = os.path.join(EXCEL_DIR, 'EquipAffixExcelConfigData.json')
# DocumentExcelConfigData.json (storyId)
# LocalizationExcelConfigData.json


# Artifacts
ARTIFACT_DATA_JSON   = os.path.join(EXCEL_DIR, 'ReliquaryExcelConfigData.json')
ARTIFACT_CURVES_JSON = os.path.join(EXCEL_DIR, 'ReliquaryLevelExcelConfigData.json')
ARTIFACT_SETS_JSON   = os.path.join(EXCEL_DIR, 'ReliquarySetExcelConfigData.json')

# Items
ITEM_LIST_JSON         = os.path.join(EXCEL_DIR, 'MaterialExcelConfigData.json')
ITEM_GLIDERS_JSON      = os.path.join(EXCEL_DIR, 'AvatarFlycloakExcelConfigData.json')
ITEM_REWARDS_JSON      = os.path.join(EXCEL_DIR, 'RewardExcelConfigData.json')
ITEM_REWARDS_PREV_JSON = os.path.join(EXCEL_DIR, 'RewardPreviewExcelConfigData.json')

# Domains
DOMAIN_DATA_JSON    = os.path.join(EXCEL_DIR, 'DungeonExcelConfigData.json')
DOMAIN_DAILY_JSON   = os.path.join(EXCEL_DIR, 'DailyDungeonConfigData.json')
DOMAIN_ENTRY_JSON   = os.path.join(EXCEL_DIR, 'DungeonEntryExcelConfigData.json')
DOMAIN_EFFECTS_JSON = os.path.join(EXCEL_DIR, 'DungeonLevelEntityConfigData.json')
DOMAIN_POINTS_JSON  = os.path.join(BIN_DIR,   'Scene/Point/scene3_point.json')

# Exp
EXP_FRIENDSHIP_JSON     = os.path.join(EXCEL_DIR, 'AvatarFettersLevelExcelConfigData.json')
EXP_OFFERINGS_JSON      = os.path.join(EXCEL_DIR, 'OfferingLevelUpExcelConfigData.json')
EXP_REPUTATION_JSON     = os.path.join(EXCEL_DIR, 'ReputationLevelExcelConfigData.json')
EXP_STATUES_JSON         = os.path.join(EXCEL_DIR, 'CityLevelupConfigData.json')
EXP_ADVENTURE_RANK_JSON = os.path.join(EXCEL_DIR, 'PlayerLevelExcelConfigData.json')
EXP_CHARACTER_JSON      = os.path.join(EXCEL_DIR, 'AvatarLevelExcelConfigData.json')
EXP_WEAPON_JSON         = os.path.join(EXCEL_DIR, 'WeaponLevelExcelConfigData.json')

# Translation
LANG_JSON_TEMPLATE = os.path.join(REPO_DIR,  'GenshinData/TextMap/TextMap{lang}.json')
MANUAL_LANG_JSON   = os.path.join(EXCEL_DIR, 'ManualTextMapConfigData.json')

# Misc
COOKING_RECIPES_JSON = os.path.join(EXCEL_DIR, 'CookRecipeExcelConfigData.json')
SPECIAL_DISHES_JSON  = os.path.join(EXCEL_DIR, 'CookBonusExcelConfigData.json')
WORLD_CITIES_JSON    = os.path.join(EXCEL_DIR, 'CityConfigData.json')
# FRIENDSHIP_REWARDS_JSON = os.path.join(EXCEL_DIR, 'FetterCharacterCardExcelConfigData.json')


ITEM_MORA_ID = 'mora'


# TODO move to common
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
    FIGHT_PROP_PHYSICAL_ADD_HURT = 'Physical DMG%'
    FIGHT_PROP_HEAL_ADD          = 'Healing Bonus%'
    FIGHT_PROP_FIRE_ADD_HURT  = 'Pyro DMG%'
    FIGHT_PROP_WATER_ADD_HURT = 'Hydro DMG%'
    FIGHT_PROP_ICE_ADD_HURT   = 'Cryo DMG%'
    FIGHT_PROP_ELEC_ADD_HURT  = 'Electro DMG%'
    FIGHT_PROP_WIND_ADD_HURT  = 'Anemo DMG%'
    FIGHT_PROP_ROCK_ADD_HURT  = 'Geo DMG%'
