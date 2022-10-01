
from common.images.dataobj import ImageStore
# from artifacts.dataobj     import ArtifactSet
# from constants import AMBR_IMAGE_TEMPLATE


image_store = ImageStore()

def getImageStore() -> ImageStore :
    return image_store
