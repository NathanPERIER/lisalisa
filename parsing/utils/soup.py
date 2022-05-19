import re
import bs4
from lxml import etree
import logging

logger = logging.getLogger('parsing.utils')


def getRef(a) :
	return a['href']


def firstGroup(reg, s) :
	return reg.match(s).group(1)


# Gets the name used to identify an object in the database from a link
item_name = re.compile(r'^.*/([^?][^/]+)/?(?:\?[^/]*)?$')
def idFromLink(a) :
	if type(a) == bs4.element.Tag :
		a = getRef(a)
	return item_name.match(a).group(1)

# reads the id of an item contained in an image name
image_item = re.compile(r".*/(\w+?)(?:_\d{2})?.png")
def idFromImage(img) :
	return image_item.match(img['data-src']).group(1)

filter_reg = re.compile('[^a-zA-Z0-9]+')
def idFromName(name) :
	return filter_reg.sub('_', name.replace('\'', '').lower())


# Retrieves the text content of an HTML tag
def getTagContent(tag) :
	return str(tag.string)

def extractText(tags: "list[bs4.element.Tag]") :
	res = []
	for tag in tags :
		if type(tag) == bs4.element.NavigableString :
			res.append(getTagContent(tag))
		elif tag.name == 'br' :
			res.append('\n')
		else :
			res.append(extractText(tag))
	return "".join(res).strip()

def groupByTwo(l) :
	half_size = len(l) // 2
	res_a = [l[2*i] for i in range(half_size)]
	res_b = [l[2*i+1] for i in range(half_size)]
	return list(zip(res_a, res_b))

# Converts an HTML array into a (python) list
def getArray(html) :
	table = etree.HTML(str(html)).find("body/table")
	rows = iter(table)
	res = [[col.text for col in next(rows)]]
	if res[0][0] == None : 
		res[0][0] = ''
	for row in rows :
		res.append([col.text for col in row])
	return res

def getLevelIndexedArray(html) :
	arr = getArray(html)
	if len(arr) < 2 :
		logger.warning('HTML table is empty')
		return None
	desc = [l[0] for l in arr[1:]]
	vals = [[l[i] for l in arr[1:]] for i in range(1,len(arr[0]))]
	return {'desc': desc, 'values': vals}


# Removes the tags wrapping HTML data as text
# For example '<a>bbb</a>' will become 'bbb'
# Also removes the color tags inside the text
# and converts the br tags to line return
remove_wrapper = re.compile(r'^<[^<>]*>(.*)</[^<>]*>$')
def removeWrapper(html) : 
	res = str(html).replace('<color>', '').replace('</color>', '')
	res = remove_wrapper.match(res).group(1)
	res = res.replace('<br/>', '\\n').replace('\\n ', '\\n')
	return res

# Reads all the items displayed in a certain part of the document (as images)
# and associates them with their count
count_value = re.compile(r"\s?x?(\d*)")
def readItems(line, translate=None) :
	ids = [idFromImage(x) for x in line.select('img.itempic')]
	if translate is not None :
		ids = [translate[x] for x in ids]
	count = [int("0"+count_value.match(x.string).group(1)) for x in line.select('span.asc_amount')]
	return dict(zip(ids, count))


reg_int = re.compile(r"(\d+)(K)?")
reg_float = re.compile(r"(\d+\.\d+)(K)?")
def scanNum(s: str) :
	m = reg_int.fullmatch(s)
	if m is not None :
		res = int(m.group(1))
		if len(m.groups()) > 1 and m.group(2) == 'K':
			res = res * 1000
		return res
	m = reg_float.fullmatch(s)
	if m is not None :
		res = float(m.group(1))
		if len(m.groups()) > 1 and m.group(2) == 'K':
			res = res * 1000
		if res.is_integer() :
			res = int(res)
		return res
	raise ValueError(f"\"{s}\" is not a valid number")


# Reads all the items displayed in a certain part of the document (as images)
# and associates them with their count
def readNewItems(line, translate=None) :
	ids = [idFromImage(x) for x in line.select('img.itempic')]
	if translate is not None :
		ids = [translate[x] for x in ids]
	count = [scanNum(getTagContent(x)) for x in line.select('div.itemstarcontbg_smol')]
	return dict(zip(ids, count))