
import os

# Directories
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_DIR = os.path.dirname(THIS_DIR)
DEST_DIR = os.path.join(REPO_DIR, 'rawdata')
EXCEL_DIR = os.path.join(REPO_DIR, 'GenshinData/ExcelBinOutput')


# Characters
CHAR_DATA_JSON           = os.path.join(EXCEL_DIR, 'AvatarExcelConfigData.json')
CHAR_INFO_JSON           = os.path.join(EXCEL_DIR, 'FetterInfoExcelConfigData.json')
CHAR_SKINS_JSON          = os.path.join(EXCEL_DIR, 'AvatarCostumeExcelConfigData.json')
CHAR_CURVES_JSON         = os.path.join(EXCEL_DIR, 'AvatarCurveExcelConfigData.json')
CHAR_ASCENSIONS_JSON     = os.path.join(EXCEL_DIR, 'AvatarPromoteExcelConfigData.json')
CHAR_SKILLS_JSON         = os.path.join(EXCEL_DIR, 'AvatarSkillExcelConfigData.json')
CHAR_TALENTS_JSON        = os.path.join(EXCEL_DIR, 'AvatarSkillDepotExcelConfigData.json')
CHAR_CONSTELLATIONS_JSON = os.path.join(EXCEL_DIR, 'AvatarTalentExcelConfigData.json')

# Exp
FRIENDSHIP_JSON = os.path.join(EXCEL_DIR, 'AvatarFettersLevelExcelConfigData.json')

# Translation
LANG_JSON_TEMPLATE = os.path.join(REPO_DIR, 'GenshinData/TextMap/TextMap{lang}.json')

# Misc
COOKING_RECIPES_JSON = os.path.join(EXCEL_DIR, 'CookRecipeExcelConfigData.json')
