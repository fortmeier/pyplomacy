class Player:
	name = "None"
	def __init__(self, name):
		self.name = name

class Unit:
	owner = "None"
	territory = None
	utype = "Army"

	def __init__(self, player, territory, utype="Army"):
		self.owner = player
		self.territory = territory
		self.utype = utype

	def __repr__(self):
		return "<{} at {}>".format(self.utype, self.territory)


class Territory:
	name = "None"
	short = "shrt"
	terrain = "coastal"
	x = 0.0
	y = 0.0
	def __init__(self, name, short, x=0.0, y=0.0):
		self.name = name
		self.short = short
		self.x = x
		self.y = y

	def __repr__(self):
		return "<%s (%s)>" % (self.name, self.short)

class Border:
	A = "None"
	B = "None"
	modA = []
	modB = []
	typ = "all"
	def __init__(self, A, B, typ="all", modA=[], modB=[]):
		self.A = A
		self.B = B
		self.modA = modA
		self.modB = modB
		self.type = typ

	def __repr__(self):
		modAstring = "" if self.modA == [] else self.modA
		modBstring = "" if self.modB == [] else self.modB
		return "< {} -{}- {} -{}- {} >".format(self.A, modAstring, self.type, modBstring, self.B)


class GameState:
	territories = []
	units = []
	borders = []
	occupations = []

	def __init__(self, territories, units, borders, occupations):
		self.territories = territories
		self.units = units
		self.borders = borders
		self.occupations = occupations

	def getUnitAt(self, territory):
		for unit in self.units:
			if unit.territory == territory:
				return unit
		return None
