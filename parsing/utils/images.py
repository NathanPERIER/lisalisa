
class ImageRegister :

	def __init__(self) :
		self._items = {}
		self._characters = {}
	
	def addItem(self, identifier: str, url: str) :
		self._items[identifier] = url
	
	def addCharacter(self, char: str, filename: str, url: str) :
		if char not in self._characters :
			self._characters[char] = {}
		self._characters[char][filename] = url
	
	def getLinks(self) :
		return {'items': self._items, 'characters': self._characters}
