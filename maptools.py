from elements import *
import json

spain = Territory("Spain", "spn" )
portu = Territory("Portugal", "ptg", -5, 0)
midat = Territory("Mid-Atlantic", "mid", -5, 5)

territories = [spain, portu, midat]

borders = { (spain,portu): "all", (spain,midat) : "fleets" }

occupations = {}
units = { spain: Unit("p1"), portu: Unit("p2")}



def loadMap():
	return (territories, borders, units, occupations)

def getConnection( g, A, B ):
	if (A,B) in g:
		return g[A,B]
	elif (B,A) in g:
		return g[B,A]
	else:
		return False 

def getTerritory( territories, short ):
	ts = [x for x in territories if x.short == short]
	if len(ts) > 1: return False
	if len(ts) == 0: return False
	return ts[0]

def loadMapJSON( filename ):
	with open( filename ) as data_file:    
		data = json.load(data_file)

	territories = []
	for t in data['territories']:
		newTerritory = Territory(t['name'], t['short'], t['x'], t['y'])
		if 'terrain' in t:
			newTerritory.terrain = t['terrain']
		territories.append( newTerritory )

	print territories

	borders = {}
	for b in data['borders']:
		A = getTerritory( territories, b['A'] )
		B = getTerritory( territories, b['B'] )
		borders[(A,B)] = Border(A,B,b['type'])

	print borders

	return (territories, borders, {}, {})
