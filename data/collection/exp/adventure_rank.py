
from utils import loadJson
from constants import EXP_ADVENTURE_RANK_JSON

ar_exp: list = loadJson(EXP_ADVENTURE_RANK_JSON)


# rewards ?
def readAdventureRankExp() -> "list[int]" :
	ar_exp.sort(key = lambda x: x['level'])
	return [x['exp'] for x in ar_exp if 'exp' in x]
