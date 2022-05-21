
from utils.io import fetchJson

MOE_URL = 'https://api.paimon.moe/wish?banner='
MOE_FIRST_BANNER = 300009
MOE_PERMA_BANNER = 200001

GENSHIN_WISHES_PERMA = 'https://genshin-wishes.com/api/public/stats/PERMANENT'
GENSHIN_WISHES_TEMPO = 'https://genshin-wishes.com/api/public/stats/CHARACTER_EVENT'


def formatGenshinWishes(url: str) :
	data = fetchJson(url)
	return [elt['count']for elt in data['countPerPity5Stars']]

def genshinWishes() :
	return {
		'perma': formatGenshinWishes(GENSHIN_WISHES_PERMA), 
		'tempo': formatGenshinWishes(GENSHIN_WISHES_TEMPO)
	}


def formatMoe(url: str, silent=False) :
	data = fetchJson(url, silent)
	if data is None :
		return None
	counts = data['pityCount']['legendary']
	return counts[1:91]

def tempoMoe() :
	data = formatMoe(f"{MOE_URL}{MOE_FIRST_BANNER}")
	banner = MOE_FIRST_BANNER + 1
	ok = True
	while(ok) :
		cpts = formatMoe(f"{MOE_URL}{banner}", True)
		if cpts is not None :
			for i, c in enumerate(cpts) :
				data[i] += c
			banner += 1
		else :
			ok = False
	return data

def moe() :
	return {
		'perma': formatMoe(f"{MOE_URL}{MOE_PERMA_BANNER}"), 
		'tempo': tempoMoe()
	}


def fetchWishes() :
	return genshinWishes(), moe()
