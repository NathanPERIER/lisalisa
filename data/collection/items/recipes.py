
from utils import loadJson, idFromName
from constants import COOKING_RECIPES_JSON, SPECIAL_DISHES_JSON
from translate.textmap import lang
from translate.mhy import mhy_items, mhy_recipes
from items.dataobj import Dish
from characters.dataobj import CharSpecialDish
from common.ascensions import formatCosts
from items import items, readItem

import logging
from enum import Enum

logger = logging.getLogger(__name__)

recipes = loadJson(COOKING_RECIPES_JSON)
special_dishes = loadJson(SPECIAL_DISHES_JSON)

class CookingMethod(Enum) :
	COOK_METHOD_BAKE  = 'bake'
	COOK_METHOD_BOIL  = 'boil'
	COOK_METHOD_FRY   = 'fry'
	COOK_METHOD_STEAM = 'steam'

class FoodType(Enum) :
	COOK_FOOD_ATTACK   = 'attack'
	COOK_FOOD_DEFENSE  = 'defense'
	COOK_FOOD_HEAL     = 'heal'
	COOK_FOOD_FUNCTION = 'stamina'


def readRecipes() -> dict :
	res = {}
	for data in recipes :
		recipe = __g_readRecipe(data)
		identifier = idFromName(recipe['name'])
		mhy_recipes[recipe['hoyo_id']] = identifier
		res[identifier] = recipe
	return res

def __g_readRecipe(recipe: dict) -> dict :
	res = {
		'hoyo_id': recipe['id'],
		'name_hash': recipe['nameTextMapHash'],
		'desc_hash': recipe['descTextMapHash'],
		'rarity': recipe['rankLevel'],
		'type': FoodType[recipe['foodType']],
		'cook_method': CookingMethod[recipe['cookMethod']],
		'proficiency': recipe['maxProficiency']
	}
	res['name'] = lang(res['name_hash'])
	res['desc'] = lang(res['desc_hash'])
	ingredients = {
		x['id']: x['count']
		for x in recipe['inputVec']
		if 'id' in x and 'count' in x
	}
	res['ingredients'] = formatCosts(ingredients, 0)
	res['dishes'] = [__g_readDish(d) for d in recipe['qualityOutputVec']]
	return res
		

# Reads the special dish of a character if there is one
# (dish with an additional property : original recipe)
def readSpecialDish(char_hoyo_id: int) -> CharSpecialDish :
	search_dish = [
		x for x in special_dishes
		if x['avatarId'] == char_hoyo_id and x['bonusType'] == 'COOK_BONUS_REPLACE'
	]
	if len(search_dish) == 0 :
		return None
	if len(search_dish) > 1 :
		logger.warning("Character %d has %d special dish entries (expected one)", char_hoyo_id, len(search_dish))
	dish = search_dish[0]
	res = CharSpecialDish.fromDish(
		__g_readDish({'id': dish['paramVec'][0], 'count': 1})
	)
	if dish['paramVec'][1] != 0 :
		logger.info("Second value of paramVec of character %d special dish is non-zero value %d",
						char_hoyo_id, dish['paramVec'][1])
	res.original_recipe = mhy_recipes[dish['recipeId']]
	return res


# Reads a dish (special item with additional properties)
def __g_readDish(dish: "dict[str,int]") -> Dish :
	data = items[dish['id']]
	item = readItem(data)
	res = Dish.fromItem(item)
	res.count = dish['count']
	res.effect_hash = data['effectDescTextMapHash']
	res.effect = lang(res.effect_hash)
	identifier = idFromName(res.name)
	mhy_items[res.hoyo_id] = identifier
	return item
