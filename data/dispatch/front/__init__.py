
from utils import OutputDir
from engine.core import DispatchEngine
from front.characters import dispatchCharacters

FRONT_CONSTANTS_FILE = 'numeric_constants.json'


def dispatch() :
	engine = DispatchEngine(FRONT_CONSTANTS_FILE, OutputDir.FRONT)

	dispatchCharacters(engine)

	engine.close()
