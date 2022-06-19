
from unicodedata import name
from utils import loadJson
from constants import WEAPON_DATA_JSON, PropType
from translate.textmap import lang
from weapons.ascensions import readAscensions
from weapons.abilities import readAbilities

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
		if data is not None :
			res[data['hoyo_id']] = data

	readAscensions(res)
	
	# for weapon in res.values() :
	#	print(weapon['name'])
	# 	print(weapon)

	return res


# weapon['rank'] is always 10 (idk)
def __g_readWeaponBase(weapon: dict) -> dict :
	data = {
		'hoyo_id': weapon['id'],
		'promote_id': weapon['weaponPromoteId'],
		'gadget_id': weapon['gadgetId'],
		'story_id': weapon['storyId'] if 'storyId' in weapon else None,
		'skill_affix': weapon['skillAffix'],
		'name_hash': weapon['nameTextMapHash'],
		'desc_hash': weapon['descTextMapHash'],
		'rarity': weapon['rankLevel'],
		'type': WeaponType[weapon['weaponType']].value
	}

	data['name'] = lang[str(data['name_hash'])]
	data['desc'] = lang[str(data['desc_hash'])]
	# print(data['name'])
	# print(data['type'])

	if(data['name'] == '') :
		return None

	base_stats = {}
	curves = {}
	for prop in weapon['weaponProp'] :
		if 'propType' in prop and 'initValue' in prop and 'type' in prop :
			prop_type = PropType[prop['propType']].value
			base_val = prop['initValue']
			curve = prop['type']
			base_stats[prop_type] = base_val
			curves[prop_type] = curve
	data['base_stats'] = base_stats
	data['curves'] = curves

	# print(weapon['weaponBaseExp'])
	# if 'initialLockState' in weapon :
	# 	print(weapon['initialLockState'])
	# print('--------------')
	
	refinement_costs = weapon['awakenCosts']
	awaken_material = weapon['awakenMaterial'] if 'awakenMaterial' in weapon else None
	readAbilities(data, refinement_costs, awaken_material)

	return data