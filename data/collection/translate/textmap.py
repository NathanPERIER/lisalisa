
from constants import LANG_JSON_TEMPLATE, MANUAL_LANG_JSON
from utils import loadJson, indexById

import logging

logger = logging.getLogger(__name__)

LANG_JSON = LANG_JSON_TEMPLATE.format(lang = 'EN')

__g_lang: "dict[str, str]"   = loadJson(LANG_JSON)
__g_manual: "dict[str, any]" = indexById(loadJson(MANUAL_LANG_JSON), 'textMapId')


class Translator :
	def __init__(self, textmap: "dict[str,str]") :
		self._textmap = textmap
	def __getitem__(self, hash: str) :
		if hash in self._textmap :
			return self._textmap[hash]
		logger.error("Translation for hash %s not found in lang", hash)
		return None
	def __call__(self, hash: int) :
		return self[str(hash)]
	def __contains__(self, hash: int) :
		return str(hash) in self._textmap

lang = Translator(__g_lang)


def hashForValue(val: str) -> int :
	if val in __g_manual :
		return __g_manual[val]['textMapContentTextMapHash']
	logger.error("Text hash not found for %s", val)
	return None
