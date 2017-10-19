a = input()
b = input()
c = input()

a1 = a*4 + b*2
b1 = a*2 + c*2
c1 = c*4 + b*2

if a1 <= b1 and a1 <= c1:
	print a1
elif b1 <= a1 and b1 <= c1:
	print b1
else:
	print c1