
from utils import loadJson
from constants import CHAR_CURVES_JSON
from common.curves import makeCurves

curves = makeCurves(loadJson(CHAR_CURVES_JSON))


def setCurves(characters: dict) :
    for char in characters.values() :
        stat_names = list(char['ascensions']['props'][0]['values'])
        stats = {}
        for stat in stat_names :
            init_val = char['base_stats'][stat] if stat in char['base_stats'] else 0.0
            if stat in char['curves'] :
                curve = computeCurve(stat, char['curves'][stat], init_val, char['ascensions']['props'])
            else :
                curve = computeConstantCurve(stat, init_val, char['ascensions']['props'])
            stats[stat] = curve
        char['stats'] = stats


def computeCurve(curve_name: str, curve_type: str, init_val: float, props: list) :
    res = []
    level = 1
    curve = curves[curve_type]
    for prop in props : 
        shift = prop['values'][curve_name]
        res.append([
            __g_curvePoint(curve, l, init_val, shift) 
            for l in range(level, prop['until'] + 1)
        ])
        level = prop['until']
    return res

def __g_curvePoint(curve: list, level: int, init_val: float, shift: float) :
    return init_val * curve[level - 1] + shift


def computeConstantCurve(curve_name: str, init_val: float, props: list) :
    res = []
    level = 1
    for prop in props : 
        shift = prop['values'][curve_name]
        size = prop['until'] + 1 - level
        res.append([init_val + shift] * size)
        level = prop['until']
    return res
