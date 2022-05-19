#!/usr/bin/python3
from utils.io import readToSoup
from utils.soup import idFromImage, idFromName, getTagContent, getArray, removeWrapper, readItems, getRef

# The last column of a statistics table is usually incomplete
# and doesn't contain interesting data
# Hence, this function removes it
def cleanStats(arr, last_col_name) :
	newlen = len(arr[0])
	if arr[0][-1] == last_col_name :
		newlen -= 1
	if arr[0][newlen-1] == 'none' :
		newlen -= 1
	if newlen != len(arr[0]) :
		for line in arr :
			while len(line) > newlen : 
				del line[-1]
	return {
		'desc': arr[0][1:],
		'values': {l[0]: l[1:] for l in arr[1:]}
	}


def getWeaponInfo(link, translate) :
	res={}
	soup = readToSoup(link)
	
	res['name'] = getTagContent(soup.select_one('.custom_title')).strip()
	info = soup.select_one('div.data_cont_wrapper:nth-child(5) > table:nth-child(1)')
	res['type'] = getTagContent(info.select_one('tr:nth-child(1) > td:nth-child(3) > a:nth-child(1)')).lower()
	res['rarity'] = len(info.select_one('tr:nth-child(2) > td:nth-child(2)').select('div'))
	res['desc'] = getTagContent(info.select_one('tr:nth-child(8) > td:nth-child(2)'))
	
	ability = getTagContent(info.select_one('tr:nth-child(6) > td:nth-child(2)'))
	if len(ability) > 0 and ability != 'None' :
		descriptions = soup.select_one('div.data_cont_wrapper:nth-child(5) > table:nth-child(5)').select('td:nth-child(2)')
		res['ability'] = {
			'name': ability,
			'desc': [removeWrapper(x) for x in descriptions]
		}
	else :
		res['ability'] = None
	
	refine = soup.select_one('div.data_cont_wrapper:nth-child(5) > table:nth-child(3)')
	res['enhancement'] = cleanStats(getArray(refine), 'Ascension Materials')
	res['ascensions'] = [readItems(x, translate) for x in refine.select('td:nth-child(4)')[2:]]
	
	return res


def readAllWeapons(link, translate) : 
	res = {}
	soup = readToSoup(link)
	table = soup.select_one('div.scrollwrapper:nth-child(3) > table:nth-child(1)')
	for tr in table.select('tr')[1:] :
		link = "https://genshin.honeyhunterworld.com" + getRef(tr.select_one('td:nth-child(3) > a'))
		honey_id = idFromImage(tr.select_one('.itempic'))
		data = getWeaponInfo(link, translate)
		identifier = idFromName(data['name'])
		res[identifier] = data
		translate[honey_id] = identifier
	return res

