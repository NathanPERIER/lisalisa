
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
	return {
		'weapon': character['weapon'],
		'defaultWeapon': character['default_weapon'],
		'alternateSkins': __d_transformSkins(character['skins'])
	}

def __d_transformSkins(skins: "dict[str,any]") -> "dict[str,any]" :
	return [
		skin['name'] for skin in skins['alt']
	]
