a = raw_input()
aa = a.split()
qtd = int( aa[0] )

for i in range( int( aa[1] ) ):
	b = raw_input()
	if b == "fechou":
		qtd += 1

	elif b == "clicou":
		qtd -= 1

print qtd