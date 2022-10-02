
from utils import loadJson, idFromName
from constants import CHAR_SKINS_JSON
from characters.dataobj import Character, CharSkin
from translate.textmap import lang

import sys
import logging

logger = logging.getLogger(__name__)

skins = loadJson(CHAR_SKINS_JSON)

class SkinFields :
    def __init__(self) :
        skin_search = [
            x for x in skins
            if 'itemId' in x and x['itemId'] == 340001
        ]
        if len(skin_search) == 0 :
            logger.critical('Could not find the reference skin in the list of skins', stack_info=True)
            sys.exit(1)
        if len(skin_search) > 1 :
            logger.warning('Found several instances for the reference skin')
        skin: "dict[str,any]" = skin_search[0]
        values = list(skin.values())
        try :
            index_char = values.index(10000003)
            index_icon = values.index('UI_AvatarIcon_QinCostumeSea')
            index_rarity = values.index(4)
        except ValueError :
            logger.error('Could not automatically determine some fields for character skins', exc_info=sys.exc_info())
        keys = list(skin.keys())
        self.character = keys[index_char]
        self.icon      = keys[index_icon]
        self.rarity    = keys[index_rarity]
        logger.debug("Found key `%s` for character field in character skins", self.character)
        logger.debug("Found key `%s` for icon field in character skins", self.icon)
        logger.debug("Found key `%s` for rarity field in character skins", self.rarity)

FIELDS = SkinFields()


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
    data.icon = skin[FIELDS.icon]
    data.restricted = skin['hide'] if 'hide' in skin else False
    char_id = skin[FIELDS.character]
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
