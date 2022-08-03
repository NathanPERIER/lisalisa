
from common.dataobj.images import ImageStore, CharacterImageStore, WeaponImageStore, ArtifactImageStore
from common.dataobj.character import Character
from common.dataobj.weapon import    Weapon
from common.dataobj.artifact import  ArtifactSet

AMBR_IMAGE_TEMPLATE = "https://api.ambr.top/assets/UI/%s.png"

image_store = ImageStore()


# TODO one package in each section

def registerItemImage(item_id: str, item: "dict[str,any]") :
    icon_name = f"UI_ItemIcon_{item['hoyo_id']}"
    image_store.items[item_id] = AMBR_IMAGE_TEMPLATE % icon_name

"""
https://api.ambr.top/assets/UI/UI_AvatarIcon_Mona.png
+ Full list of skins from wiki

https://api.ambr.top/assets/UI/UI_Gacha_AvatarImg_Mona.png
+ Full list of skins from wiki

https://api.ambr.top/assets/UI/Skill_A_Catalyst_MD.png
https://api.ambr.top/assets/UI/Skill_S_Mona_01.png
https://api.ambr.top/assets/UI/Skill_S_Mona_02.png
https://api.ambr.top/assets/UI/Skill_E_Mona_01.png
AvatarSkillExcelConfigData.json

https://api.ambr.top/assets/UI/UI_Talent_S_Mona_05.png
https://api.ambr.top/assets/UI/UI_Talent_S_Mona_06.png
https://api.ambr.top/assets/UI/UI_Talent_Combine_Weapon.png
ProudSkillExcelConfigData.json

https://api.ambr.top/assets/UI/UI_Talent_S_Mona_01.png
https://api.ambr.top/assets/UI/UI_Talent_S_Mona_02.png
https://api.ambr.top/assets/UI/UI_Talent_U_Mona_01.png
https://api.ambr.top/assets/UI/UI_Talent_S_Mona_03.png
https://api.ambr.top/assets/UI/UI_Talent_U_Mona_02.png
https://api.ambr.top/assets/UI/UI_Talent_S_Mona_04.png
AvatarTalentExcelConfigData.json
"""
def registerCharacterImages(char_id: str, char: Character) :
    res = CharacterImageStore()
    res.normal_attack = AMBR_IMAGE_TEMPLATE % char.talents['normal_attack']['icon']
    # ...
    image_store.characters[char_id] = res


"""
From wiki
"""
def registerWeaponImages(weapon_id: str, weapon: Weapon) :
    pass


"""
https://api.ambr.top/assets/UI/reliquary/UI_RelicIcon_10010_4.png
Build from set id + {'flower': 4, 'plume': 2, 'sands': 5, 'goblet': 1, 'circlet': 3}
"""
def registerArtifactImages(set_id: str, art_set: ArtifactSet) :
    pass
