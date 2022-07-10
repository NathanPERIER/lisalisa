
from utils import loadJson, groupByField
from constants import EXP_STATUES_JSON
from translate.mhy import mhy_items, mhy_cities

import logging

logger = logging.getLogger(__name__)

statues_exp: "dict[int,list[dict[str,any]]]" = groupByField(loadJson(EXP_STATUES_JSON), 'cityId')


# Rewards ?
def getStatuesExp(hoyo_city_id: int) -> "dict[str,dict]" :
	levels = statues_exp[hoyo_city_id]
	search_material = list(set([x['consumeItem']['itemId'] for x in levels[1:]]))
	if len(search_material) > 1 :
		logger.warning("Found %d materials for statue level-up in %s region, expected only one", len(search_material), hoyo_city_id)
	return {
		'item': mhy_items[search_material[0]],
		'counts': [level['consumeItem']['itemNum'] for level in levels[1:]]
	}
