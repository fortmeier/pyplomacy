#!/usr/bin/env python

from plotting import *
from elements import *
import maptools
import logic
import sys

#territories, borders, units, occupations = maptools.loadMap()
territories, borders, units, occupations = maptools.loadMapJSON('europe.json')



p1 = Player("A-Man")
p2 = Player("B-Man")

players = [p1, p2]

print borders


settings = { "year": 1901, "season": "spring"}
gamestate = GameState( territories, units, borders, occupations )

orders = { "moves" : [{"nation": "France", "origin":"Par", "target":"Gas", "mod":False}] }

print "--------"
print units

logic.processGame( gamestate, orders )

print units

#plotMap( borders, territories, units )


while False:
	for p in players:
		print "Enter command for "+str(p.name)+":"
		line = sys.stdin.readline()
		if line == "exit\n": break

