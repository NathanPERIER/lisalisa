#!/usr/bin/python3

from utils import saveJson
from constants import DEST_DIR
from characters import readCharacters, getCharacterCurves
from weapons import readWeapons, getWeaponCurves
from artifacts import readArtifactSets, getArtifactCurves
from world.cities  import readCities
from world.domains import readDomains
from exp.adventure_rank import readAdventureRankExp
from exp.character      import readCharacterExp
from exp.friendship     import readFriendshipExp
from exp.offerings      import readOfferingsExp
from exp.weapon         import readWeaponExp
from items.gliders import readGliders
from items.recipes import readRecipes
from items import getAutoTranslated

import os
import logging

logging.basicConfig(level=logging.INFO, format="(%(name)s) [%(levelname)s] %(message)s", datefmt='%d/%m/%Y %H:%M:%S')


def main() :
	gliders = readGliders()
	dest_file = os.path.join(DEST_DIR, 'items/gliders.json')
	saveJson(gliders, dest_file)

	recipes = readRecipes()
	dest_file = os.path.join(DEST_DIR, 'items/recipes.json')
	saveJson(recipes, dest_file)

	cities = readCities()
	dest_file = os.path.join(DEST_DIR, 'cities.json')
	saveJson(cities, dest_file)

	domains = readDomains()
	dest_file = os.path.join(DEST_DIR, 'domains.json')
	saveJson(domains, dest_file)

	ar_exp = readAdventureRankExp()
	dest_file = os.path.join(DEST_DIR, 'exp/adventure_rank.json')
	saveJson(ar_exp, dest_file)

	char_exp = readCharacterExp()
	dest_file = os.path.join(DEST_DIR, 'exp/character.json')
	saveJson(char_exp, dest_file)

	friendship_exp = readFriendshipExp()
	dest_file = os.path.join(DEST_DIR, 'exp/friendship.json')
	saveJson(friendship_exp, dest_file)

	offerings_exp = readOfferingsExp()
	dest_file = os.path.join(DEST_DIR, 'exp/offerings.json')
	saveJson(offerings_exp, dest_file)

	weapon_exp = readWeaponExp()
	dest_file = os.path.join(DEST_DIR, 'exp/weapon.json')
	saveJson(weapon_exp, dest_file)

	art_sets = readArtifactSets()
	dest_file = os.path.join(DEST_DIR, 'artifacts.json')
	saveJson(art_sets, dest_file)

	art_curves = getArtifactCurves()
	dest_file = os.path.join(DEST_DIR, 'curves/artifacts.json')
	saveJson(art_curves, dest_file)

	weapons = readWeapons()
	for weapon_id, weapon in weapons.items() :
		dest_file = os.path.join(DEST_DIR, f"weapons/{weapon_id}.json")
		saveJson(weapon, dest_file)
	
	weapon_curves = getWeaponCurves()
	dest_file = os.path.join(DEST_DIR, 'curves/weapons.json')
	saveJson(weapon_curves, dest_file)

	characters = readCharacters()
	for char_id, char in characters.items() :
		dest_file = os.path.join(DEST_DIR, f"characters/{char_id}.json")
		saveJson(char, dest_file)
	
	char_curves = getCharacterCurves()
	dest_file = os.path.join(DEST_DIR, 'curves/characters.json')
	saveJson(char_curves, dest_file)

	items_auto = getAutoTranslated()
	dest_file = os.path.join(DEST_DIR, 'items/auto.json')
	saveJson(items_auto, dest_file)


if __name__ == '__main__' :
	main()