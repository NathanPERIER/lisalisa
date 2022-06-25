#!/usr/bin/python3

from utils import saveJson
from constants import DEST_DIR
from characters import readCharacters, getCharacterCurves
from weapons import readWeapons, getWeaponCurves
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