
from constants import RAW_DIR
from utils import loadJson
from engine.core import Dispatcher

import os


class MergeDispatcher(Dispatcher) :

	def __init__(self, input_folder: str, output_file: str, transform = None, ignore: "list[str]" = []) :
		super().__init__(input_folder, output_file, transform)
		self._ignore = ignore
	
	def load(self):
		self._data = {}
		input_dir = os.path.join(RAW_DIR, self._input)
		for file in os.listdir(input_dir) :
			if file.endswith('.json') :
				name = file[:-5]
				if name not in self._ignore :
					fullpath = os.path.join(input_dir, file)
					self._data[name] = loadJson(fullpath)
	
	def process(self) :
		if self._transform is None :
			self._res = self._data
			return
		self._res = {
			name: self._transform(self, value)
			for name, value in self._data.items()
		}
