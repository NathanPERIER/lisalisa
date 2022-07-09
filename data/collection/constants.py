
import os

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
ARTIFACT_PIECES_JSON  = os.path.join(EXCEL_DIR, 'ReliquaryExcelConfigData.json')
ARTIFACT_SETS_JSON    = os.path.join(EXCEL_DIR, 'ReliquarySetExcelConfigData.json')
ARTIFACT_EQUIP_JSON   = os.path.join(EXCEL_DIR, 'EquipAffixExcelConfigData.json')
ARTIFACT_DISPLAY_JSON = os.path.join(EXCEL_DIR, 'DisplayItemExcelConfigData.json')
ARTIFACT_CODEX_JSON   = os.path.join(EXCEL_DIR, 'ReliquaryCodexExcelConfigData.json')
ARTIFACT_AFFIXES_JSON = os.path.join(EXCEL_DIR, 'ReliquaryAffixExcelConfigData.json')
ARTIFACT_CURVES_JSON  = os.path.join(EXCEL_DIR, 'ReliquaryLevelExcelConfigData.json')

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

