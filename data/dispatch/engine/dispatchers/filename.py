
from engine.core import Dispatcher


class SameFilenameDispatcher(Dispatcher) :
	'''
	Dispatcher that keeps the same filename as the original file
	'''
	
	def __init__(self, input_file: str, transform = None) :
		super().__init__(input_file, input_file.split('/')[-1], transform)

