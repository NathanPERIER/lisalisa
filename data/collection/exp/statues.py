
from utils import loadJson, groupByField
from constants import EXP_STATUES_JSON
from translate.mhy import mhy_items, mhy_cities

import logging

logger = logging.getLogger(__name__)

statues_exp: list = loadJson(EXP_STATUES_JSON)


# Rewards ?
def readStatuesExp() -> "dict[str,dict]" :
	res = {}
	sexp = groupByField(statues_exp, 'cityId')
	for city_hoyo_id, levels in sexp.items() :
		city_id = mhy_cities[city_hoyo_id]
		search_material = list(set([x['consumeItem']['itemId'] for x in levels[1:]]))
		if len(search_material) > 1 :
			logger.warning("Found %d materials for statue level-up in region %s, expected only one", len(search_material), city_id)
		res[city_id] = {
			'item': mhy_items[search_material[0]],
			'counts': [level['consumeItem']['itemNum'] for level in levels[1:]]
		}
	return res
