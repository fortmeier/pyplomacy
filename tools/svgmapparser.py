#!/usr/bin/env python

TERRITORY_TYPES = {'l': "land", 'w': "sea", 's': "neutral"}

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("../maps/images/standard02.svg"))

##### PARSE TERRITORIES #####
territories = []
for g in soup.svg.findAll('g'):
    if g.has_attr('title') and g.findChild('text') and g.polygon:
        territories.append({
            'short': g.findChild('text').text.encode('ascii','ignore'),
            'name': g.get('title'),
            'terrain': TERRITORY_TYPES[g.polygon.get('class')[0]],
            'x': g.findChild('text').get('x'),
            'y': g.findChild('text').get('y')
        })

##### PARSE HOMES AND INITIAL UNITS #####
homes = {}
units = {}
for g in soup.svg.findAll('g'):
    if g.has_attr('title') and g.use and g.use.has_attr('class') and g.use.has_attr('xlink:href'):
        nation = g.use.get('class')[0]
        if '#sc' == g.use.get('xlink:href'):
            if not nation in homes:
                homes[nation] = []
            homes[nation].append(g.get('title'))
        elif '#A' == g.use.get('xlink:href'):
            if not nation in units:
                units[nation] = []
            units[nation].append((g.get('title'), 'A'))
        elif '#F' == g.use.get('xlink:href'):
            if not nation in units:
                units[nation] = []
            units[nation].append((g.get('title'), 'F'))
                                 
        
#print(homes)
#print(units)
for t in territories:
    print(t)

