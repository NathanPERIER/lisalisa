
from utils import loadJson, indexById, idFromName
from constants import ITEM_LIST_JSON
from translate.textmap import lang
from common.text import clearFormat
from translate.mhy import mhy_items
from items.dataobj import Item

import logging

logger = logging.getLogger(__name__)

items = indexById(loadJson(ITEM_LIST_JSON))


__g_auto_translated = {}

def getAutoTranslated() -> dict :
	return __g_auto_translated


def readAllItems() -> "list[Item]" :
	return [
		__g_readFullItem(item) for item in items.values()
		if item['nameTextMapHash'] in lang
	]


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
	res.desc = clearFormat(lang(res.desc_hash)) if res.desc_hash in lang else None
	res.type = item['itemType']
	res.type_desc = lang(res.type_hash) if res.type_hash in lang else None
	return res


def __g_readFullItem(item: dict) -> Item :
	res = readItem(item)
	if 'gadgetId' in item :
		res.gadget_id = item['gadgetId']
	return res
