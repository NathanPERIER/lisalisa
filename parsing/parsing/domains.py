#!/usr/bin/python3
from parsing.utils import readToSoup, idFromLink, idFromName, getTagContent, extractText, removeWrapper, getRef
import re


farmable_domains = {
	'Artifacts':                  'artifacts',
	'Weapon Ascension Materials': 'weapon_materials',
	'Talent Level-Up Material':   'talent_materials',
	'Trounce Domains':            'trounce_domains',
}


def readDomain(link, translate) :
	data = {}
	soup = readToSoup(link)
	data['name'] = extractText(soup.select_one('.custom_title'))
	# TODO get other data as well...
	# https://genshin-impact.fandom.com/wiki/Domains
	return data


def getDomainRefs(link) :
	data = {}
	soup = readToSoup(link)
	span = soup.select_one('span.enemy_type')
	span_name = extractText(span)
	span_data = []
	for elem in [x for x in span.next_siblings if x.name == 'a'] :
		span_data.append(getRef(elem))
		next_span = elem.select_one('span.enemy_type')
		if next_span is not None :
			data[span_name] = span_data
			span_data = []
			span_name = extractText(next_span)
	return data


def readAllDomains(link, translate) :
	res = {}
	domains = getDomainRefs(link)
	for category, refs in domains.items() :
		if category in farmable_domains :
			domain_data = {}
			for ref in refs :
				link = "https://genshin.honeyhunterworld.com" + ref
				data = readDomain(link, translate)
				honey_id = idFromLink(link)
				identifier = idFromName(data['name'])
				domain_data[identifier] = data
				translate[honey_id] = identifier
			res[farmable_domains[category]] = domain_data
	return res


