
from utils import loadJson
from constants import EXP_FRIENDSHIP_JSON

friendship_exp: list = loadJson(EXP_FRIENDSHIP_JSON)


def readFriendshipExp() -> "list[int]" :
	friendship_exp.sort(key = lambda x: x['fetterLevel'])
	return [x['needExp'] for x in friendship_exp]
