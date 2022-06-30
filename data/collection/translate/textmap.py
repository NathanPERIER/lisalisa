
from constants import LANG_JSON_TEMPLATE
from utils import loadJson

import logging

logger = logging.getLogger(__name__)

LANG_JSON = LANG_JSON_TEMPLATE.format(lang = 'EN')

__g_lang: "dict[str, str]" = loadJson(LANG_JSON)


def lang(text_hash: int) -> str :
	str_hash = str(text_hash)
	if str_hash in __g_lang :
		return __g_lang[str_hash]
	logger.error("Translation for hash %s not found in lang", str_hash)
	return None
