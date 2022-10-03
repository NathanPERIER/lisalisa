
from constants import WEAPONS_FOLDER
from engine.core import DispatchEngine, Dispatcher
from engine.dispatchers.merge import MergeDispatcher

import logging

logger = logging.getLogger(__name__)

BACK_WEAPONS_FILE = 'weapons.json'


def dispatchWeapons(engine: DispatchEngine) :
	dispatcher = MergeDispatcher(
		WEAPONS_FOLDER, 
		BACK_WEAPONS_FILE,
		__d_transformWeapon
	)
	engine.accept(dispatcher)


def __d_transformWeapon(_dispatcher: Dispatcher, weapon: "dict[str,any]") :
	return {
		'type': weapon['type'],
		'rarity': weapon['rarity'],
		'ascensions': len(weapon['ascensions']['costs']),
		'refinement': 1 if weapon['abilities'] is None else len(weapon['abilities']['values'])
	}
