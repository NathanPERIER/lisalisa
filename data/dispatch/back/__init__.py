
from utils import OutputDir
from engine.core import DispatchEngine
from back.hardcoded  import dispatchHardcoded
from back.characters import dispatchCharacters

BACK_CONSTANTS_FILE = 'numeric_constants.json'


def dispatch() :
	engine = DispatchEngine(BACK_CONSTANTS_FILE, OutputDir.BACK)

	dispatchHardcoded(engine)

	dispatchCharacters(engine)

	engine.close()


