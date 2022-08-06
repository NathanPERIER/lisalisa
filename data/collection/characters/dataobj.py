
from common.dataobj import DataObject
from common.ascensions.dataobj import Ascensions
from items.dataobj import Dish


class CharTalentStats(DataObject) :
	def __init__(self) :
		self.names: "list[str]" = None
		self.values: "list[list[str]]" = None


class CharTalent(DataObject) :
	def __init__(self) :
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.icon: str = None
		self.charge_num: int = 0
		self.costs: "list[dict[str,int]]" = None
		self.stats: CharTalentStats = None


class CharTalents(DataObject) :
	def __init__(self) :
		self.normal_attack:    CharTalent = None
		self.elemental_skill:  CharTalent = None
		self.elemental_burst:  CharTalent = None
		self.alternate_sprint: CharTalent = None


class CharPassive(DataObject) :
	def __init__(self) :
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.icon: str = None
		self.ascension: int = 0


class CharConstellation(DataObject) :
	def __init__(self) :
		self.name_hash: int = 0
		self.desc_hash: int = 0
		self.name: str = None
		self.desc: str = None
		self.icon: str = None


class CharSpecialDish(Dish) :
	def __init__(self):
		self.original_recipe: str = None
	def fromDish(dish: Dish) -> "CharSpecialDish" :
		res = CharSpecialDish()
		res.__dict__.update(dish.__dict__)
		return res


class CharSkin(DataObject) :
    def __init__(self) :
        # Identifiers
        self.hoyo_id: int = 0
        # General data
        self.name_hash: int = 0
        self.desc_hash: int = 0
        self.name: str = None
        self.desc: str = None
        self.icon: str = None
        self.restricted: bool = False


class CharSkins(DataObject) :
    def __init__(self) :
        self.default: CharSkin = None
        self.alt: "list[CharSkin]" = []


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
		self.icon: str = None
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
		self.default_weapon: str = None
		# Stats
		self.base_stats = {}
		self.curves = {}
		# Ascensions
		self.ascensions: Ascensions = None
		# Talents, passives, constellations
		self.talents:        CharTalents = CharTalents()
		self.passives:       "list[CharPassive]" = None
		self.constellations: "list[CharConstellation]" = None
		# Skins
		self.skins: CharSkins = CharSkins()
		# Special dish
		self.special_dish: CharSpecialDish = None


class CharacterImageStore(DataObject) :
    def __init__(self) :
        self.front:  str = None
        self.banner: str = None
        self.normal_attack:   str = None
        self.elemental_skill: str = None
        self.elemental_burst: str = None
        self.constellations: "list[str]" = []
        self.passives: "list[str]" = []
