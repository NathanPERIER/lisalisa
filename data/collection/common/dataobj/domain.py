
from common.dataobj import DataObject

class Domain(DataObject) :
	def __init__(self) :
		# Identifiers
		self.hoyo_id:  int = 0
		self.scene_id: int = 0
		self.entry_id: int = 0
		# General data
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.type: str = None
		self.req_ar: int = 0
		# Sub-domains
		self.sub_domains: "list[list[SubDomain]]" = []

class SubDomain(DataObject) :
	def __init__(self) :
		# Identifiers
		self.hoyo_id:   int = 0
		self.scene_id:  int = 0
		self.reward_id: int = 0
		# General data
		self.name_hash: int = 0
		self.name: str = None
		self.type: str = None
		self.city: str = None
		self.days: "list[str]" = []
		self.sub_name: str = None
		self.level: int = 0
		# Effects
		self.effects_hash: "list[int]" = []
		self.effects: "list[str]"      = []
		# Requirements
		self.reco_types: "list[str]" = []
		self.reco_level: int = 0
		self.req_ar: int = 0
		# Metadata used to group sub-domains together
		self.ui_type: str = None
