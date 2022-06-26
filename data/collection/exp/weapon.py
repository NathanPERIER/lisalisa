
from utils import loadJson
from constants import EXP_WEAPON_JSON

weapon_exp: list = loadJson(EXP_WEAPON_JSON)


def readWeaponExp() -> "list[list[int]]" :
	weapon_exp.sort(key = lambda x: x['level'])
	return [
		[x['requiredExps'][i] for x in weapon_exp]
		for i in range(5)
	]
