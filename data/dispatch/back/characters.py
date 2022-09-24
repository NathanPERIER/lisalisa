
from constants import CHARACTERS_FOLDER, CHARACTERS_IGNORED
from engine.core import DispatchEngine, Dispatcher
from engine.dispatchers.merge import MergeDispatcher

import logging

logger = logging.getLogger(__name__)

BACK_CHARACTERS_FILE = 'characters.json'


def dispatchCharacters(engine: DispatchEngine) :
	dispatcher = MergeDispatcher(
		CHARACTERS_FOLDER, 
		BACK_CHARACTERS_FILE,
		__d_transformCharacter,
		CHARACTERS_IGNORED
	)
	engine.accept(dispatcher)


def __d_transformCharacter(_dispatcher: Dispatcher, character: "dict[str,any]") :
	elemental_skill = character['talents']['elemental_skill']['name']
	elemental_burst = character['talents']['elemental_burst']['name']
	skill_increase_text = f"Increases the Level of {elemental_skill} by 3."
	burst_increase_text = f"Increases the Level of {elemental_burst} by 3."
	c3: str = character['constellations'][2]['desc']
	c5: str = character['constellations'][4]['desc']
	increase_skill = 10
	increase_burst = 10
	if c3.startswith(skill_increase_text) :
		increase_skill = 3
		increase_burst = 5
		if not c5.startswith(burst_increase_text) :
			logger.warning("Found skill increase at C3 but no burst increase at C5 for %s", character['name'])
	elif c5.startswith(skill_increase_text) :
		increase_skill = 5
		increase_burst = 3
		if not c3.startswith(burst_increase_text) :
			logger.warning("Found skill increase at C5 but no burst increase at C3 for %s", character['name'])
	return {
		'weapon': character['weapon'],
		'defaultWeapon': character['default_weapon'],
		'alternateSkins': __d_transformSkins(character['skins']),
		'increaseSkill': increase_skill,
		'increaseBurst': increase_burst
	}

def __d_transformSkins(skins: "dict[str,any]") -> "dict[str,any]" :
	return [
		skin['name'] for skin in skins['alt']
	]
