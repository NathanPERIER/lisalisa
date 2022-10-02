
from constants import AMBR_IMAGE_TEMPLATE
from common.images import image_store
from common.images.dataobj import CharacterImageStore
from characters.dataobj import Character

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
    res.normal_attack = AMBR_IMAGE_TEMPLATE % char.talents.normal_attack.icon
    # ...
    image_store.characters[char_id] = res