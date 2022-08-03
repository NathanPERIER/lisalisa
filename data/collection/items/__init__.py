
from utils import loadJson, indexById, idFromName
from constants import ITEM_LIST_JSON
from translate.textmap import lang
from translate.mhy import mhy_items
from common.dataobj.item import Item

import logging

logger = logging.getLogger(__name__)

items = indexById(loadJson(ITEM_LIST_JSON))


__g_auto_translated = {}

def getAutoTranslated() -> dict :
	return __g_auto_translated


def __g_supplyThroughItems(str_id: str) -> str :
	hoyo_id = int(str_id)
	if hoyo_id in items :
		item = items[hoyo_id]
		identifier = idFromName(lang(item['nameTextMapHash']))
		__g_auto_translated[identifier] = readItem(item)
		return identifier
	logger.warning("No item found with hoyo id %d", hoyo_id)
	return str(hoyo_id)

mhy_items.setSupplyStrategy(__g_supplyThroughItems)


def readItem(item: dict) -> Item :
	res = Item()
	res.hoyo_id = item['id']
	res.name_hash = item['nameTextMapHash']
	res.desc_hash = item['descTextMapHash']
	res.type_hash = item['typeDescTextMapHash']
	res.rarity = item['rankLevel'] if 'rankLevel' in item else 1
	res.name = lang(res.name_hash)
	res.desc = lang(res.desc_hash)
	res.type = lang(res.type_hash)
	sp_desc_hash = item['specialDescTextMapHash']
	if sp_desc_hash in lang :
		sp_desc = lang(sp_desc_hash)
		print(f"SP: {sp_desc}")
	effect_desc_hash = item['effectDescTextMapHash']
	if effect_desc_hash in lang :
		effect_desc = lang(effect_desc_hash)
		print(f"EFF: {effect_desc}")
	interaction_hash = item['interactionTitleTextMapHash']
	if interaction_hash in lang :
		interaction = lang(interaction_hash)
		print(f"INTERACT: {interaction}")
	return res
