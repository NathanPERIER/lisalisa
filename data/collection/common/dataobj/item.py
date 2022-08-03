
from common.dataobj import DataObject

class Item(DataObject) :
    def __init__(self) :
        # Identifiers
        self.hoyo_id: int = 0
        # General data
        self.name_hash: int = 0
        self.desc_hash: int = 0
        self.type_hash: int = 0
        self.name: str = None
        self.desc: str = None
        self.type: str = None
        self.rarity: int = 0


class Dish(Item) :
    def __init__(self) :
        self.effect_hash: int = 0
        self.effect: str = None
        self.count: int = 0
    def fromItem(item: Item) -> "Dish" :
        res = Item()
        res.__dict__.update(item.__dict__)
        return res

