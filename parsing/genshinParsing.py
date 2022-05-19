#!/usr/bin/python3
import os
import sys
import logging

from utils.io import readToSoup, loadJson, saveJson
from utils.soup import idFromName
from utils.recorder import Recorder
import parsing.fix as fix
from parsing.characters import getCharacterInfo
from parsing.artifacts import readAllArtifacts
from parsing.weapons import readAllWeapons
from parsing.items import readExpMaterials, readAllItems

logging.basicConfig(format='[%(name)s|%(levelname)s] %(message)s', level=logging.INFO)
logger = logging.getLogger('parsing')

BASE_URL = 'https://genshin.honeyhunterworld.com'

DIR = os.path.dirname(os.path.realpath(__file__))
DEST_DIR = os.path.join(DIR, 'data')
TRANSLATE_DIR = os.path.join(DEST_DIR, 'translate_cache.json')
IMAGES_DIR = os.path.join(DEST_DIR, 'images_urls.json')

record = Recorder(loadJson(TRANSLATE_DIR))


args = sys.argv[1:]

do_all = (len(sys.argv) == 1) or 'all' in args

do_characters = do_all or 'characters' in args
do_weapons    = do_all or 'weapons'    in args
do_artifacts  = do_all or 'artifacts'  in args

do_exp = do_characters or do_weapons or do_artifacts or 'exp'       in args
do_ascension_materials = do_characters or do_weapons or 'materials' in args
do_currency = do_exp or 'currency' in args

do_domains = do_ascension_materials or 'domains' in args

do_wings   = do_all or 'wings'   in args
do_gadgets = do_all or 'gadgets' in args

do_recipes = do_all or 'recipes' in args
do_potions = do_all or 'potions' in args

do_fishes      = do_recipes               or 'fish'        in args
do_ingredients = do_recipes or do_potions or 'ingredients' in args


if do_currency :
	link = 'https://genshin.honeyhunterworld.com/db/item/currency/?lang=EN'
	data = readAllItems(link, record)
	saveJson(os.path.join(DEST_DIR, f"currencies.json"), data)


if do_exp :
	exp_pages = {
		'character-exp-material': 'characters',
		'weapon-exp-material':    'weapons',
		'artifact-exp-material':  'artifacts'
	}

	data = {}
	for page, name in exp_pages.items() :
		link = f"https://genshin.honeyhunterworld.com/db/item/{page}/?lang=EN"
		data[name] = readExpMaterials(link, record)
	saveJson(os.path.join(DEST_DIR, f"exp/materials.json"), data)


if do_ascension_materials :
	ascension_material_pages = {
		'character-ascension-material-jewel':              'jewels',
		'character-ascension-material-elemental-stone':    'boss_materials',
		'character-ascension-material-secondary-material': 'common_materials',
		'character-ascension-material-local-material':     'local_materials',
		'talent-level-up-material':                        'talent_materials',
		'weapon-ascension-material-primary':               'weapon_primary',
		'weapon-ascension-material-secondary-material':    'weapon_secondary'
	}

	data = {}
	for page, name in ascension_material_pages.items() :
		link = f"https://genshin.honeyhunterworld.com/db/item/{page}/?lang=EN"
		data[name] = readAllItems(link, record)
		fix.apply(data[name], record, name)
	saveJson(os.path.join(DEST_DIR, f"ascension_materials.json"), data)


if do_artifacts :
	link = 'https://genshin.honeyhunterworld.com/db/artifact/?lang=EN'
	data = readAllArtifacts(link, record)
	saveJson(os.path.join(DEST_DIR, f"artifacts.json"), data)


if do_weapons :
	for weapon in ['sword', 'polearm', 'claymore', 'bow', 'catalyst'] :
		link = f"https://genshin.honeyhunterworld.com/db/weapon/{weapon}/?lang=EN"
		data = readAllWeapons(link, record)
		saveJson(os.path.join(DEST_DIR, f"weapons/{weapon}.json"), data)


if do_characters :
	soup = readToSoup('https://genshin.honeyhunterworld.com/db/char/characters/?lang=EN')
	chars = soup.select('div.char_sea_cont')
	for link in [BASE_URL + c.select_one('a')['href'] for c in chars] :
		data = getCharacterInfo(link, record)
		char_id = idFromName(data['name'])
		if char_id == 'traveler' :
			char_id = link.split('/')[-2]
		fix.apply(data, record, char_id)
		record.images.popCharacter(char_id)
		saveJson(os.path.join(DEST_DIR, f"characters/{char_id}.json"), data)


"""
link = 'https://genshin.honeyhunterworld.com/db/item/glider/?lang=EN'
data = readAllItems(link, record)
print(data)
# TODO save

link = 'https://genshin.honeyhunterworld.com/db/item/ingredients/?lang=EN'
data = readAllItems(link, record)
print(data)
# TODO save

link = 'https://genshin.honeyhunterworld.com/db/item/fish/?lang=EN'
data = readAllItems(link, record)
print(data)
# TODO save

gadget_pages = {
	'gadget':  'gadget',
	'event':   'event-gadgets',
	'fishing': 'fishing_rod'
}

data = {}
for name, page in gadget_pages.items() :
	link = f"https://genshin.honeyhunterworld.com/db/item/{page}/?lang=EN"
	data[name] = readAllItems(link, record)
	print(data[name])
# TODO save

"""

"""
https://genshin.honeyhunterworld.com/db/domains/?lang=EN

link = "https://genshin.honeyhunterworld.com/db/item/potions/?lang=EN"

https://genshin.honeyhunterworld.com/db/crafting-recipes-cooking/?lang=EN
https://genshin.honeyhunterworld.com/db/crafting-recipes-processing/?lang=EN

	if 'items' in sys.argv or everything :
		for page, name in [('ingredients', 'ingredients'), ('gadget', 'gadgets'), ('event-items', 'event'), ('currency', 'currency'), ('glider', 'gliders')] :
			link = "https://genshin.honeyhunterworld.com/db/item/" + page + "/"
			print("[GenshinDL] PARSE " + link)
			soup = readToSoup(link)
			data = readAllItems(soup)
			saveJson(data, dir + "/json/items/" + name + ".json")
	
	if 'ascension' in sys.argv or everything :
		data = {}
		for page, name in [('character-ascension-material-jewel', 'jewels'), ('character-ascension-material-elemental-stone', 'boss_materials'), ('character-ascension-material-secondary-material', 'common_materials'), ('character-ascension-material-local-material', 'local_materials'), ('talent-level-up-material', 'talent_materials'), ('weapon-ascension-material-primary', 'weapon_primary'), ('weapon-ascension-material-secondary-material', 'weapon_secondary')] :
			link = "https://genshin.honeyhunterworld.com/db/item/" + page + "/"
			print("[GenshinDL] PARSE " + link)
			soup = readToSoup(link)
			data[name] = readAllItems(soup)
		saveJson(data, dir + "/json/ascension_materials.json")
	
	if 'potions' in sys.argv or everything :
		link = 'https://genshin.honeyhunterworld.com/db/item/potions/'
		print("[GenshinDL] PARSE " + link)
		soup = readToSoup(link)
		data = readAllPotions(soup)
		saveJson(data, dir + "/json/items/potions.json")
	
	if 'cooking' in sys.argv or everything :
		link = 'https://genshin.honeyhunterworld.com/db/crafting-recipes-cooking/'
		print("[GenshinDL] PARSE " + link)
		data = readAllFoods(readToSoup(link))
		saveJson(data, dir + "/json/food.json")
	
	if 'crafting' in sys.argv or everything :
		data = {}
		for page, name in [('crafting-recipes-smithing', 'smithing'), ('crafting-recipes-alchemy', 'alchemy'), ('crafting-recipes-cooking', 'cooking'), ('crafting-recipes-processing', 'food-processing'), ('crafting-recipes-furniture', 'homeworld')] :
			link = "https://genshin.honeyhunterworld.com/db/" + page + "/"
			print("[GenshinDL] PARSE " + link)
			soup = readToSoup(link)
			data[name] =  readAllRecipes(soup)
		saveJson(data, dir + "/json/recipes.json")
	
	if 'books' in sys.argv or everything :
		if soup == None :
			soup = readToSoup('https://genshin.honeyhunterworld.com/')
		menu = soup.select_one('#custom_html-2 > div > div:nth-child(7)')
		data = {}
		for a in menu.select('a') :
			link = "https://genshin.honeyhunterworld.com" + getRef(a)
			print("[GenshinDL] PARSE " + link)
			data[getIdentifier(a['href'])] = readAllBooks(readToSoup(link))
		saveJson(data, dir + "/json/items/books.json")
"""

record.translate.saveIfModified(TRANSLATE_DIR)
record.images.save(IMAGES_DIR)
