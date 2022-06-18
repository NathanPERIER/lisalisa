
import os

# Directories
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_DIR = os.path.dirname(THIS_DIR)
DEST_DIR = os.path.join(REPO_DIR, 'rawdata')
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

# Artifacts
ARTIFACT_DATA_JSON   = os.path.join(EXCEL_DIR, 'ReliquaryExcelConfigData.json')
ARTIFACT_CURVES_JSON = os.path.join(EXCEL_DIR, 'ReliquaryLevelExcelConfigData.json')
ARTIFACT_SETS_JSON   = os.path.join(EXCEL_DIR, 'ReliquarySetExcelConfigData.json')

# Items
ITEM_LIST_JSON    = os.path.join(EXCEL_DIR, 'MaterialExcelConfigData.json')
ITEM_GLIDERS_JSON = os.path.join(EXCEL_DIR, 'AvatarFlycloakExcelConfigData.json')
ITEM_REWARDS_JSON = os.path.join(EXCEL_DIR, 'RewardExcelConfigData.json')

# Domains
DOMAIN_DATA_JSON    = os.path.join(EXCEL_DIR, 'DungeonExcelConfigData.json')
DOMAIN_DAILY_JSON = os.path.join(EXCEL_DIR, 'DailyDungeonConfigData.json')

# Exp
EXP_FRIENDSHIP_JSON     = os.path.join(EXCEL_DIR, 'AvatarFettersLevelExcelConfigData.json')
EXP_OFFERINGS_JSON      = os.path.join(EXCEL_DIR, 'OfferingLevelUpExcelConfigData.json')
EXP_REPUTATION_JSON     = os.path.join(EXCEL_DIR, 'ReputationLevelExcelConfigData.json')
EXP_ADVENTURE_RANK_JSON = os.path.join(EXCEL_DIR, 'PlayerLevelExcelConfigData.json')
EXP_CHARACTER_JSON      = os.path.join(EXCEL_DIR, 'AvatarLevelExcelConfigData.json')
EXP_WEAPON_JSON         = os.path.join(EXCEL_DIR, 'WeaponLevelExcelConfigData.json')

# Translation
LANG_JSON_TEMPLATE = os.path.join(REPO_DIR, 'GenshinData/TextMap/TextMap{lang}.json')

# Misc
COOKING_RECIPES_JSON = os.path.join(EXCEL_DIR, 'CookRecipeExcelConfigData.json')
WORLD_CITIES_JSON    = os.path.join(EXCEL_DIR, 'CityConfigData.json')
# FRIENDSHIP_REWARDS_JSON = os.path.join(EXCEL_DIR, 'FetterCharacterCardExcelConfigData.json')


ITEM_MORA_ID = 'mora' # TODO
