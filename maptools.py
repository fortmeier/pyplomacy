from elements import *

spain = Territory("Spain", "spn" )
portu = Territory("Portugal", "ptg", -5, 0)
midat = Territory("Mid-Atlantic", "mid", -5, 5)

territories = [spain, portu, midat]

graph = { (spain,portu): "all", (spain,midat) : "fleets" }

occupations = {}
units = { spain: Unit("p1"), portu: Unit("p2")}



def loadMap():
	return (territories, graph, units, occupations)

def getConnection( g, A, B ):
	if (A,B) in g:
		return g[A,B]
	elif (B,A) in g:
		return g[B,A]
	else:
		return False 
