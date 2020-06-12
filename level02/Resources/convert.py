import sys

#words = []

#for arg in sys.argv[1:]:
#	words.append(arg)
#out = ''

#for w in words:	
#	for i in range(16, 0, -2):
#		out += chr(int('0x' + w[i-2:i], 16))

#print(out)

## ou la version plus rigolote

print ''.join([''.join([chr(int('0x'+o, 16)) for o in [k[i:i+2] for i in range(0, 16, 2)][::-1]]) for k in sys.argv[1:]])

