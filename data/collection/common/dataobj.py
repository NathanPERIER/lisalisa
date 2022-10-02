
import copy
from json import JSONEncoder
from enum import Enum

import logging

logger = logging.getLogger(__name__)


class DataObject :

	def toJson(self) :
		return self.__dict__
	
	def clone(self) :
		return copy.deepcopy(self)
	
	def __getitem__(self, key: str) :
		if key in self.__dict__ :
			return self.__dict__[key]
		logger.error("Property %s doesn't exist in object of type %d", key, type(self).__name__)
		return None	


class DOEncoder(JSONEncoder) :

	def __init__(self, **kwargs) :
		super().__init__(**kwargs)
	
	def default(self, o) :
		if issubclass(type(o), DataObject) :
			return o.toJson()
		if issubclass(type(o), Enum) :
			return o.value
		return super().default(o)
