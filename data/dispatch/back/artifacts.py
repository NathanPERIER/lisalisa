
from constants import ARTIFACT_FILE
from engine.core import DispatchEngine, Dispatcher

import logging

logger = logging.getLogger(__name__)

BACK_ARTIFACTS_FILE = 'artifacts.json'


def dispatchArtifacts(engine: DispatchEngine) :
	dispatcher = Dispatcher(
		ARTIFACT_FILE, 
		BACK_ARTIFACTS_FILE,
		__d_transformArtifacts
	)
	engine.accept(dispatcher)


def __d_transformArtifacts(_dispatcher: Dispatcher, artifacts: "dict[str,any]") :
	return {
		set_id: __d_processArtifactSet(set_id, art_set)
		for set_id, art_set in artifacts.items()
	}

def __d_processArtifactSet(set_id: str, art_set: "dict[str,any]") -> "dict[str,any]" :
	rarities = [x['rarity'] for x in art_set['pieces']]
	search_pieces = [
		list(set(y['type'].split('_')[0] for y in x['pieces']))
		for x in art_set['pieces']
	]
	pieces = search_pieces[0]
	for other_pieces in search_pieces[1:] :
		if other_pieces != pieces :
			logger.warning("Inconsistent pieces for different rarities %s", set_id)
	return {
		'rarities': rarities,
		'pieces': pieces
	}
