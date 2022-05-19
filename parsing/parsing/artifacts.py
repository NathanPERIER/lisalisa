#!/usr/bin/python3
from utils.io import readToSoup
from utils.soup import idFromLink, idFromName, getTagContent, getRef


def getArtifactInfo(link) :
	res={}

	soup = readToSoup(link)
	
	table_desc = soup.select_one('.item_main_table')
	res['name'] = getTagContent(table_desc.select('td')[4])
	
	stars = []
	star_count = 0
	for node in table_desc.select('td')[6] :
		if node.has_attr('class') and node['class'][0] == 'sea_char_stars_wrap' :
			star_count += 1
		elif star_count > 0 :
			stars.append(star_count)
			star_count = 0
	if star_count > 0 :
		stars.append(star_count)
	res['rarity'] = stars
	
	bonuses = {}
	table_desc = table_desc.select('td')[7:]
	for i in range(len(table_desc)//2) :
		title = getTagContent(table_desc[2*i])
		if title.endswith('Piece Bonus') :
			bonuses[title[0]] = getTagContent(table_desc[2*i+1])
	res['bonus'] = bonuses
	
	pieces = {}
	table_items = soup.select_one('table.add_stat_table:nth-child(5)')
	for span in table_items.select('td > a > span') : 
		line = getTagContent(span).strip()
		if line.endswith(' (Flower of Life)') :
			pieces['flower_of_life'] = line[0:-17]
		elif line.endswith(' (Plume of Death)') :
			pieces['plume_of_death'] = line[0:-17]
		elif line.endswith(' (Sands of Eon)') :
			pieces['sands_of_eon'] = line[0:-15]
		elif line.endswith(' (Goblet of Eonothem)') :
			pieces['goblet_of_eonothem'] = line[0:-21]
		elif line.endswith(' (Circlet of Logos)') :
			pieces['circlet_of_logos'] = line[0:-19]
	res['pieces'] = pieces
	
	return res

def readAllArtifacts(link, translate) : 
	res = {}
	soup = readToSoup(link)
	for a in soup.select('table.art_stat_table_new > tr > td:nth-child(3) > a') :
		link = "https://genshin.honeyhunterworld.com" + getRef(a)
		honey_id = idFromLink(link)
		data = getArtifactInfo(link)
		identifier = idFromName(data['name'])
		res[identifier] = data
		translate[honey_id] = identifier
	return res


