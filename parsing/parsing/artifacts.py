#!/usr/bin/python3
from utils.io import readToSoup
from utils.recorder import Recorder
from utils.soup import idFromLink, idFromName, getTagContent, getRef


def getArtifactInfo(link, record: Recorder) :
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
	for a in table_items.select('td > a') : 
		span = a.select_one('span')
		line = getTagContent(span).strip()
		img = a.select_one('img.itempic')['data-src']
		if img.endswith('_35.png') :
			img = f"{img[:-7]}.png"
		if line.endswith(' (Flower of Life)') :
			pieces['flower_of_life'] = line[0:-17]
			record.images.addForArtifact('flower_of_life', img)
		elif line.endswith(' (Plume of Death)') :
			pieces['plume_of_death'] = line[0:-17]
			record.images.addForArtifact('plume_of_death', img)
		elif line.endswith(' (Sands of Eon)') :
			pieces['sands_of_eon'] = line[0:-15]
			record.images.addForArtifact('sands_of_eon', img)
		elif line.endswith(' (Goblet of Eonothem)') :
			pieces['goblet_of_eonothem'] = line[0:-21]
			record.images.addForArtifact('goblet_of_eonothem', img)
		elif line.endswith(' (Circlet of Logos)') :
			pieces['circlet_of_logos'] = line[0:-19]
			record.images.addForArtifact('circlet_of_logos', img)
	res['pieces'] = pieces
	
	return res

def readAllArtifacts(link, record: Recorder) : 
	res = {}
	soup = readToSoup(link)
	for a in soup.select('table.art_stat_table_new > tr > td:nth-child(3) > a') :
		link = "https://genshin.honeyhunterworld.com" + getRef(a)
		honey_id = idFromLink(link)
		data = getArtifactInfo(link, record)
		identifier = idFromName(data['name'])
		res[identifier] = data
		record.translate[honey_id] = identifier
		record.images.popArtifact(identifier)
	return res


