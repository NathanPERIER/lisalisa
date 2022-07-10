
from utils import loadJson, groupByField
from constants import EXP_REPUTATION_JSON
from translate.mhy import mhy_cities

reputation_exp: "dict[int,list[dict[str,any]]]" = groupByField(loadJson(EXP_REPUTATION_JSON), 'cityId')


# Rewards ?
def getReputationExp(hoyo_city_id: int) -> "list[int]" :
	levels = reputation_exp[hoyo_city_id]
	levels.sort(key = lambda x: x['level'])
	return [x['nextLevelExp'] for x in levels if 'nextLevelExp' in x]
