#!/usr/bin/python3

from utils import loadJson, saveJson, idFromName
from constants import CHAR_DATA_JSON, DEST_DIR
from translate.textmap import lang
from characters.info import readInfo
from characters.skins import readSkins
from characters.ascensions import readAscensions, PropType
from characters.curves import setCurves

import os
from enum import Enum

class BodyType(Enum) :
    BODY_LOLI = 0
    BODY_BOY  = 1
    BODY_GIRL = 2
    BODY_MALE = 3
    BODY_LADY = 4

class QualityType(Enum) :
    QUALITY_PURPLE = 4
    QUALITY_ORANGE = 5

class WeaponType(Enum) :
    WEAPON_SWORD_ONE_HAND = 'sword'
    WEAPON_CATALYST = 'catalyst'
    WEAPON_CLAYMORE = 'claymore'
    WEAPON_POLE = 'polearm'
    WEAPON_BOW = 'bow'


def __g_filterCharacters(chars: list) :
    return [
        char for char in chars
        if 'useType' in char and char['useType'] == 'AVATAR_FORMAL'
    ]

chars = __g_filterCharacters(loadJson(CHAR_DATA_JSON))


if __name__ == '__main__' :

    characters = {}

    for char in chars :
        data = {
            'hoyo_id': char['id'],
            'promote_id': char['avatarPromoteId'],
            'weapon': WeaponType[char['weaponType']].value,
            'dish': None # TODO
        }
        data['body'] = BodyType[char['bodyType']].name
        quality: str = char['qualityType']
        data['special'] = False
        if quality.endswith('_SP') :
            quality = quality[:-3]
            data['special'] = True
        data['rarity'] = QualityType[quality].value
        data['name_hash'] = char['nameTextMapHash']
        data['name'] = lang[str(data['name_hash'])]
        print(data['name'])
        data['desc_hash'] = char['descTextMapHash']
        data['desc'] = lang[str(data['desc_hash'])]
        # Same as `infoDescTextMapHash` it seems (?)
        data['skins'] = {
            'default': None,
            'alt': []
        }

        # initialWeapon -> we need weapons first

        # avatarIdentityType ?

        data['base_stats'] = {
            PropType.FIGHT_PROP_BASE_HP.value:       char['hpBase'],
            PropType.FIGHT_PROP_BASE_ATTACK.value:   char['attackBase'],
            PropType.FIGHT_PROP_BASE_DEFENSE.value:  char['defenseBase'],
            PropType.FIGHT_PROP_CRITICAL.value:      char['critical'],
            PropType.FIGHT_PROP_CRITICAL_HURT.value: char['criticalHurt']
        }
        data['curves'] = {
            PropType[x['type']].value: x['growCurve']
            for x in char['propGrowCurves']
        }

        characters[data['hoyo_id']] = data

    readInfo(characters)

    readSkins(characters)

    readAscensions(characters)
    
    setCurves(characters)

    for char in characters.values() :
        char_id = idFromName(char['name'])
        dest = os.path.join(DEST_DIR, f"characters/{char_id}.json")
        saveJson(char, dest)

