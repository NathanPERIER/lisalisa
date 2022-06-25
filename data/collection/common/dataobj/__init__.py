
import copy
from json import JSONEncoder
from enum import Enum


class DataObject :

	def toJson(self) :
		return self.__dict__
	
	def clone(self) :
		return copy.deepcopy(self)


class DOEncoder(JSONEncoder) :

	def __init__(self, **kwargs) :
		super().__init__(**kwargs)
	
	def default(self, o) :
		if issubclass(type(o), DataObject) :
			return o.toJson()
		if issubclass(type(o), Enum) :
			return o.value
		return super().default(o)
