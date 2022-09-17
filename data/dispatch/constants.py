
import os

# Directories
THIS_DIR  = os.path.dirname(os.path.realpath(__file__))
DATA_DIR  = os.path.dirname(THIS_DIR)
REPO_DIR  = os.path.dirname(DATA_DIR)
RAW_DIR   = os.path.join(DATA_DIR, 'rawdata')
BACK_DIR  = os.path.join(REPO_DIR, 'backend/src/main/resources/genshin')
FRONT_DIR = os.path.join(REPO_DIR, 'frontend/src/assets/data')

# Constants file
CONSTANTS_FILE   = 'hardcoded/numeric_constants.json'

# Hardcoded
HC_ADV_RANK_FILE    = 'hardcoded/adventure_rank.json'
HC_ASCENSION_FILE   = 'hardcoded/ascension.json'
HC_WORLD_LEVEL_FILE = 'hardcoded/world_level.json'

CHARACTERS_FOLDER = 'characters'
CHARACTERS_IGNORED = ['traveler_boy_common', 'traveler_girl_common']
