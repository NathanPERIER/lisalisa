
from utils import OutputDir
from engine import DispatchEngine
from back.hardcoded import dispatchHardcoded

BACK_CONSTANTS_FILE = 'numeric_constants.json'


def dispatch() :
	engine = DispatchEngine(BACK_CONSTANTS_FILE, OutputDir.BACK)

	dispatchHardcoded(engine)

	engine.close()


