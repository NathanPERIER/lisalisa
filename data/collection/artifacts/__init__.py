
from utils import fieldsEqual, idFromName, loadJson, indexById, groupByField
from constants import ARTIFACT_DATA_JSON, ARTIFACT_SETS_JSON, ARTIFACT_EQUIP_JSON
from translate.textmap import lang
from artifacts.curves import curves

import logging
from enum import Enum

logger = logging.getLogger(__name__)

class EquipType(Enum) :
    EQUIP_BRACER   = 'flower_of_life'
    EQUIP_NECKLACE = 'plume_of_death'
    EQUIP_SHOES    = 'sands_of_eon'
    EQUIP_RING     = 'goblet_of_eonothem'
    EQUIP_DRESS    = 'circlet_of_logos'

def __g_filterSets(sets: "list[dict[str,any]]") -> "list[dict[str,any]]" :
    return [
        art_set for art_set in sets
        if 'DisableFilter' not in art_set or art_set['DisableFilter'] != 1
    ]

artifacts = loadJson(ARTIFACT_DATA_JSON)
sets = __g_filterSets(loadJson(ARTIFACT_SETS_JSON))
equips = groupByField(loadJson(ARTIFACT_EQUIP_JSON), 'id')


def getCurves() -> list :
    return curves


def readArtifactSets() :
    res = []
    pieces = __g_readAllPieces(artifacts)
    for art_set in sets :
        data = __g_readArtifactSet(art_set)
        set_pieces = pieces[data['hoyo_id']]
        data['pieces'] = __g_groupArtifactPieces(set_pieces)
        res.append(data)
    return res


def __g_groupArtifactPieces(pieces: "list[dict[str,any]]") :
    res = {}
    for type, t_pieces in groupByField(pieces, 'type').items() :
        grouped = groupByField(t_pieces, 'rarity')
        grouped_items = list(grouped.items())
        grouped_items.sort(key = lambda x: x[0])
        t_res = [x[1][0] for x in grouped_items]
        for rarity, g_pieces in grouped.items() :
            if not fieldsEqual(g_pieces, 'name') :
                logger.warning("Pieces of set %d, of rarity %d and of type %s have different names", g_pieces[0]['set_id'], rarity, type.value)
                logger.warning([x['name'] for x in g_pieces])
        res[type.value] = t_res
    return res
        
 

def __g_readAllPieces(artifacts: "list[dict]") -> "dict[str,list[dict[str,any]]]" :
    res = [
        __g_readArtifactPiece(piece)
        for piece in artifacts
    ]
    return groupByField(res, 'set_id')


# TODO : set name ?
def __g_readArtifactSet(art_set: dict) -> "dict[str,any]" :
    res = {
        'hoyo_id': art_set['setId'],
        'equip_id': art_set['EquipAffixId'],
        'piece_ids': art_set['containsList'] # Not actually pieces, most likely a group of them
    }
    need_nums = art_set['setNeedNum']
    equip_data = equips[res['equip_id']]
    if len(need_nums) != len(equip_data) :
        logger.warning("Found %d equips for artifact set %d, expected %d", 
                            len(equip_data), res['hoyo_id'], len(need_nums))
    equip_data.sort(key = lambda x: x['level'] if 'level' in x else 0)
    res['bonuses'] = [
        __g_readEquip(equip, need_num)
        for need_num, equip in zip(need_nums, equip_data)
    ]
    return res


def __g_readEquip(equip: dict, need_num: int) -> "dict[str,any]" :
    res = {
        'hoyo_id': equip['affixId'],
        'name_hash': equip['nameTextMapHash'],
        'desc_hash': equip['descTextMapHash'],
        'nb_req': need_num
    }
    res['name'] = lang(res['name_hash'])
    res['desc'] = lang(res['desc_hash'])
    return res


def __g_readArtifactPiece(piece: dict) -> "dict[str,any]" :
    res = {
        'hoyo_id': piece['id'],
        'story_id': piece['storyId'] if 'storyId' in piece else None,
        'gadget_id': piece['gadgetId'],
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
