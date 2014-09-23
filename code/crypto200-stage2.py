from math import floor
from sys import argv, exit

def decode(myStr):
	strLen = len(myStr)
	max = strLen / 2
	if max < 3:
		max = 30

	for key in range(2,max):
		rows = list()
		counter = 0
		i = 0
		last = 0
		leftover = strLen % key
		minNum = int(floor(float(strLen) / float(key)))
		while i < strLen:
			if counter < leftover:
				i += minNum + 1
			else:
				i += minNum
	
			if i > strLen:
				rows.append(myStr[last:])
			else:
				rows.append(myStr[last:i])

			last = i
			counter += 1
		
		columns = list()
		i = 0
		while i < len(rows):
			j = 0
			for char in rows[i]:
				index = j % len(rows[i])
				if index == len(columns):
					columns.append(char)
				else:
					columns[index] += char
				j += 1

			i += 1

		longStr = "".join(columns)
		if longStr[:10] == "I hope you":
			break

	firstQuote = longStr.find('"') + 1
	return longStr[firstQuote:longStr.find('"', firstQuote)]

if len(argv) < 2:
	print "Usage: %s CIPH_TEXT_FILE" % argv[0]
	exit(-1)
else:
	with open(argv[1], 'r') as myFile:
		ciph = myFile.read()

print(decode(ciph))
