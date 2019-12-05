def setDict(arrOne):
	wireX = dict()
	wireY = dict()
	curX = 0
	curY = 0
	for cmd in arrOne:
		direction = cmd[0]
		val = int(cmd[1:])
		if direction == 'R':
			wireX[curY] = {curX : curX + val}
			curX += val
		elif direction == 'L':
			wireX[curY] = {curX - val : curX}
			curX -= val
		elif direction == 'U':
			wireY[curX] = {curY : curY + val}
			curY += val
		else:
			wireY[curX] = {curY - val : curY}
			curY -= val
	return (wireX, wireY)

def crossCheck(x, y, table, crosses):
	if (x in table):
		d = table[x]
		for key, value in d.items():
			if key <= y and value >= y:
				# print(x, y, table)
				crosses.append(abs(x) + abs(y)) 

def check(arrTwo, wireX, wireY):
	crosses = []
	curX = 0
	curY = 0
	for cmd in arrTwo:
		direction = cmd[0]
		val = int(cmd[1:])
		if direction == 'R':
			for i in range(0, val + 1):
				crossCheck(curX + i, curY, wireY, crosses)
			curX += val
		elif direction == 'L':
			for i in range(0, val + 1):
				crossCheck(curX - i, curY, wireY, crosses)
			curX -= val
		elif direction == 'U':
			for i in range(0, val + 1):
				crossCheck(curY + i, curX, wireX, crosses)
			curY += val
		else:
			for i in range(0, val + 1):
				crossCheck(curY - i, curX, wireX, crosses)
			curY -= val
	list.sort(crosses)
	print(crosses)

def main():
	f = open('d03.txt', 'r')
	wireOne = f.readline()
	wireTwo = f.readline()
	arrOne = wireOne.split(',')
	arrTwo = wireTwo.split(',')
	(wireX, wireY) = setDict(arrOne)
	check(arrTwo, wireX, wireY)
	f.close

main()

	