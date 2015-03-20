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
	x = 0.0
	y = 0.0
	def __init__(self, name, short, x=0.0, y=0.0):
		self.name = name
		self.short = short
		self.x = x
		self.y = y

	def __repr__(self):
		return "<%s (%s)>" % (self.name, self.short)