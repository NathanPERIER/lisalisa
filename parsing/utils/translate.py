import logging

from utils.io import saveJson

logger = logging.getLogger(__name__)

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
	
