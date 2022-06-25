from common.dataobj import DataObject

class Weapon(DataObject) :
	def __init__(self) :
		# Identifiers
		self.hoyo_id:     int         = 0
		self.promote_id:  int         = 0
		self.gadget_id:   int         = 0
		self.story_id:    int         = 0
		self.skill_affix: "list[int]" = None
		# General data
		self.type: str = None
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.rarity: int = 0
		# Stats
		self.base_stats = {}
		self.curves = {}
		# Ascensions
		self.ascensions: dict = None
		# Abilities + refinement
		self.abilities: list = None 
