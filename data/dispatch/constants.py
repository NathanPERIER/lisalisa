
import os

# Directories
THIS_DIR  = os.path.dirname(os.path.realpath(__file__))
DATA_DIR  = os.path.dirname(THIS_DIR)
REPO_DIR  = os.path.dirname(DATA_DIR)
RAW_DIR   = os.path.join(DATA_DIR, 'rawdata')
# FRONT_DIR = os.path.join(REPO_DIR, '')
BACK_DIR  = os.path.join(REPO_DIR, 'backend/src/main/resources/genshin')

# Constants file
CONSTANTS_FILE   = 'hardcoded/numeric_constants.json'

# Hardcoded
HC_ADV_RANK_FILE    = 'hardcoded/adventure_rank.json'
HC_ASCENSION_FILE   = 'hardcoded/ascension.json'
HC_WORLD_LEVEL_FILE = 'hardcoded/world_level.json'