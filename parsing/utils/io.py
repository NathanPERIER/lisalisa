import json
import bs4
from urllib.request import Request, urlopen
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


def readToSoup(url) :
	logger.info(f"PARSE {url}")
	req = Request(url, headers={'User-Agent': USER_AGENT})
	html_bytes = urlopen(req).read()
	html_doc = html_bytes.decode("utf8")
	return bs4.BeautifulSoup(html_doc, features="lxml")
