import sys

ant = -1
res = 0

while True:
	try:
		value = raw_input()
		v = int( value )
		if v <= ant:
			res = ant + 1
		else:
			ant = v
	except KeyboardInterrupt:
		break
	except (EOFError):
		break

if res == 0:
	res = ant + 1
	
print res