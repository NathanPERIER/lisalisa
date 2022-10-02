
from utils import OutputDir
from engine.core import DispatchEngine
from front.characters import dispatchCharacters
from front.hardcoded  import dispatchHardcoded

FRONT_CONSTANTS_FILE = 'numeric_constants.json'


def dispatch() :
	engine = DispatchEngine(FRONT_CONSTANTS_FILE, OutputDir.FRONT)

	dispatchCharacters(engine)

	dispatchHardcoded(engine)

	engine.close()
