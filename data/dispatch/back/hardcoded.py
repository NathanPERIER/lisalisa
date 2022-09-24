
from constants import HC_ADV_RANK_FILE, HC_ASCENSION_FILE, HC_WORLD_LEVEL_FILE, HC_ART_RARITIES_FILE
from engine.core import DispatchEngine
from engine.dispatchers.filename import SameFilenameDispatcher


def dispatchHardcoded(engine: DispatchEngine) :
	engine.acceptAll([
		SameFilenameDispatcher(HC_ADV_RANK_FILE),
		SameFilenameDispatcher(HC_ASCENSION_FILE),
		SameFilenameDispatcher(HC_WORLD_LEVEL_FILE),
		SameFilenameDispatcher(HC_ART_RARITIES_FILE)
	])
