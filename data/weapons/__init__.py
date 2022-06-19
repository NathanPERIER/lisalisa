
from utils import loadJson
from constants import WEAPON_DATA_JSON, PropType
from translate.textmap import lang
from weapons.ascensions import readAscensions

from enum import Enum

weapons = loadJson(WEAPON_DATA_JSON)

class WeaponType(Enum) :
    WEAPON_SWORD_ONE_HAND = 'sword'
    WEAPON_CATALYST = 'catalyst'
    WEAPON_CLAYMORE = 'claymore'
    WEAPON_POLE = 'polearm'
    WEAPON_BOW = 'bow'


def readWeapons() :
	res = {}
	for weapon in weapons :
		data = __g_readWeaponBase(weapon)
		res[data['hoyo_id']] = data

	readAscensions(res)

	return res


def __g_readWeaponBase(weapon: dict) -> dict :
	data = {
		'hoyo_id': weapon['id'],
		'promote_id': weapon['weaponPromoteId'],
		'gadget_id': weapon['gadgetId'],
		'name_hash': weapon['nameTextMapHash'],
		'desc_hash': weapon['descTextMapHash'],
		'rarity': weapon['rankLevel'],
		'type': WeaponType[weapon['weaponType']].value
	}

	data['name'] = lang[str(data['name_hash'])]
	data['desc'] = lang[str(data['desc_hash'])]
	print(data['name'])
	print(data['type'])

	base_stats = {}
	curves = {}
	for prop in weapon['weaponProp'] :
		print(prop)
		if 'propType' in prop and 'initValue' in prop and 'type' in prop :
			prop_type = PropType[prop['propType']].value
			base_val = prop['initValue']
			curve = prop['type']
			base_stats[prop_type] = base_val
			curves[prop_type] = curve
	data['base_stats'] = base_stats
	data['curves'] = curves

	refinement_costs = weapon['awakenCosts']
	skill_affix = weapon['skillAffix']
	# print(weapon['weaponBaseExp'])
	# if 'initialLockState' in weapon :
	# 	print(weapon['initialLockState'])
	# weapon['rank'] is always 10 (idk)
	print('storyId' in weapon)
	print('--------------')

	return data