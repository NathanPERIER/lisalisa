
from common.dataobj     import DataObject
from characters.dataobj import CharacterImageStore
from weapons.dataobj    import WeaponImageStore
from artifacts.dataobj  import ArtifactImageStore


class ImageStore(DataObject) :
    def __init__(self) :
        self.items:      "dict[str,str]" = {}
        self.characters: "dict[str,CharacterImageStore]" = {}
        self.weapons:    "dict[str,WeaponImageStore]" = {}
        self.artifacts:  "dict[str,ArtifactImageStore]" = {}
