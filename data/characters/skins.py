from translate.textmap import lang
from constants import CHAR_SKINS_JSON
from utils import loadJson

CHARACTER_FIELD_NAME = 'FMAJGGBGKKN'

skins = loadJson(CHAR_SKINS_JSON)


def readSkins(characters: dict) :
    for skin in skins :
        __g_readSkin(skin, characters)
    for char in characters.values() :
        if char['skins']['default'] is None :
            # TODO logging
            print(f"Warning : no default skin for {char['hoyo_id']}")

def __g_readSkin(skin, characters) :
    data = {
        'hoyo_id': skin['itemId'] if 'itemId' in skin else None,
        'name_hash': skin['nameTextMapHash'],
        'desc_hash': skin['descTextMapHash'],
        'restricted': skin['hide'] if 'hide' in skin else False
    }
    data['name'] = lang[str(data['name_hash'])]
    data['desc'] = lang[str(data['desc_hash'])]
    char_id = skin[CHARACTER_FIELD_NAME]
    if 'isDefault' in skin and skin['isDefault'] :
        # TODO warning if there is already a default skin
        characters[char_id]['skins']['default'] = data
    else :
        characters[char_id]['skins']['alt'].append(data)
