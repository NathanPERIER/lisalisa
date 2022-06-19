
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
	return filter_reg.sub('_', name.replace('\'', '').lower())
