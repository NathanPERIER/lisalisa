
from constants import ITEMS_GLIDERS_FILE
from engine.core import Dispatcher, DispatchEngine
from engine.dispatchers.filename import SameFilenameDispatcher


def dispatchGliders(engine: DispatchEngine) :
	engine.accept(
		SameFilenameDispatcher(ITEMS_GLIDERS_FILE, __g_glidersTransform)
	)

def __g_glidersTransform(_dispatcher: Dispatcher, gliders: "dict[str,any]") -> "list[str]" :
	return list(gliders.keys())
