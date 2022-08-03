
from utils import loadJson
from constants import CHAR_INFO_JSON
from common.dataobj.character import Character
from translate.textmap import lang

import logging
from enum import Enum

logger = logging.getLogger(__name__)

class AssocType(Enum) :
    ASSOC_TYPE_MONDSTADT = 'mondstadt'
    ASSOC_TYPE_FATUI = 'snezhnaya'
    ASSOC_TYPE_MAINACTOR = 'outlander'
    ASSOC_TYPE_INAZUMA = 'inazuma'
    ASSOC_TYPE_LIYUE = 'liyue'
    ASSOC_TYPE_RANGER = 'ranger'

info = loadJson(CHAR_INFO_JSON)


def readInfo(characters: "dict[str,Character]") :
    ok = set()
    for inf in info :
        char_id = __g_readInfo(inf, characters)
        if char_id in ok :
            logger.warning('Overriding character info for %d', char_id)
        else :
            ok.add(char_id)
    # TODO check for characters that haven't been used

def __g_readInfo(inf: dict, characters: "dict[str,Character]") :
    char_id = inf['avatarId']
    data = characters[char_id]
    if 'infoBirthDay' in inf and 'infoBirthMonth' in inf :
        data.birthday = [
            inf['infoBirthDay'],
            inf['infoBirthMonth']
        ]
    data.vision_hash = [
        inf['avatarVisionBeforTextMapHash'],
        inf['avatarVisionAfterTextMapHash']
    ]
    data.vision = lang(data.vision_hash[0]).lower()
    data.astrolabe_hash = [
        inf['avatarConstellationBeforTextMapHash'],
        inf['avatarConstellationAfterTextMapHash']
    ]
    if data.astrolabe_hash[1] in lang :
        data.astrolabe = lang(data.astrolabe_hash[1])
    else :
        data.astrolabe = lang(data.astrolabe_hash[0])
    data.allegiance_hash = inf['avatarNativeTextMapHash']
    data.allegiance = lang(data.allegiance_hash)
    # Translation of `avatarDetailTextMapHash` should be the same as character desc
    # TODO test + warning
    data.region = AssocType[inf['avatarAssocType']]
    data.fetter_id = inf['fetterId']
    return char_id