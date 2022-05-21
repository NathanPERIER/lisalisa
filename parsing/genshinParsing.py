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
from parsing.wishes import fetchWishes

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

do_domains = do_ascension_materials or 'domains' in args # TODO

do_wishes = do_all or 'wishes' in args

do_wings   = do_all or 'wings'   in args
do_gadgets = do_all or 'gadgets' in args # TODO

do_recipes     = do_all     or 'recipes'     in args # TODO
do_ingredients = do_recipes or 'ingredients' in args

# maybe also https://genshin.honeyhunterworld.com/db/item/event-currency-items/?lang=EN
if do_currency :
	link = 'https://genshin.honeyhunterworld.com/db/item/currency/?lang=EN'
	data = readAllItems(link, record)
	saveJson(os.path.join(DEST_DIR, 'currencies.json'), data)


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
	saveJson(os.path.join(DEST_DIR, 'exp/materials.json'), data)


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
	saveJson(os.path.join(DEST_DIR, 'ascension_materials.json'), data)


if do_artifacts :
	link = 'https://genshin.honeyhunterworld.com/db/artifact/?lang=EN'
	data = readAllArtifacts(link, record)
	saveJson(os.path.join(DEST_DIR, 'artifacts.json'), data)


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


if do_wishes :
	genshinWishes, moe = fetchWishes()
	saveJson(os.path.join(DEST_DIR, 'wish_stats/gw.json'), genshinWishes)
	saveJson(os.path.join(DEST_DIR, 'wish_stats/moe.json'), moe)


if do_wings :
	link = 'https://genshin.honeyhunterworld.com/db/item/glider/?lang=EN'
	data = readAllItems(link, record)
	saveJson(os.path.join(DEST_DIR, 'wings.json'), data)

if do_ingredients :
	link = 'https://genshin.honeyhunterworld.com/db/item/ingredients/?lang=EN'
	data = readAllItems(link, record)
	saveJson(os.path.join(DEST_DIR, 'ingredients.json'), data)

"""

link = 'https://genshin.honeyhunterworld.com/db/item/namecard/?lang=EN'
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

https://genshin.honeyhunterworld.com/db/crafting-recipes-cooking/?lang=EN

https://genshin.honeyhunterworld.com/db/domains/?lang=EN

"""

record.translate.saveIfModified(TRANSLATE_DIR)
record.images.save(IMAGES_DIR)
