
from utils import loadJson, idFromName
from constants import ITEM_GLIDERS_JSON
from translate.textmap import lang
from translate.mhy import mhy_items
from items import items

import logging

logger = logging.getLogger(__name__)

gliders = loadJson(ITEM_GLIDERS_JSON)


def readGliders() :
	res = {}

	for glider in gliders :
		data = {
			'hoyo_id': glider['materialId'],
			'name_hash': glider['nameTextMapHash'],
			'desc_hash': glider['descTextMapHash']
		}
		data['name'] = lang[str(data['name_hash'])]
		data['desc'] = lang[str(data['desc_hash'])]
		if glider['flycloakId'] != data['hoyo_id'] :
			logger.info("Glider with id %d has a different material id %s", glider['flycloakId'], data['hoyo_id'])
		
		item = items[data['hoyo_id']]
		data['rarity'] = item['rankLevel']

		identifier = idFromName(data['name'])
		mhy_items[data['hoyo_id']] = identifier
		res[identifier] = data
	
	return res
