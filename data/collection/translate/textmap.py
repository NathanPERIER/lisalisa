
from constants import LANG_JSON_TEMPLATE, MANUAL_LANG_JSON
from utils import loadJson, indexById

import logging

logger = logging.getLogger(__name__)

LANG_JSON = LANG_JSON_TEMPLATE.format(lang = 'EN')

__g_lang: "dict[str, str]"   = loadJson(LANG_JSON)
__g_manual: "dict[str, any]" = indexById(loadJson(MANUAL_LANG_JSON), 'textMapId')


def lang(text_hash: int) -> str :
	str_hash = str(text_hash)
	if str_hash in __g_lang :
		return __g_lang[str_hash]
	logger.error("Translation for hash %s not found in lang", str_hash)
	return None


def hashForValue(val: str) -> int :
	if val in __g_manual :
		return __g_manual[val]['textMapContentTextMapHash']
	logger.error("Text hash not found for %s", val)
	return None
