class Player:
	name = "None"
	def __init__(self, name):
		self.name=name

class Unit:
	owner = "None"
	utype = "Army"
	def __init__(self, player):
		self.owner = player


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
	modA = "None"
	modB = "None"
	typ = "all"
	def __init__(self, A, B, typ="all", modA="None", modB="None"):
		self.A = A
		self.B = B
		self.modA = modA
		self.modB = modB
		self.type = typ

	def __repr__(self):
		return "< %s -- %s -- %s >" % (self.A.short, self.type, self.B.short)