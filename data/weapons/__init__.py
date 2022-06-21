
from utils import loadJson, idFromName
from constants import WEAPON_DATA_JSON, PropType
from translate.textmap import lang
from translate.mhy import mhy_weapons, mhy_items
from common.dataobj.weapon import Weapon
from weapons.ascensions import readAscensions
from weapons.abilities import readAbilities
from weapons.curves import curves

import logging
from enum import Enum

logger = logging.getLogger(__name__)

weapons = loadJson(WEAPON_DATA_JSON)

class WeaponType(Enum) :
    WEAPON_SWORD_ONE_HAND = 'sword'
    WEAPON_CATALYST = 'catalyst'
    WEAPON_CLAYMORE = 'claymore'
    WEAPON_POLE = 'polearm'
    WEAPON_BOW = 'bow'


def readWeapons() -> "dict[str,Weapon]" :
	res = {}
	for weapon in weapons :
		data = __g_readWeaponBase(weapon)
		if data is not None :
			identifier = idFromName(data.name)
			res[identifier] = data
			mhy_weapons[data.hoyo_id] = identifier

	readAscensions(res)

	return res


def getWeaponCurves() -> dict :
	return curves


# weapon['rank'] is always 10 (idk)
def __g_readWeaponBase(weapon: dict) -> Weapon :
	data = Weapon()

	data.hoyo_id     = weapon['id']
	data.promote_id  = weapon['weaponPromoteId']
	data.gadget_id   = weapon['gadgetId']
	data.story_id    = weapon['storyId'] if 'storyId' in weapon else None,
	data.skill_affix = weapon['skillAffix']

	data.type = WeaponType[weapon['weaponType']]
	data.name_hash = weapon['nameTextMapHash']
	data.desc_hash = weapon['descTextMapHash']
	data.name = lang[str(data.name_hash)]
	data.desc = lang[str(data.desc_hash)]
	data.rarity = weapon['rankLevel']

	if data.name == '' :
		return None
	
	if data.rarity > 1 and data.promote_id == 11101 :
		logger.info("< %s > (ignored)", data.name)
		return None
	
	logger.info("< %s >", data.name)

	for prop in weapon['weaponProp'] :
		if 'propType' in prop and 'initValue' in prop and 'type' in prop :
			prop_type = PropType[prop['propType']].value
			base_val = prop['initValue']
			curve = prop['type']
			data.base_stats[prop_type] = base_val
			data.curves[prop_type] = curve

	# print(weapon['weaponBaseExp'])
	# if 'initialLockState' in weapon :
	# 	print(weapon['initialLockState'])
	# print('--------------')
	
	refinement_costs = weapon['awakenCosts']
	awaken_material = weapon['awakenMaterial'] if 'awakenMaterial' in weapon else None
	if awaken_material is not None :
		awaken_material = mhy_items[awaken_material]
	readAbilities(data, refinement_costs, awaken_material)

	return data