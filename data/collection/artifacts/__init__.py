
from utils import fieldsEqual, idFromName, loadJson, indexById, groupByField
from constants import ARTIFACT_CODEX_JSON, ARTIFACT_DISPLAY_JSON
from translate.textmap import lang
from translate.mhy import mhy_art_sets
from artifacts.pieces import readArtifactPiece as __g_readArtifactPiece
from artifacts.sets   import readArtifactSet   as __g_readArtifactSet
from artifacts.curves import curves, getSetAffixes as __g_getSetAffixes
from artifacts.dataobj import ArtifactSet, ArtifactRaritySet
from artifacts.images import registerArtifactImages

import logging

logger = logging.getLogger(__name__)


def __g_formatDisplay(display: "list[dict[str,any]]") -> "dict[int,list[dict[int,dict[str,any]]]]" :
    res = {}
    filtered = [x for x in display if 'param' in x]
    for param, values in groupByField(filtered, 'param').items() :
        res[param] = indexById(values, 'rankLevel')
    return res

codex = loadJson(ARTIFACT_CODEX_JSON)
display = __g_formatDisplay(loadJson(ARTIFACT_DISPLAY_JSON))

PIECE_FIELDS = ["cupId", "leatherId", "capId", "flowerId", "sandId"]


def getArtifactCurves() -> list :
    return curves


def readArtifactSets() -> "dict[str,ArtifactSet]" :
    res = {}
    grouped = groupByField(codex, 'suitId')
    for set_id, data in grouped.items() :
        art_set = __g_readArtifactSet(set_id)
        for rarity_set in data :
            __g_readRaritySet(art_set, rarity_set)
        art_set.pieces.sort(key = lambda x: x.rarity)
        if not fieldsEqual(art_set.pieces, 'name') :
            logger.warning("Artifact set %d has different names at different rarities", art_set.hoyo_id)
        art_set.name = art_set.pieces[0].name
        identifier = idFromName(art_set.name)
        res[identifier] = art_set
        registerArtifactImages(identifier, art_set)
        mhy_art_sets[art_set.hoyo_id] = identifier
    return res
        

def __g_readRaritySet(art_set: ArtifactSet, r_set: "dict[str,any]") :
    res = ArtifactRaritySet()
    res.rarity = r_set['level']
    for field in PIECE_FIELDS :
        if field in r_set :
            piece_id = r_set[field]
            res.pieces.append(__g_readArtifactPiece(piece_id))
    # Set name
    disp = display[art_set.hoyo_id][res.rarity]
    res.display_id = disp['id']
    res.name_hash = disp['nameTextMapHash']
    res.name = lang(res.name_hash)
    # Affixes
    if not fieldsEqual(res.pieces, 'prop_id') :
        logger.warning("Pieces of set %d at rarity %d have different prop IDs", art_set.hoyo_id, res.rarity)
    prop_id = res.pieces[0]['prop_id']
    res.substats = __g_getSetAffixes(prop_id)
    art_set.pieces.append(res)
