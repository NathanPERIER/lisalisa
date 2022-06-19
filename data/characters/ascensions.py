
from utils import loadJson
from constants import CHAR_ASCENSIONS_JSON, ITEM_MORA_ID, PropType
from common.ascensions import formatAscensions as __g_formatAscensions
from common.ascensions import readAscension    as __g_readAscension

import logging

logger = logging.getLogger(__name__)

ascensions = loadJson(CHAR_ASCENSIONS_JSON)


PROMOTE_ID_FIELD = 'avatarPromoteId'
MORA_COST_FIELD  = 'scoinCost'


def readAscensions(characters: dict) :
    data = {}
    for asc in ascensions :
        __g_readAscension(asc, data, PROMOTE_ID_FIELD, MORA_COST_FIELD)
    for char in characters.values() :
        promote_id = char['promote_id']
        if promote_id not in data :
            logger.warning('Ascensions not found for %s (%d)', char['name'], char['hoyo_id'])
        else :
            char['ascensions'] = __g_formatAscensions(data[promote_id], char)
