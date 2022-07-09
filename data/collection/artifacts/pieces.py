
from utils import loadJson, indexById
from constants import ARTIFACT_PIECES_JSON
from translate.textmap import lang
from common.dataobj.artifact import ArtifactPiece

from enum import Enum

class EquipType(Enum) :
    EQUIP_BRACER   = 'flower_of_life'
    EQUIP_NECKLACE = 'plume_of_death'
    EQUIP_SHOES    = 'sands_of_eon'
    EQUIP_RING     = 'goblet_of_eonothem'
    EQUIP_DRESS    = 'circlet_of_logos'

pieces = indexById(loadJson(ARTIFACT_PIECES_JSON))


def readArtifactPiece(piece_id: dict) -> ArtifactPiece :
	piece = pieces[piece_id]
	res = ArtifactPiece()
	res.hoyo_id = piece['id']
	res.story_id = piece['storyId'] if 'storyId' in piece else None
	res.gadget_id = piece['gadgetId']
	res.prop_id = piece['appendPropDepotId']
	res.set_id = piece['setId'] if 'setId' in piece else None
	res.name_hash = piece['nameTextMapHash']
	res.desc_hash = piece['descTextMapHash']
	res.type = EquipType[piece['equipType']]
	res.rarity = piece['rankLevel']
	res.max_level = piece['maxLevel'] - 1
	# Levels at which a prop is added (substat level)
	res.add_prop_levels = [x-1 for x in piece['addPropLevels']]
	# Exp given by using this artifact (at min level) to enhance another artifact
	res.conv_exp = piece['baseConvExp']
	res.name = lang(res.name_hash)
	res.desc = lang(res.desc_hash)
	return res