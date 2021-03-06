
from utils import loadJson, groupByField
from constants import ARTIFACT_AFFIXES_JSON, ARTIFACT_CURVES_JSON
from common.props import PropType


def __g_formatAffixes(affixes: "list[dict[str,any]]") -> "dict[int,dict[str,list[dict[str,any]]]]" :
    res = {}
    for depot_id, data in groupByField(affixes, 'depotId').items() :
        res[depot_id] = groupByField(data, 'propType')
    return res

affixes = __g_formatAffixes(loadJson(ARTIFACT_AFFIXES_JSON))


def __g_makeArtifactCurves(data: "list[dict]") :
    rarity_groups = list(groupByField([x for x in data if 'rank' in x], 'rank').items())
    rarity_groups.sort(key = lambda p: p[0])
    return [
        __g_makeArtifactRarityCurves(rarity_curves)
        for _rarity, rarity_curves in rarity_groups
    ]


def __g_makeArtifactRarityCurves(data: "list[dict[str,any]]") :
    data.sort(key = lambda pt: pt['level'])
    res = []
    for pt in data :
        exp = pt['exp']
        props: "dict[str,float]" = {
            PropType[x['propType']].value: x['value']
            for x in pt['addProps']
            if 'propType' in x and 'value' in x
        }
        # Fix percentages not actually being percentages
        props = {
            prop: value * 100 if prop.endswith('%') else value
            for prop, value in props.items()
        }
        res.append({
            'exp': exp,
            'props': props
        })
    return res


curves = __g_makeArtifactCurves(loadJson(ARTIFACT_CURVES_JSON))


def getSetAffixes(depot_id: int) :
    res = {}
    for prop, affx in affixes[depot_id].items() :
        values = [x['propValue'] for x in affx]
        prop_name: str = PropType[prop].value
        if prop_name.endswith('%') :
            values = [x * 100 for x in values]
        res[prop_name] = values
    return res
