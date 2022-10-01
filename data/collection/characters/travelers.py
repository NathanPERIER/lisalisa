
from utils import idFromName
from characters.skills import skill_depot, readSkillsConstellations, readSkill as __g_readSkill
from characters.dataobj import Character

import re
import logging
from enum import Enum

logger = logging.getLogger(__name__)

char_vision_reg = re.compile(r'Avatar_Player_AbilityGroup_(Girl|Boy)_(Common|Wind|Rock|Electric|Grass|Fire|Water|Ice)')

class Visions(Enum) :
	Common   = None
	Wind     = 'anemo'
	Rock     = 'geo'
	Electric = 'electro'
	Grass    = 'dendro'
	Fire     = 'pyro'
	Water    = 'hydro'
	Ice      = 'cryo'


# The traveler has 7 skill entries, so we need to go through them and keep only the ones that actually exist
def readTravelerSkills(char: Character) -> "dict[str,Character]" :
	logger.debug("Parsing traveler talents for %s (%s)", char.hoyo_id, char.name)
	res = {}
	for depot_id in char.skill_depot_id : 
		sp_char = __g_readTravelerSkillEntry(char, depot_id)
		if sp_char is not None : 
			res[sp_char[0]] = sp_char[1]
	return res


def __g_readTravelerSkillEntry(char: Character, depot_id: int) -> "tuple[str,Character]" :
	depot_search = [x for x in skill_depot if x['id'] == depot_id]
	if len(depot_search) != 1 :
		logger.error('No skills found in skill depot with for %s (%d) with id %d', 
						char.name, char.hoyo_id, depot_id)
		return None
	depot = depot_search[0]
	# If the version of the traveler has not been implemented yet, we skip this entry
	ability_group = depot['skillDepotAbilityGroup']
	if ability_group == '' :
		return None
	# Get the gender and the vision for this traveler
	m = char_vision_reg.match(ability_group)
	if m is None :
		logger.error('Bad ability group name %d for %s (%d) with id %d', 
						ability_group, char.name, char.hoyo_id, depot_id)
		return None
	gender = m.group(1)
	vision = Visions[m.group(2)]
	# Duplicate the object and update the values
	specialised_char = char.clone()
	specialised_char.skill_depot_id = depot_id
	specialised_char.vision = vision.value
	specialised_char.vision_hash = None
	if vision.value is not None :
		specialised_char.name = f"{vision.value.capitalize()} {char.name}"
		specialised_char.name_hash = None
		identifier = idFromName(f"{char.name}_{gender}_{vision.value}")
	else :
		identifier = idFromName(f"{char.name}_{gender}_common")
	# Read the skills, depending on wether it is the common traveler or not
	if 'energySkill' in depot and depot['skills'][1] != 0 and depot['talents'] != [0, 0, 0, 0, 0, 0] :
		readSkillsConstellations(specialised_char)
	else :
		__g_readCommonTravelerSkillEntry(specialised_char, depot)
	return identifier, specialised_char


# Reads the skills for the common traveler (only has default attack)
def __g_readCommonTravelerSkillEntry(char: Character, depot: dict) :
	char.talents.normal_attack    = __g_readSkill(depot['skills'][0])
	char.talents.elemental_skill  = None        # No elemental skill
	char.talents.elemental_burst  = None        # No elemental burst
	char.talents.alternate_sprint = None
	# No passives, no constellations
