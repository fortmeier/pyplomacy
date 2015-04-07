import maptools
import logic
import sys
import elements

def test_move():
	territories, borders, units, occupations = maptools.loadMapJSON('europe.json')

	gamestate = elements.GameState( territories, units, borders, occupations )

	orders = { "moves" : [{"nation": "France", "origin":"Par", "target":"Gas", "mod":False}] }

	assert gamestate.getUnitAt("Par") 

	logic.processGame( gamestate, orders )

	assert not gamestate.getUnitAt("Par") 
	assert gamestate.getUnitAt("Gas") 

def test_bounce():
	territories, borders, units, occupations = maptools.loadMapJSON('europe.json')

	gamestate = elements.GameState( territories, units, borders, occupations )

	orders = { "moves" : [{"nation": "France", "origin":"Par", "target":"Gas", "mod":False}, 
						  {"nation": "France", "origin":"Mar", "target":"Gas"}] }
	assert gamestate.getUnitAt("Par") 
	assert gamestate.getUnitAt("Mar") 

	logic.processGame( gamestate, orders )

	assert not gamestate.getUnitAt("Gas") 
	assert gamestate.getUnitAt("Mar") 
	assert gamestate.getUnitAt("Par") 

