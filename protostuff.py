from plotting import *
from elements import *
import maptools
import logic

territories, graph, units, occupations = maptools.loadMap()

spain = territories[0]
portu = territories[1]
midat = territories[2]



p1 = Player("A-Man")
p2 = Player("B-Man")

print graph



print maptools.getConnection( graph, spain, portu )
print maptools.getConnection( graph, portu, spain )
print maptools.getConnection( graph, spain, midat )

settings = { "year": 1901, "season": "spring"}
gamestate = ( territories, units, graph, settings )

orders = {}

logic.processGame( gamestate, orders )


plotMap( graph, territories, units )