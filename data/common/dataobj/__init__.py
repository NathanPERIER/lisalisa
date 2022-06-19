
from json import JSONEncoder


class DataObject :

	def toJson(self) :
		return self.__dict__


class DOEncoder(JSONEncoder) :

	def __init__(self, **kwargs) :
		super().__init__(**kwargs)
	
	def default(self, o) :
		if issubclass(type(o), DataObject) :
			return o.toJson()
		return super().default(o)
