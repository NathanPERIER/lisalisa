
from constants import AMBR_IMAGE_TEMPLATE
from common.images import image_store
from items.dataobj import Item

def registerItemImage(item_id: str, item: Item) :
    icon_name = f"UI_ItemIcon_{item.hoyo_id}"
    image_store.items[item_id] = AMBR_IMAGE_TEMPLATE % icon_name
