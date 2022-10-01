
from common.dataobj import DataObject


class ArtifactPiece(DataObject) :
	def __init__(self) :
		# Identifiers
		self.hoyo_id:   int = 0
		self.gadget_id: int = 0
		self.story_id:  int = 0
		self.prop_id:   int = 0
		self.set_id:    int = 0
		# General data
		self.type: str = None
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.rarity: int = 0
		# Stats
		self.max_level: int = 0
		self.add_prop_levels: "list[int]" = []
		self.conv_exp: int = 0


class ArtifactSetEquip(DataObject) :
	def __init__(self) :
		# Identifiers
		self.hoyo_id:   int = 0
		# General data
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.nb_req: int = 0


class ArtifactRaritySet(DataObject) :
	def __init__(self) :
		# Identifiers
		self.display_id:   int = 0
		# General data
		self.name_hash: int = 0
		self.name: str = None
		self.rarity: int = 0
		self.pieces: "list[ArtifactPiece]" = []
		# Stats
		self.substats: "dict[str,list[int]]" = {}


class ArtifactSet(DataObject) :
	def __init__(self) :
		# Identifiers
		self.hoyo_id:  int = 0
		self.equip_id: int = 0
		# General data
		self.name: str = None
		self.bonuses: "list[ArtifactSetEquip]" = []
		self.pieces: "list[ArtifactRaritySet]" = []

