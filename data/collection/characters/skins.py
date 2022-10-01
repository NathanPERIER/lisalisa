
from utils import loadJson, idFromName
from constants import CHAR_SKINS_JSON
from characters.dataobj import Character, CharSkin
from translate.textmap import lang

import logging

logger = logging.getLogger(__name__)


# Change between versions (is annoying)
CHARACTER_FIELD_NAME = 'PDBPABLOMMA'
ICON_FIELD_NAME = 'MKPEEANCLCO'
RARITY_FIELD_NAME = 'OPHHKALFACK'

skins = loadJson(CHAR_SKINS_JSON)


def readSkins(characters: "dict[str,Character]") :
    for skin in skins :
        __g_readSkin(skin, characters)
    for char in characters.values() :
        if char.skins['default'] is None :
            logger.warning('No default skin for %s (%d)', char.name, char.hoyo_id)

def __g_readSkin(skin: dict, characters: "dict[str,Character]") :
    data = CharSkin()
    data.hoyo_id = skin['itemId'] if 'itemId' in skin else None
    data.name_hash = skin['nameTextMapHash']
    data.desc_hash = skin['descTextMapHash']
    data.name = lang(data.name_hash)
    data.desc = lang(data.desc_hash)
    data.icon = skin[ICON_FIELD_NAME]
    data.restricted = skin['hide'] if 'hide' in skin else False
    char_id = skin[CHARACTER_FIELD_NAME]
    char = characters[char_id]
    if 'isDefault' in skin and skin['isDefault'] :
        if char.skins['default'] is not None :
            logger.warning("Overriding default skin %s for %s (%d)", 
                char.skins['default']['name'], char.name, char.hoyo_id)
        char.skins.default = data
    else :
        skin_id = idFromName(data.name)
        if skin_id == 'default' :
            logger.warning("Non-default skin %s with id `default` found for character %s (%s), renaming to `_default`",
                data.hoyo_id, char.hoyo_id, char.name)
            skin_id = '_default'
        char.skins.alt[skin_id] = data