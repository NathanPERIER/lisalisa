
from common.dataobj import DOEncoder

import re
import json

def loadJson(file: str) :
    with open(file, 'r') as f :
        return json.load(f)

def saveJson(data, file: str) :
    with open(file, 'w') as f :
        json.dump(data, f, cls=DOEncoder, indent='\t')


filter_reg = re.compile('[^a-zA-Z0-9]+')
def idFromName(name) :
	return filter_reg.sub('_', name.replace('\'', '').lower()).strip('_')


def indexById(l: list, id_field: str = 'id') -> "dict[int,any]" :
    return {x[id_field]: x for x in l}

def groupByField(ld: "list[dict[str,any]]", field: str) -> "dict[str,list[dict[str,any]]]" :
	res: "dict[str,list[dict[str,any]]]" = {}
	for d in ld :
		val = d[field]
		if val not in res :
			res[val] = [d]
		else :
			res[val].append(d)
	return res
