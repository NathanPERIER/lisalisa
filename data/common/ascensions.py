
import logging

logger = logging.getLogger(__name__)

def formatAscensions(ascensions: list) -> dict :
    if len(ascensions) == 7 :
        ascensions = ascensions[1:]
    else :
        logger.warning('Expected 6 ascensions (7 items), got %d items', len(ascensions))
    ascensions.sort(key = lambda asc: asc['level'])
    # TODO translate the item ids (hoyo_id)
    costs = [asc['cost'] for asc in ascensions]
    props = [
        {
            'values': asc['props'], 
            'until': asc['maxLvl']
        }
        for asc in ascensions
    ]
    return {
        'costs': costs,
        'props': props
    }
