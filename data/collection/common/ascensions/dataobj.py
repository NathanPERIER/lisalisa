
from common.dataobj import DataObject


class AscensionLevel(DataObject) :
	def __init__(self) :
		self.level:  int = 0
		self.maxLvl: int = 0
		self.props: "dict[str,float]" = None
		self.cost:  "dict[str,int]"   = None
		self.mora_cost: int           = 0


class AscensionProps(DataObject) :
	def __init__(self) :
		self.values: "dict[str,float]" = None
		self.until: int = 0
	def fromLevelData(data: AscensionLevel) -> "AscensionProps" :
		res = AscensionProps()
		res.values = data.props
		res.until  = data.maxLvl
		return res


class Ascensions(DataObject) :
	def __init__(self) :
		self.costs: "list[dict[str,int]]"  = None
		self.props: "list[AscensionProps]" = None

