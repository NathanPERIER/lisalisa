
from utils import loadJson, groupByField
from constants import EXP_REPUTATION_JSON
from translate.mhy import mhy_cities

reputation_exp: list = loadJson(EXP_REPUTATION_JSON)


# Rewards ?
def readReputationExp() -> "dict[str,list[int]]" :
	res = {}
	rexp = groupByField(reputation_exp, 'cityId')
	for city_hoyo_id, levels in rexp.items() :
		city_id = mhy_cities[city_hoyo_id]
		levels.sort(key = lambda x: x['level'])
		res[city_id] = [x['nextLevelExp'] for x in levels if 'nextLevelExp' in x]
	return res
