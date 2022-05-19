#!/usr/bin/python3
from utils.io import readToSoup
from utils.soup import idFromLink, idFromImage, getTagContent, removeWrapper, firstGroup, getRef
import re

item_quantity = re.compile(r'x ?(.*)')
def readRecipeEntry(soup) :
	res = []
	for div in soup.select('.sea_item_used_by_char') : 
		materials = [idFromLink(a) for a in div.select('a')]
		quantities = [int(firstGroup(item_quantity, getTagContent(span))) for span in div.select('span')]
		res.append(dict(zip(materials, quantities)))
	return res
	
def readAllRecipes(soup) : 
	res = {}
	for item in soup.select_one('.items_wrap').select('.itemcont') :
		link = getRef(item.select_one('a'))
		res[idFromLink(link)] = readRecipeEntry(item)
	return res


def readPotion(soup) :
	res = {}
	res['name'] = getTagContent(soup.select_one('.itemname'))
	res['rarity'] = len(soup.select_one('.itemstarcont').select('.stars_wrap'))
	res['effect'] = getTagContent(soup.select_one('span.sea_wep_item_prop'))
	return res

def readAllPotions(soup) :
	res = {}
	items = soup.select('.itemcont')
	for item in items :
		link = getRef(item.select_one('a'))
		res[idFromLink(link)] = readPotion(item)
	return res


def readAllFoods(soup) :
	res = {}
	for item in soup.select_one('.items_wrap').select('.itemcont') :
		data = {'recipies':readRecipeEntry(item)}
		link = getRef(item.select_one('a'))
		if link.startswith('/db/char/') :
			data['character'] = idFromLink(link)
			link = getRef(item.select('a')[1])
		else : 
			data['character'] = None
		identifier = idFromLink(link)
		if len(identifier.split('_')) == 2 or data['character'] != None :
			link = "https://genshin.honeyhunterworld.com" + link
			print("[GenshinCraftingRecipies] PARSE " + link)
			item_soup = readToSoup(link)
			table = item_soup.select_one('table.item_main_table:nth-child(3)')
			data['rarity'] = len(table.select('tr:nth-child(2) > td:nth-child(2) > div.sea_char_stars_wrap'))
			data['effect'] = removeWrapper(table.select_one('tr:nth-child(3) > td:nth-child(2)'))
			data['description'] = removeWrapper(table.select_one('tr:nth-child(5) > td:nth-child(2) > div'))
			data['name'] = getTagContent(item_soup.select_one('.custom_title'))
			if data['character'] != None :
				data['derived'] = idFromImage(item_soup.select_one('.item_main_table_alt > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > img:nth-child(1)'))
			res[identifier] = data
	return res

