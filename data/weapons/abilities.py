
from common.dataobj.weapon import Weapon
from utils import loadJson
from constants import WEAPON_ABILITY_JSON
from translate.textmap import lang

import logging

logger = logging.getLogger(__name__)

abilities = loadJson(WEAPON_ABILITY_JSON)


def readAbilities(weapon: Weapon, refinement_costs: "list[int]", awaken_material: int) :
	if weapon.skill_affix[0] == 0 :
		return
	if weapon.skill_affix[1] != 0 :
		logger.info("Second slot of skill affix is %d for %s (%d), usually is 0", 
						weapon.skill_affix[1], weapon.name, weapon.hoyo_id)
	__g_readWeaponAbilities(weapon, weapon.skill_affix[0], refinement_costs, awaken_material)


def __g_readWeaponAbilities(weapon: Weapon, affix: int, costs: "list[int]", awaken_material: int) :
	res = [
		__g_readAbilityEntry(entry)
		for entry in abilities
		if entry['id'] == affix
	]
	res.sort(key = lambda a : a['level'])
	# Check that we have at least an ability, else is sus
	if len(res) == 0 :
		logger.warning("Got no abilities for %s (%d), with affix %d",
						weapon.name, weapon.hoyo_id, affix)
		return
	# First ability is given by default, so we set the cost to zero
	padded_costs = [0, *costs]
	# Check that we have the right amount of costs
	if len(res) != len(padded_costs) :
		logger.warning("Got %d abilities for %s (%d), but had %d costs", 
						len(res), weapon.name, weapon.hoyo_id, len(costs))
		if len(res) > len(padded_costs) :
			padded_costs.extend( [0] * (len(res) - len(padded_costs)) )
	# Integrate the mora cost in all 
	# The name should be the same for all levels so we remove that
	# The level is also useless since it is just index + 1
	name_hash = res[0]['name_hash']
	name = res[0]['name']
	for i in range(len(res)) :
		ability = res[i]
		ability['cost'] = padded_costs[i]
		del ability['level']
		del ability['name_hash']
		del ability['name']
	weapon.abilities = {
		'name_hash': name_hash,
		'name': name,
		'special_material': awaken_material,
		'values': res
	}


def __g_readAbilityEntry(entry: dict) -> dict :
	ability = {
		'affix_id': entry['affixId'],
		'level': entry['level'] if 'level' in entry else 0,
		'name_hash': entry['nameTextMapHash'],
		'desc_hash': entry['descTextMapHash']
	}
	ability['name'] = lang[str(ability['name_hash'])]
	ability['desc'] = lang[str(ability['desc_hash'])]
	return ability
