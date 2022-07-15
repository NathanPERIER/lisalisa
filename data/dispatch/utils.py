
from constants import RAW_DIR, BACK_DIR
from args import Options

import os
import json
from enum import Enum

class OutputDir(Enum) :
	BACK = BACK_DIR


def loadJson(file: str) :
	path = os.path.join(RAW_DIR, file)
	with open(path, 'r') as f :
		return json.load(f)

def saveJsonMinimal(data, dir: OutputDir, file: str) :
	path = os.path.join(dir.value, file)
	with open(path, 'w') as f :
		json.dump(data, f, indent=None, separators=(',', ':'))

def saveJsonPretty(data, dir: OutputDir, file: str) :
	path = os.path.join(dir.value, file)
	with open(path, 'w') as f :
		json.dump(data, f, indent='\t', separators=(', ', ': '))

saveJson = saveJsonPretty if Options.debugMode else saveJsonMinimal
