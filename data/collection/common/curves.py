
def makeCurves(curves) -> "dict[str, list]" :
    data = {curve['type']: [] for curve in curves[0]['curveInfos']}
    for point in curves :
        for curve in point['curveInfos'] :
            data[curve['type']].append(curve['value'])
    return data