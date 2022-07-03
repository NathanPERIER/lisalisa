
from utils import loadJson, idFromName
from constants import WORLD_CITIES_JSON
from translate.textmap import lang
from translate.mhy import mhy_cities

def __g_filterCities(cities: list) -> list :
	return [x for x in cities if x['cityId'] < 90]

cities = __g_filterCities(loadJson(WORLD_CITIES_JSON))


def readCities() -> "dict[str,dict]" :
	res = {}
	for data in cities :
		city = {
			'hoyo_id': data['cityId'],
			'name_hash': data['cityNameTextMapHash']
		}
		city['name'] = lang(city['name_hash'])
		identifier = idFromName(city['name'])
		mhy_cities[city['hoyo_id']] = identifier
		res[identifier] = city
	return res
