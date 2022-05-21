#!/usr/bin/python3
import re

from utils.io import readToSoup
from utils.recorder import Recorder
from utils.soup import idFromLink, idFromName, getTagContent, getRef


def readItem(itemcont) :
	res = {}
	res['name'] = getTagContent(itemcont.select_one('.itemname'))
	res['rarity'] = len(itemcont.select_one('.itemstarcont').select('.stars_wrap'))
	img: str = itemcont.select_one('img.itempic')['data-src']
	if img.endswith('_35.png') :
		img = f"{img[:-7]}.png"
	return res, img
	
def readAllItems(link, record: Recorder) : 
	res = {}
	soup = readToSoup(link)
	items = soup.select('.itemcont')
	for item in items :
		link = getRef(item.select_one('a'))
		honey_id = idFromLink(link)
		data, img = readItem(item)
		identifier = idFromName(data['name'])
		res[identifier] = data
		record.addItem(identifier, honey_id, img)
	return res


inline_xp_val = re.compile(r'.* Gives (.+) EXP\..*') 
def expValue(link) :
	soup = readToSoup(link)
	desc_rough = str(soup.select_one('.item_main_table > tr:nth-child(4) > td:nth-child(2)'))
	return int(inline_xp_val.match(desc_rough).group(1).replace(',', ''))
	
def readExpMaterials(link, record: Recorder) :
	res = {}
	soup = readToSoup(link)
	items = soup.select('.itemcont')
	for item in items :
		link = getRef(item.select_one('a'))
		item_res, img = readItem(item)
		item_res['value'] = expValue(f"https://genshin.honeyhunterworld.com{link}")
		honey_id = idFromLink(link)
		identifier = idFromName(item_res['name'])
		res[identifier] = item_res
		record.addItem(identifier, honey_id, img)
	return res


