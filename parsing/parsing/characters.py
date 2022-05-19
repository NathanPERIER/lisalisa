#!/usr/bin/python3
from utils.io import readToSoup
from utils.soup import getTagContent, extractText, getArray, removeWrapper, readNewItems, getLevelIndexedArray, idFromImage

import re
import logging
from bs4 import BeautifulSoup
from bs4.element import Tag

logger = logging.getLogger(__name__)


def cleanStats(arr) :
	newlen = len(arr[0])
	if arr[0][0].lower() != 'lv' :
		logger.warning('First column of character stats table is not "Lv"')
	if arr[0][newlen-1].lower() == 'total' :
		newlen -= 1
	else :
		logger.warning('Last column of character stats table is not "Total"')
	if arr[0][newlen-1].lower() == 'ascension' :
		newlen -= 1
	else :
		logger.warning('Penultimate column of character stats table is not "Ascension"')
	for line in arr :
		while len(line) > newlen :
			del line[-1]
	return {
		'desc': arr[0][1:],
		'values': {l[0]: l[1:] for l in arr[1:]}
	}

# Reads all the items (+ counts) required for the ascension of a character
# in a column of the character statistics table
def readCharAscension(table: Tag, translate) :
	lines = table.select('tr')
	col_name = getTagContent(lines[0].select('td')[-2])
	if col_name.lower() != 'ascension' :
		logger.warning('Penultimate column of character stats table is not "Ascension"')
	lines = lines[2:-1]
	lines = [lines[2*i] for i in range(len(lines)//2)]
	return [readNewItems(line.select('td')[-2], translate) for line in lines]

# Interpretes a description in such a way that every block of text and its title are stored in
# a list of two items. Returns a list of these structures in the order in which they appear.
# If the first block of text doesn't have a title, the first element of the list will be None
full_desc = re.compile(r'^[^<>]+$')
notitle_desc = re.compile(r'^([^<>]+)(<span.*)$')
title_desc = re.compile(r'^<span[^<>]*>([^<>]+)</span>([^<>]+)(<?.*)$')
def interpreteDescription(html: Tag) :
	desc = removeWrapper(html)
	if full_desc.match(desc) != None :
		return [[None, desc.replace('\\n', '\n').strip('\n')]]
	tabtxt = []
	res = notitle_desc.match(desc)
	if res != None :
		tabtxt = [[None, res.group(1).replace('\\n', '\n').strip('\n')]]
		desc = res.group(2)
	res = title_desc.match(desc)
	while res != None : 
		tabtxt.append([res.group(1), res.group(2).replace('\\n', '\n').strip('\n')])
		desc = res.group(3)
		res = title_desc.match(desc)
	return tabtxt

# Reads the items required to ascend a character's talents
def readTalentAscension(table: Tag, translate) : 
	lines = table.select("tr")[1:]
	lines = [line.select('td')[0:2] for line in lines]
	return {getTagContent(line[0]): readNewItems(line[1], translate) for line in lines}


# Reads the stats and description of a talent for which the description is in the i-th table
def readTalent(soup: BeautifulSoup, i) :
	res = {}
	desc_html = soup.select_one(f"#live_data > table:nth-child({i})")
	title_html = desc_html.select_one('tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
	desc_html = desc_html.select_one('div.skill_desc_layout')
	stats_html = soup.select_one(f"#live_data > div:nth-child({i+1}) > table:nth-child(1)")
	res['title'] = getTagContent(title_html)
	res['desc'] = interpreteDescription(desc_html)
	if res['desc'][0][0] == 'Alternate Sprint' :
		arr = getArray(stats_html)
		res['stats'] = {l[0] : l[1] for l in arr[1:]}
	else :
		res['stats'] = getLevelIndexedArray(stats_html)
	return res

# Reads the passive talents or the constellations of a character (same data structure) and returns
# an associative array where the keys are the names and the items are the descriptions
def readPassivesConstellations(html: Tag) : 
	lines = html.select("tr")
	res = []
	for i in range(0, len(lines)//2) :
		temp = {}
		temp['name'] = getTagContent(lines[2*i].select_one("td:nth-child(2) > a"))
		temp['desc'] = extractText(lines[2*i+1].select_one("td > div.skill_desc_layout"))
		temp['name'] = temp['name'].replace('\\n', '\n').strip('\n')
		res.append(temp)
	return res


def getCharacterInfo(link: str, translate) :
	# Associative array containing all the information
	data = {}

	soup = readToSoup(link)
	
	# General data about the character
	data['name'] = str(soup.select_one('.post-title').string.strip(" "))
	char_lore_html = soup.select_one('#live_data > table:nth-child(1)')
	data['title'] = getTagContent(char_lore_html.select_one("tr:nth-child(2) > td:nth-child(2)"))
	data['allegiance'] = getTagContent(char_lore_html.select_one("tr:nth-child(3) > td:nth-child(2)"))
	data['rarity'] = len(char_lore_html.select_one("tr:nth-child(4) > td:nth-child(2)").select("div"))
	data['vision'] = idFromImage((char_lore_html.select('td')[10]).img).capitalize()
	data['astrolabe'] = getTagContent(char_lore_html.select('td')[14])
	data['weapon'] = getTagContent(char_lore_html.select('td')[8]).lower()
	
	# Character statistics (Atk, Def, ...)
	char_stats_html = soup.select_one('#live_data > div:nth-child(5) > table:nth-child(1)')
	data["stats"] = cleanStats(getArray(char_stats_html))
	
	# Materials and mora required for ascension
	data["ascensions"] = readCharAscension(char_stats_html, translate)
	
	# Attacks / talents of a character
	talents = {}
	# Auto attacks
	talents['normal'] = readTalent(soup, 7)
	if (talents['normal']['title']).startswith('Normal Attack: ') :
		talents['normal']['title'] = talents['normal']['title'][15:]
	# Elemental skill
	talents['skill'] = readTalent(soup, 9)
	# Elemental burst
	talents['burst'] = readTalent(soup, 11)
	if talents['burst']['desc'][0][0] == 'Alternate Sprint' : 
		i = 16
		talents['sprint'] = talents['burst']
		talents['burst'] = readTalent(soup, 13)
	else : 
		i = 14
		talents['sprint'] = None
	
	title_next_part = soup.select_one(f"#live_data > span:nth-child({i-1})").text
	if not title_next_part.startswith('Talent Ascension Materials') :
		logger.warning("span:nth-child(%s) should be 'Talent Ascension Materials ...'", i-1)

	# Talents, passives and constellations are a problem as their number may vary
	talents_title = getTagContent(soup.select_one('#scroll_talent_material'))
	if talents_title.lower().endswith("(single talent)") :
		talents_stats_html = [soup.select_one(f"#live_data > div:nth-child({i}) > table")]
		i += 2
	else : 
		talents_stats_html = [soup.select_one(f"#live_data > div:nth-child({i+k}) > table") for k in range(0, 6, 2)]
		i += 6

	i += 2 # Skip the "Talent Ascension Materials (All 3 Talents lvl 10)" bit
	
	title_next_part = soup.select_one(f"#live_data > span:nth-child({i-1})").text
	if not title_next_part.startswith('Passive Talents') :
		logger.warning("span:nth-child(%d) should be 'Passive Talents'", i-1)
	passives_html = soup.select_one(f"#live_data > table:nth-child({i})")
	
	title_next_part = soup.select_one(f"#live_data > span:nth-child({i+1})").text
	if not title_next_part.startswith('Constellations') :
		logger.warning("span:nth-child(%d) should be 'Constellations'", i+1)
	constellations_html = soup.select_one(f"#live_data > table:nth-child({i+2})")
	
	# Items required for talent ascension
	talents['ascensions'] = [readTalentAscension(x, translate) for x in talents_stats_html]
	data['talents'] = talents
	
	# Passives
	data['passives'] = readPassivesConstellations(passives_html)
	
	# Constellations
	data['constellations'] = readPassivesConstellations(constellations_html)
	
	if data['constellations'][2]['desc'].startswith(f"Increases the Level of {data['talents']['burst']['title']}") :
		data['constellation_increase_burst'] = 3
		data['constellation_increase_skill'] = 5
	else :
		data['constellation_increase_burst'] = 5
		data['constellation_increase_skill'] = 3
	
	return data

