#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def plotTerritories( g, terr ):
	x = [t.x for t in terr]
	y = [t.y for t in terr]
	names = [t.name for t in terr]
	plt.scatter(x,y)
	for t in terr:
		plt.annotate( t.name, (t.x, t.y))
	print names

def plotBorders( g, terr ):
	for A,B in g:
		c = 'black'
		if g[A,B] == "fleets":
			c = 'blue'
		elif g[A,B] == "armies":
			c = 'brown'

		plt.plot([A.x, B.x], [A.y, B.y], color=c)

def plotUnits( g, u ):

	print u
		

def plotMap( g, terr, units ):
	plotTerritories( g, terr )
	plotBorders( g, terr )
	plotUnits( g, units )
	plt.show()