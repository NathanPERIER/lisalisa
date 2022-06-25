
from utils import loadJson
from constants import WEAPON_CURVES_JSON
from common.curves import makeCurves

curves = makeCurves(loadJson(WEAPON_CURVES_JSON))

