
from utils import loadJson
from constants import EXP_CHARACTER_JSON

char_exp: list = loadJson(EXP_CHARACTER_JSON)


def readCharacterExp() -> "list[int]" :
	char_exp.sort(key = lambda x: x['level'])
	return [x['exp'] for x in char_exp]
