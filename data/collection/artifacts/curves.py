
from utils import loadJson, groupByField
from constants import ARTIFACT_CURVES_JSON
from common.props import PropType


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
        props = {
            PropType[x['propType']].value: x['value']
            for x in pt['addProps']
            if 'propType' in x and 'value' in x
        }
        res.append({
            'exp': exp,
            'props': props
        })
    return res


curves = __g_makeArtifactCurves(loadJson(ARTIFACT_CURVES_JSON))
