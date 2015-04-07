def processGame( gamestate, orders ):
	print "Orders given: " + str(orders)

	struggles = {}

	# implicit holds ??? and possible bounce
	for unit in gamestate.units:
		struggles[unit.territory] = {unit.territory: 1}


	for move in orders["moves"]:
		# TODO check for valid move
		if not move["target"] in struggles:
			struggles[move["target"]] = {}
		struggles[move["target"]][move["origin"]] = 1

	print struggles

	# todo add processing of supports here

	winner_found = True

	while winner_found:
		winner_found = False
		for target, struggle in struggles.iteritems():
			strengths = struggle.values()
			max_strength = max(strengths)
			if strengths.count(max_strength) == 1:
				origin = sorted(struggle.items(), key=lambda x: x[1], reverse=True)[0][0]
				print "orig: ", origin, "target:", target
				if origin == target:
					continue
				winner_found = True
				print "STRUGGLES: ",struggles

				struggles[origin][origin] -= 1
				gamestate.getUnitAt(origin).territory = target
				del struggles[target]
				break




