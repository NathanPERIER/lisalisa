
from utils import loadJson, indexById
from constants import ITEM_REWARDS_JSON, ITEM_REWARDS_PREV_JSON
from translate.mhy import mhy_items

rewards  = indexById(loadJson(ITEM_REWARDS_JSON), 'rewardId')
previews = indexById(loadJson(ITEM_REWARDS_PREV_JSON)[1:]) # first element is malformed


def getRewards(reward_id: int, preview = False) -> "dict[str,any]" :
	if preview :
		return __g_getPrevRewards(reward_id)
	return __g_getRealRewards(reward_id)


def __g_getRealRewards(reward_id: int) -> "dict[str,any]" :
	reward = rewards[reward_id]
	return __g_formatRewards(reward['rewardItemList'], 'itemId', 'itemCount')

def __g_getPrevRewards(reward_id: int) -> "dict[str,any]" :
	reward = previews[reward_id]
	return __g_formatRewards(reward['previewItems'], 'id', 'count')


def __g_formatRewards(reward_list: "list[dict[str,any]]", id_prop: str, count_prop: str) -> "dict[str,any]" :
	return {
		mhy_items[reward[id_prop]]: reward[count_prop]
		for reward in reward_list
		if id_prop in reward and count_prop in reward
	}
