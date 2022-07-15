
from constants import HC_ADV_RANK_FILE, HC_ASCENSION_FILE, HC_WORLD_LEVEL_FILE
from engine import DispatchEngine, Dispatcher

BACK_ADV_RANK_FILE    = 'adventure_rank.json'
BACK_ASCENSION_FILE   = 'ascension.json'
BACK_WORLD_LEVEL_FILE = 'world_level.json'


def dispatchHardcoded(engine: DispatchEngine) :
	engine.acceptAll([
		Dispatcher(HC_ADV_RANK_FILE,    BACK_ADV_RANK_FILE),
		Dispatcher(HC_ASCENSION_FILE,   BACK_ASCENSION_FILE),
		Dispatcher(HC_WORLD_LEVEL_FILE, BACK_WORLD_LEVEL_FILE)
	])
