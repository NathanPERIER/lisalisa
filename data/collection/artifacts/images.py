
from constants import AMBR_IMAGE_TEMPLATE
from common.images import image_store
from common.images.dataobj import ArtifactImageStore
from artifacts.dataobj import ArtifactSet 

__g_piece_num = {
	'flower':  4,
	'plume':   2,
	'sands':   5,
	'goblet':  1,
	'circlet': 3
}

"""
https://api.ambr.top/assets/UI/reliquary/UI_RelicIcon_10010_4.png
Build from set id + {'flower': 4, 'plume': 2, 'sands': 5, 'goblet': 1, 'circlet': 3}
"""
def registerArtifactImages(set_id: str, art_set: ArtifactSet) :
	set_template = AMBR_IMAGE_TEMPLATE % f"reliquary/UI_RelicIcon_{art_set.hoyo_id}_%d"
	res = ArtifactImageStore()
	image_store.artifacts[set_id] = res