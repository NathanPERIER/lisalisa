
import logging

logger = logging.getLogger(__name__)


class TrackUpdateDict(dict) :

	def __init__(self, supply_startegy = None) :
		super().__init__()
		self.supply = supply_startegy if supply_startegy is not None else TrackUpdateDict.__default_strategy
	
	def __default_strategy(key) :
		logger.warning("Translation not found for entry %s", str(key))
		return key
	
	def __getitem__(self, key) :
		str_key = str(key)
		if str_key not in self :
			value = self.supply(str_key)
			super().__setitem__(str_key, value)
			return value
		return super().__getitem__(str_key)

	def __setitem__(self, key, value) :
		str_key = str(key)
		if str_key in self :
			logger.warning("Override value for entry %s (%s -> %s)", str_key, str(self[str_key]), str(value))
		super().__setitem__(str_key, value)
