
from constants import CHARACTERS_FOLDER, CHARACTERS_IGNORED
from engine.core import DispatchEngine, Dispatcher
from engine.dispatchers.merge import MergeDispatcher

FRONT_CHARACTERS_FILE = 'characters.json'


def dispatchCharacters(engine: DispatchEngine) :
	dispatcher = MergeDispatcher(
		CHARACTERS_FOLDER, 
		FRONT_CHARACTERS_FILE,
		__d_transformCharacter,
		CHARACTERS_IGNORED
	)
	engine.accept(dispatcher)


def __d_transformCharacter(_dispatcher: Dispatcher, character: "dict[str,any]") :
	del character['hoyo_id']
	del character['promote_id']
	del character['skill_depot_id']
	del character['fetter_id']
	del character['name_hash']
	del character['desc_hash']
	del character['icon']
	del character['body']
	del character['vision_hash']
	del character['astrolabe_hash']
	del character['allegiance_hash']
	# TODO ascensions
	# TODO talents
	# TODO passives
	# TODO constellations
	# TODO skins
	# TODO special_dish
	return character
