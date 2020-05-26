import argparse
from random import randint
parser = argparse.ArgumentParser(description='Win95/NT4 OEM key generator')
parser.add_argument('Number', type=int, help='# of keys')
args = parser.parse_args()
num = args.Number
keys = []
keyappend = ""
print("Working... ")
while(len(keys) != num):
	Part1 = str(randint(1,366))
	Part1A = 3 - len(Part1)
	Part1B = [0]*Part1A
	Part1C = ""
	if(Part1A > 0):
		for f in range(0, Part1A):
			Part1C += str(Part1B[f])
	keyappend += Part1C
	keyappend += str(Part1)
	Part2PRQ = randint(0, 1)
	Part2A, Part2B = "",""
	if Part2PRQ == 0:
		Part2A = str(randint(95,99))
		keyappend = keyappend + Part2A
	if Part2PRQ == 1:
		Part2B = "0" + str(randint(0,2))
		keyappend = keyappend + Part2B
	keyappend += "-OEM-0"
	Part3A = []
	Part3B = 0
	Part3C = 0
	Part3D = ""
	for a in range(0, 5):
		Part3B = randint(0,9)
		Part3C += Part3B
		Part3A.append(Part3B)
	Part3E = 0
	for b in range(0, 6):
		if Part3E < Part3C:
			Part3E = 7*(b+1)
	Part3A.append(Part3E - Part3C)
	Part3F = ""
	for c in range(0,6):Part3F += str(Part3A[c])
	keyappend += Part3F
	keyappend += "-"
	Part4A = str(randint(0,99999))
	Part4B = 5 - len(Part4A)
	Part4C = [0]*Part4B
	Part4D = ""
	if(Part4B > 0):
		for e in range(0, Part4B):
			Part4D += str(Part4C[e])
	keyappend += Part4D
	keyappend += Part4A
	keys.append(keyappend)
	if(Part3A[5] == 8 or Part3A[5] == 9 or Part3A[5] == 0):
		keys.pop()
	print(keyappend, end='\r')
	keyappend = ""
print("Done!                   ")
with open('95Keys.txt', 'w') as filehandle:
	for listitem in keys:
		filehandle.write('%s\n' % listitem)
