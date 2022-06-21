
from utils import loadJson, indexById, idFromName
from constants import ITEM_LIST_JSON
from translate.textmap import lang
from translate.mhy import mhy_items

import logging

logger = logging.getLogger(__name__)

items = indexById(loadJson(ITEM_LIST_JSON))


__g_auto_translated = {}

def getAutoTranslated() -> dict :
	return __g_auto_translated


def __g_supplyThroughItems(hoyo_id: int) -> str :
	if hoyo_id in items :
		item = items[hoyo_id]
		identifier = idFromName(lang[str(item['nameTextMapHash'])])
		__g_auto_translated[identifier] = __g_readItem(item)
		return identifier
	logger.warning("No item found with hoyo id %d", hoyo_id)
	return str(hoyo_id)

mhy_items.setSupplyStrategy(__g_supplyThroughItems)


def __g_readItem(item: dict) -> dict :
	res = {
		'hoyo_id': item['id'],
		'name_hash': item['nameTextMapHash'],
		'desc_hash': item['descTextMapHash'],
		'type_hash': item['typeDescTextMapHash'],
		'rarity': item['rankLevel']
	}
	res['name'] = lang[str(res['name_hash'])]
	res['desc'] = lang[str(res['desc_hash'])]
	res['type'] = lang[str(res['type_hash'])]
	sp_desc_hash = item['specialDescTextMapHash']
	sp_desc = lang[str(sp_desc_hash)]
	if sp_desc != '' :
		print(f"SP: {sp_desc}")
	effect_desc_hash = item['effectDescTextMapHash']
	effect_desc = lang[str(effect_desc_hash)]
	if effect_desc != '' :
		print(f"EFF: {effect_desc}")
	interaction_hash = item['interactionTitleTextMapHash']
	interaction = lang[str(interaction_hash)]
	if interaction != '' :
		print(f"INTERACT: {interaction}")
	return res
