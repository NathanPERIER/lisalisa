from translate.textmap import lang
from constants import CHAR_INFO_JSON
from utils import loadJson

from enum import Enum

class AssocType(Enum) :
    ASSOC_TYPE_MONDSTADT = 'mondstadt'
    ASSOC_TYPE_FATUI = 'snezhnaya'
    ASSOC_TYPE_MAINACTOR = 'outlander'
    ASSOC_TYPE_INAZUMA = 'inazuma'
    ASSOC_TYPE_LIYUE = 'liyue'
    ASSOC_TYPE_RANGER = 'ranger'

info = loadJson(CHAR_INFO_JSON)


def readInfo(characters) :
    ok = set()
    for inf in info :
        char_id = __g_readInfo(inf, characters)
        if char_id in ok :
            print(f"Warning : override {char_id}")
        else :
            ok.add(char_id)
    # TODO check for characters that haven't been used

def __g_readInfo(inf, characters) :
    char_id = inf['avatarId']
    data = characters[char_id]
    if 'infoBirthDay' in inf and 'infoBirthMonth' in inf :
        data['birthday'] = [
            inf['infoBirthDay'],
            inf['infoBirthMonth']
        ]
    else :
        data['birthday'] = None
    data['vision_hash'] = [
        inf['avatarVisionBeforTextMapHash'],
        inf['avatarVisionAfterTextMapHash']
    ]
    data['vision'] = lang[str(data['vision_hash'][0])].lower()
    data['astrolabe_hash'] = [
        inf['avatarConstellationBeforTextMapHash'],
        inf['avatarConstellationAfterTextMapHash']
    ]
    data['astrolabe'] = lang[str(data['astrolabe_hash'][1])]
    if data['astrolabe'] == "" :
        data['astrolabe'] = lang[str(data['astrolabe_hash'][0])]
    data['allegiance_hash'] = inf['avatarNativeTextMapHash']
    data['allegiance'] = lang[str(data['allegiance_hash'])]
    # Translation of `avatarDetailTextMapHash` should be the same as character desc
    # TODO test + warning
    data['region'] = AssocType[inf['avatarAssocType']].value
    data['fetter_id'] = inf['fetterId']
    return char_id