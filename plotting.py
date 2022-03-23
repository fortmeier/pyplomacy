#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from maptools import *

def plotTerritories( borders, terr ):
	x = [t.x for t in terr]
	y = [t.y for t in terr]
	names = [t.name for t in terr]
	plt.scatter(x,y)
	for t in terr:
		c = 'gray'
		style = 'square'
		if t.terrain == "coastal":
			style = 'round'
		elif t.terrain == "sea":
			c = 'blue'
			style = 'round'
		plt.annotate( t.name, (t.x, t.y), 
			horizontalalignment='center', verticalalignment='center',
			bbox=dict(facecolor=c, boxstyle=style))
	print(names)

def plotBorders( borders, terr ):
	for A,B in borders:
		c = 'black'
		if borders[A,B].type == 'fleets':
			c = 'blue'
		elif borders[A,B].type == 'armies':
			c = 'brown'

		Ax = getTerritory(terr, A).x
		Ay = getTerritory(terr, A).y
		Bx = getTerritory(terr, B).x
		By = getTerritory(terr, B).y
		plt.plot([Ax, Bx], [Ay, By], color=c)

def plotUnits( borders, u ):

	print(u)
		

def plotMap( borders, terr, units ):
	plotTerritories( borders,  terr )
	plotBorders( borders,  terr )
	plotUnits( borders,  units )
	plt.show()