
from constants import LANG_JSON_TEMPLATE
from utils import loadJson

LANG_JSON = LANG_JSON_TEMPLATE.format(lang = 'EN')

lang: "dict[str, str]" = loadJson(LANG_JSON)

