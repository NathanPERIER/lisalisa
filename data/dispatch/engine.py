
from utils import OutputDir, loadJson, saveJson
from constants import CONSTANTS_FILE

class DispatchEngine :

	def __init__(self, constants_dest: str, out: OutputDir) :
		self._out_dir = out
		self._constants = loadJson(CONSTANTS_FILE)
		self._dest = constants_dest

	def accept(self, dispatcher: "Dispatcher") :
		dispatcher.setEngine(self)
		dispatcher.load()
		dispatcher.process()
		dispatcher.save(self._out_dir)

	def acceptAll(self, dispatchers: "list[Dispatcher]") :
		for dispatcher in dispatchers :
			self.accept(dispatcher)
	
	def setConstant(self, key: str, value: int) :
		if key in self._constants :
			print("WARNING override ... ") # TODO logging
		self._constants[key] = value

	def close(self) :
		if self._dest is not None :
			saveJson(self._constants, self._out_dir, self._dest)


class Dispatcher :
	
	def __init__(self, input_file: str, output_file: str, transform = None) :
		self._input  = input_file
		self._output = output_file
		self._transform = transform
		self._engine = None
		self._data = None
		self._res  = None
	
	def setEngine(self, engine: DispatchEngine) :
		self._engine = engine

	def getCurrentEngine(self) -> DispatchEngine :
		return self._engine

	def load(self) :
		self._data = loadJson(self._input)
	
	def process(self) :
		if self._transform is None :
			self._res = self._data
		else : 
			self._res = self._transform(self, self._data)
	
	def save(self, dest_dir: OutputDir) :
		saveJson(self._res, dest_dir, self._output)
