
from utils import loadJson, indexById, idFromName
from constants import ITEM_LIST_JSON
from translate.textmap import lang
from translate.mhy import mhy_items

import logging

logger = logging.getLogger(__name__)

items = indexById(loadJson(ITEM_LIST_JSON))


def __g_supplyThroughItems(hoyo_id: int) -> str :
	if hoyo_id in items :
		item = items[hoyo_id]
		return idFromName(lang[str(item['nameTextMapHash'])])
	logger.warning("No item found with hoyo id %d", hoyo_id)
	return str(hoyo_id)

mhy_items.setSupplyStrategy(__g_supplyThroughItems)
	

