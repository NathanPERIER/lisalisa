import logging

from utils.io import saveJson

logger = logging.getLogger(__name__)


class Recorder :

	def __init__(self, translate_data={}) :
		self.translate = TrackUpdateDict(translate_data)
		self.images = ImageRegister()
	
	def addItem(self, identifier: str, honey_id: str, url: str) :
		self.translate[honey_id] = identifier
		self.images.addItem(identifier, url)


class ImageRegister :

	def __init__(self) :
		self._items = {}
		self._characters = {}
		self._weapons = {}
		self._temp_char = {}
		self._temp_weapon = {}
	
	def addItem(self, identifier: str, url: str) :
		self._items[identifier] = url

	def addForCharacter(self, filename: str, url: str) :
		self._temp_char[filename] = url
	
	def popCharacter(self, char: str) :
		self._characters[char] = self._temp_char
		self._temp_char = {}
	
	def addForWeapon(self, filename: str, url: str) :
		self._temp_weapon[filename] = url
	
	def popWeapon(self, weapon: str) :
		self._weapons[weapon] = self._temp_weapon
		self._temp_weapon = {}
	
	def getLinks(self) :
		return {'characters': self._characters, 'weapons': self._weapons, 'items': self._items}
	
	def save(self, path) :
		saveJson(path, self.getLinks())



class TrackUpdateDict(dict) :

	def __init__(self, data={}) :
		super().__init__(data)
		self.modified = False
		self.alert_add = lambda key, value : logger.info(f"ADD translation for key \"{key}\" : \"{value}\"")
		self.alert_mod = lambda key, old, new : logger.warning(f"MODIFIED translation for key \"{key}\" : \"{old}\" => \"{new}\"")
		self.alert_notfound = lambda key : logger.warning(f"NOT_FOUND translation for key \"{key}\"")

	def onAdd(self, call) :
		self.alert_add = call

	def onModified(self, call) :
		self.alert_mod = call
	
	def onNotFound(self, call) :
		self.alert_notfound = call

	def __setitem__(self, key, value) :
		if key not in self :
			self.alert_add(key, value)
		elif self[key] != value :
			self.alert_mod(key, self[key], value)
		else :
			return
		super().__setitem__(key, value)
		self.modified = True
	
	def __delitem__(self, key) :
		if key in self :
			super().__delitem__(key)
			self.modified = True
	
	def __getitem__(self, key) :
		if key not in self :
			self.alert_notfound(key)
			return None
		else :
			return super().__getitem__(key)
		

	def saveIfModified(self, path) :
		if self.modified :
			saveJson(path, self)
			self.modified = False
	
