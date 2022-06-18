
from utils import loadJson, saveJson
from constants import CHAR_DATA_JSON, PropType
from weapons import WeaponType
from translate.textmap import lang
from characters.info import readInfo
from characters.skins import readSkins
from characters.ascensions import readAscensions
from characters.skills import readSkillsConstellations
from characters.curves import setCurves

import logging
from enum import Enum

logger = logging.getLogger(__name__)

class BodyType(Enum) :
    BODY_LOLI = 0
    BODY_BOY  = 1
    BODY_GIRL = 2
    BODY_MALE = 3
    BODY_LADY = 4

class QualityType(Enum) :
    QUALITY_PURPLE = 4
    QUALITY_ORANGE = 5


def __g_filterCharacters(chars: list) -> list :
	return [
		c for c in chars
		if 'useType' in c and c['useType'] == 'AVATAR_FORMAL'
	]

chars = __g_filterCharacters(loadJson(CHAR_DATA_JSON))


def readCharacters() :
	characters = {}

	for char in chars :
		data = __g_readCharacterBase(char)
		characters[char['hoyo_id']] = char

	for char_id, char in [x for x in characters.items()] :
		if char['name'] == 'Traveler' :
			pass # TODO
		else :
			readSkillsConstellations(char)

	readInfo(characters)

	readSkins(characters)

	readAscensions(characters)

	setCurves(characters)

	for char_id, char in characters.items() :
		saveJson(char, f"temp/{char_id}.json")


# avatarIdentityType ?
def __g_readCharacterBase(char: dict) -> dict :
	print(char)
	data = {
		'hoyo_id': char['id'],
		'promote_id': char['avatarPromoteId'],
		'skill_depot_id': char['skillDepotId'],
		'weapon': WeaponType[char['weaponType']].value
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
	logger.info(data['name'])
	data['desc_hash'] = char['descTextMapHash']
	data['desc'] = lang[str(data['desc_hash'])]
	# Same as `infoDescTextMapHash` it seems (?)
	data['skins'] = {
		'default': None,
		'alt': []
	}

	# 'avatarIdentityType' not in data
	if data['name'] == 'Traveler' :
		data['skill_depot_id'] = char['candSkillDepotIds']

	# initialWeapon -> we need weapons first

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

	return data
