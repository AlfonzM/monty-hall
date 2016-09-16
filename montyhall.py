import random

def playMontyHall(switch):
	choices = ['goat', 'goat', 'car']

	random.shuffle(choices)
	pick = choices.pop()

	if switch:
		choices.remove('goat')
		pick = choices.pop()

	if pick == 'car':
		return True

	return False

def loopMontyHalls(iterations, switch):
	winCount = 0

	for i in range(0,iterations):
		winCount += 1 if playMontyHall(switch) else 0

	print "---"
	print "Monty Hall with switch == " + str(switch)
	print "Win Count: " + str(winCount) + "/" + str(iterations)
	print "Win Rate: " + str((winCount*1.0/iterations*1.0) * 100) + "%"

iterations = 100000

# Run monty halls with switch
loopMontyHalls(iterations, True)

# Run monty halls without switching
loopMontyHalls(iterations, False)