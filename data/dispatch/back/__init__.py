
from utils import OutputDir
from engine.core import DispatchEngine
from back.hardcoded  import dispatchHardcoded
from back.characters import dispatchCharacters
from back.gliders    import dispatchGliders

BACK_CONSTANTS_FILE = 'numeric_constants.json'


def dispatch() :
	engine = DispatchEngine(BACK_CONSTANTS_FILE, OutputDir.BACK)

	dispatchHardcoded(engine)

	dispatchCharacters(engine)

	dispatchGliders(engine)

	engine.close()


