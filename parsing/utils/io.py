import json
import bs4
import requests
import logging

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0'

logger = logging.getLogger(__name__)


def loadJson(path) :
	with open(path, 'r') as f :
		data = json.load(f)
	return data

def saveJson(path, data) :
	logger.info(f"SAVE \"{path}\"")
	with open(path, 'w') as f :
		json.dump(data, f, indent='\t')


def fetchJson(url: str, silent=False) :
	r = requests.get(url)
	if r.ok :
		return r.json()
	if silent :
		return None
	raise Exception(f"Request to url {url} returned with code {r.status_code}")


def readToSoup(url) :
	logger.info(f"PARSE {url}")
	r = requests.get(url, headers={'User-Agent': USER_AGENT})
	if not r.ok :
		raise Exception(f"Request to url {url} returned with code {r.status_code}")
	return bs4.BeautifulSoup(r.text, features="lxml")
	
