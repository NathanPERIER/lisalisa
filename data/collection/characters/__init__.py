
from utils import idFromName, loadJson
from constants import CHAR_DATA_JSON, PropType
from weapons import WeaponType
from translate.textmap import lang
from translate.mhy import mhy_chars, mhy_weapons
from common.dataobj.character import Character
from characters.info import readInfo
from characters.skins import readSkins
from characters.ascensions import readAscensions
from characters.skills import readSkillsConstellations
from characters.travelers import readTravelerSkills
from characters.curves import curves
from items.recipes import readSpecialDish

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


def readCharacters() -> "dict[str,Character]" :
	characters: "dict[str,Character]" = {}

	for char in chars :
		data = __g_readCharacterBase(char)
		characters[data.hoyo_id] = data

	readInfo(characters)

	readSkins(characters)

	readAscensions(characters)

	res = {}
	for char in characters.values() :
		if char.name == 'Traveler' :
			res.update(readTravelerSkills(char))
		else :
			readSkillsConstellations(char)
			identifier = idFromName(char.name)
			res[identifier] = char
			mhy_chars[char.hoyo_id] = identifier
		
	return res


def getCharacterCurves() -> "dict[str,list[float]]" :
	return curves


def __g_readCharacterBase(char: dict) -> Character :
	data = Character()
	data.hoyo_id        = char['id']
	data.promote_id     = char['avatarPromoteId']
	data.skill_depot_id = char['skillDepotId']

	data.weapon = WeaponType[char['weaponType']]
	data.body = BodyType[char['bodyType']].name

	quality: str = char['qualityType']
	if quality.endswith('_SP') :
		quality = quality[:-3]
		data.special = True
	data.rarity = QualityType[quality]

	data.name_hash = char['nameTextMapHash']
	data.desc_hash = char['descTextMapHash']
	data.name = lang[str(data.name_hash)]
	data.desc = lang[str(data.desc_hash)]
	# Same as `infoDescTextMapHash` it seems (?)
	logger.info(data.name)

	# <=> 'avatarIdentityType' not in data
	if data.name == 'Traveler' :
		data.skill_depot_id = char['candSkillDepotIds']

	data.default_weapon = mhy_weapons[char['initialWeapon']]

	data.base_stats = {
		PropType.FIGHT_PROP_BASE_HP.value:       char['hpBase'],
		PropType.FIGHT_PROP_BASE_ATTACK.value:   char['attackBase'],
		PropType.FIGHT_PROP_BASE_DEFENSE.value:  char['defenseBase'],
		PropType.FIGHT_PROP_CRITICAL.value:      char['critical'],
		PropType.FIGHT_PROP_CRITICAL_HURT.value: char['criticalHurt']
	}
	data.curves = {
		PropType[x['type']].value: x['growCurve']
		for x in char['propGrowCurves']
	}

	data.special_dish = readSpecialDish(data.hoyo_id)

	return data
