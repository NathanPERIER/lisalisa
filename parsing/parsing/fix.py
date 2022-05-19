
import logging

logger = logging.getLogger(__name__)

__fixers = {}

def apply(data, translate, name: str) :
	if name in __fixers :
		logger.info('FIX %s', name)
		__fixers[name](data, translate)

def register(name: str) :
	def decorator(f) :
		__fixers[name] = f
		return f
	return decorator

@register('zhongli')
def fixZhongli(data, _translate) :
	data['astrolabe'] = 'Lapis Dei'

@register('local_materials')
def fixLocalMaterials(data, translate) :
	data['onikabuto'] = {
		'name': 'Onikabuto',
		'rarity': 1
	}
	translate['i_680'] = 'onikabuto'
	data['dendrobium'] = {
		'name': 'Dendrobium',
		'rarity': 1
	}
	translate['i_677'] = 'dendrobium'
	