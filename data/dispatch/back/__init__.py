
from utils import OutputDir
from engine.core import DispatchEngine
from back.hardcoded  import dispatchHardcoded
from back.characters import dispatchCharacters
from back.weapons    import dispatchWeapons
from back.artifacts  import dispatchArtifacts
from back.gliders    import dispatchGliders

BACK_CONSTANTS_FILE = 'numeric_constants.json'


def dispatch() :
	engine = DispatchEngine(BACK_CONSTANTS_FILE, OutputDir.BACK)

	dispatchHardcoded(engine)

	dispatchCharacters(engine)

	dispatchWeapons(engine)

	dispatchArtifacts(engine)

	dispatchGliders(engine)

	engine.close()


