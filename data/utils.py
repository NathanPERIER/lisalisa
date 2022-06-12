
import re
import json

def loadJson(file: str) :
    with open(file, 'r') as f :
        return json.load(f)

def saveJson(data, file: str) :
    with open(file, 'w') as f :
        json.dump(data, f, indent='\t')


def makeCurves(curves) -> "dict[str, list]" :
    data = {curve['type']: [] for curve in curves[0]['curveInfos']}
    for point in curves :
        for curve in point['curveInfos'] :
            data[curve['type']].append(curve['value'])
    return data


filter_reg = re.compile('[^a-zA-Z0-9]+')
def idFromName(name) :
	return filter_reg.sub('_', name.replace('\'', '').lower())
