#!/usr/bin/python3
from parsing.utils import readToSoup, idFromLink, idFromName, getTagContent, removeWrapper, getRef
import re

def readItem(soup, translate) :
	res = {}
	res['name'] = getTagContent(soup.select_one('.itemname'))
	res['rarity'] = len(soup.select_one('.itemstarcont').select('.stars_wrap'))
	return res
	
def readAllItems(link, translate) : 
	res = {}
	soup = readToSoup(link)
	items = soup.select('.itemcont')
	for item in items :
		link = getRef(item.select_one('a'))
		honey_id = idFromLink(link)
		data = readItem(item, translate)
		identifier = idFromName(data['name'])
		res[identifier] = data
		translate[honey_id] = identifier
	return res


inline_xp_val = re.compile(r'.* Gives (.+) EXP\..*') 
def expValue(link) :
	soup = readToSoup(link)
	desc_rough = str(soup.select_one('.item_main_table > tr:nth-child(4) > td:nth-child(2)'))
	return int(inline_xp_val.match(desc_rough).group(1).replace(',', ''))
	
def readExpMaterials(link, translate) :
	res = {}
	soup = readToSoup(link)
	items = soup.select('.itemcont')
	for item in items :
		link = getRef(item.select_one('a'))
		item_res = readItem(item, translate)
		item_res['value'] = expValue("https://genshin.honeyhunterworld.com" + link)
		honey_id = idFromLink(link)
		identifier = idFromName(item_res['name'])
		translate[honey_id] = identifier
		res[identifier] = item_res
	return res


def readBook(soup) :
	res = {}
	res['title'] = getTagContent(soup.select_one('.post-title'))
	stars = soup.select_one('.item_main_table > tr:nth-child(2) > td:nth-child(2)')
	res['rarity'] = len(stars.select('.sea_char_stars_wrap'))
	desc = soup.select_one('.add_stat_table > tr:nth-child(1) > td:nth-child(1)')
	res['content'] = None if (desc == None) else removeWrapper(desc).replace('\\n', '\n')
	return res

def readAllBooks(soup) :
	res = {'title' : getTagContent(soup.select_one('.post-title'))}
	for div in soup.select_one('.items_wrap').select('div.itemcont') :
		link = getRef(div.select_one('a'))
		print("[GenshinGeneralItems] PARSE " + link)
		book = readBook(readToSoup("https://genshin.honeyhunterworld.com" + link))
		res[idFromLink(link)] = book
	return res


days_code = {'Mon':0, 'Tue':1, 'Wed':2, 'Thu':3, 'Fri':4, 'Sat':5, 'Sun':6}

def readDomain(soup) :
	res = {}
	res['name'] = getTagContent(soup.select_one('.post-title')).strip()
	rewards = [0, 0, 0, 0, 0, 0, 0]
	for tr in soup.select('table.add_stat_table:nth-child(5) > tr')[1:] :
		if int(getTagContent(tr.select_one('td:nth-child(2)'))) in [40, 45] :
			print(tr.select_one('td:nth-child(7)'))
			temp = [idFromLink(a) for a in tr.select_one('td:nth-child(7)').select('a')]
			for day in getTagContent(tr.select_one('td:nth-child(5)')).split(', ') :
				rewards[days_code[day]] = temp
	res['rewards'] = rewards
	return res


