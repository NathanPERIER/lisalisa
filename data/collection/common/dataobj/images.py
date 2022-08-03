
from common.dataobj import DataObject

# TODO split into other dataobj packages

class CharacterImageStore(DataObject) :
    def __init__(self) :
        self.front:  str = None
        self.banner: str = None
        self.normal_attack:   str = None
        self.elemental_skill: str = None
        self.elemental_burst: str = None
        self.constellations: "list[str]" = []
        self.passives: "list[str]" = []


class WeaponImageStore(DataObject) :
    def __init__(self) :
        self.default:  str = None
        self.awakened: str = None


class ArtifactImageStore(DataObject) :
    def __init__(self) :
        self.flower_of_life:     str = None
        self.plume_of_death:     str = None
        self.sands_of_eon:       str = None
        self.goblet_of_eonothem: str = None
        self.circlet_of_logos:   str = None


class ImageStore(DataObject) :
    def __init__(self) :
        self.items:      "dict[str,str]" = {}
        self.characters: "dict[str,CharacterImageStore]" = {}
        self.weapons:    "dict[str,WeaponImageStore]" = {}
        self.artifacts:  "dict[str,ArtifactImageStore]" = {}
