
import logging

logger = logging.getLogger(__name__)

def formatAscensions(ascensions: list, ascendable: dict, expected_nb = 6) -> dict :
    if len(ascensions) == expected_nb + 1 :
        ascensions = ascensions[1:]
    else :
        logger.warning('Expected %d ascensions (%d items) for %s (hoyo: %d / promote: %d), got %d items', 
						expected_nb, expected_nb+1, ascendable['name'], ascendable['hoyo_id'], ascendable['promote_id'], len(ascensions))
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
