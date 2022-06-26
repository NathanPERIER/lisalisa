
from utils import loadJson, groupByField
from constants import EXP_OFFERINGS_JSON
from translate.mhy import mhy_items

offerings_exp: list = loadJson(EXP_OFFERINGS_JSON)

offerings_names = {
	1: 'Frostbearing Tree\'s Gratitude',
	2: 'Sacred Sakura\'s Favor',
	3: 'Enhance the Lumenstone Adjuvant'
}


# Rewards ?
def readOfferingsExp() :
	res = {}
	oexp = groupByField(offerings_exp, 'offeringId')
	for offering_id, levels in oexp.items() :
		if offering_id in offerings_names :
			name = offerings_names[offering_id]
			levels = [x for x in levels if 'level' in x]
			levels.sort(key = lambda x: x['level'])
			res[name] = [__g_readOfferingLevel(lvl) for lvl in levels[1:]]
	return res


def __g_readOfferingLevel(level: dict) -> dict :
	res = {}
	for cost in level['actionVec'] :
		if 'id' in cost and 'count' in cost :
			identifier = mhy_items[cost['id']]
			res[identifier] = cost['count']
	return res
