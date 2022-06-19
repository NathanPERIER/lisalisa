
from common.dataobj import DataObject

class Character(DataObject) :
	def __init__(self) :
		# Identifiers
		self.hoyo_id:        int = 0
		self.promote_id:     int = 0
		self.skill_depot_id: int = 0
		self.fetter_id:      int = 0
		# General data
		self.weapon: str = None
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.rarity: int = 0
		self.special: bool = False
		self.body: str = None
		self.birthday: "list[int]" = None
		self.region: str = None
		self.vision_hash:     "list[int]" = None
		self.astrolabe_hash:  "list[int]" = None
		self.allegiance_hash:  int        = 0
		self.vision:     str = None
		self.astrolabe:  str = None
		self.allegiance: str = None
		# Stats
		self.base_stats = {}
		self.curves = {}
		# Talents, passives, constellations
		self.talents:        dict = None
		self.passives:       dict = None
		self.constellations: dict = None
		# Abilities + refinement
		self.abilities: list = None
		# Skins
		self.skins = {
			'default': None,
			'alt': []
		}
