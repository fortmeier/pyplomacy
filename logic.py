def processGame( gamestate, orders ):
	print "Orders given: " + str(orders)

	struggles = {}

	# implicit holds ??? and possible bounce
	#for unit in gamestate.units:
	#	struggles[unit.territory] = {unit.territory: 1}

	print struggles

	for move in orders["moves"]:
		# TODO check for valid move

		struggles[move["target"]] = {move["origin"]: 1}

	winner_found = True

	while winner_found:
		winner_found = False
		for target, struggle in struggles.iteritems():
			strengths = struggle.items()
			max_strength = max(strengths)
			if strengths.count(max_strength) == 1:
				winner_found = True
				origin = sorted(struggle.items(), key=lambda x: x[1], reverse=True)[0][0]
				print "STRUGGLES: ",struggles
				#struggles[origin][origin] -= 1
				gamestate.getUnitAt(origin).territory = target
				del struggles[target]
				break




