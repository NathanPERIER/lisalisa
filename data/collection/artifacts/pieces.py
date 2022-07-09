
from utils import loadJson, indexById
from constants import ARTIFACT_PIECES_JSON
from translate.textmap import lang

from enum import Enum

class EquipType(Enum) :
    EQUIP_BRACER   = 'flower_of_life'
    EQUIP_NECKLACE = 'plume_of_death'
    EQUIP_SHOES    = 'sands_of_eon'
    EQUIP_RING     = 'goblet_of_eonothem'
    EQUIP_DRESS    = 'circlet_of_logos'

pieces = indexById(loadJson(ARTIFACT_PIECES_JSON))


def readArtifactPiece(piece_id: dict) -> "dict[str,any]" :
	piece = pieces[piece_id]
	res = {
		'hoyo_id': piece['id'],
		'story_id': piece['storyId'] if 'storyId' in piece else None,
		'gadget_id': piece['gadgetId'],
		'prop_id': piece['appendPropDepotId'],
		'set_id': piece['setId'] if 'setId' in piece else None,
		'name_hash': piece['nameTextMapHash'],
		'desc_hash': piece['descTextMapHash'],
		'type': EquipType[piece['equipType']],
		'rarity': piece['rankLevel'],
		'max_level': piece['maxLevel'] - 1,
		 # Levels at which a prop is added (substat level)
		'add_prop_levels': [x-1 for x in piece['addPropLevels']],
		 # Exp given by using this artifact (at min level) to enhance another artifact
		'conv_exp': piece['baseConvExp']
	}
	res['name'] = lang(res['name_hash'])
	res['desc'] = lang(res['desc_hash'])
	return res