a = raw_input()
aa = a.split()
height = int( aa[1] )

for i in range( int( aa[0] ) ):
	b = raw_input()
	c = b.split()

	if int( c[-1] ) > height:
		print b.replace( " " + c[-1], "" )