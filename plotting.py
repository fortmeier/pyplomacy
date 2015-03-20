#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plotTerritories( borders, terr ):
	x = [t.x for t in terr]
	y = [t.y for t in terr]
	names = [t.name for t in terr]
	plt.scatter(x,y)
	for t in terr:
		plt.annotate( t.name, (t.x, t.y))
	print names

def plotBorders( borders, terr ):
	for A,B in borders:
		c = 'black'
		if borders[A,B].type == 'fleets':
			c = 'blue'
		elif borders[A,B].type == 'armies':
			c = 'brown'

		plt.plot([A.x, B.x], [A.y, B.y], color=c)

def plotUnits( borders, u ):

	print u
		

def plotMap( borders, terr, units ):
	plotTerritories( borders,  terr )
	plotBorders( borders,  terr )
	plotUnits( borders,  units )
	plt.show()