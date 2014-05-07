import sys
N = int(sys.argv[1])
f = open("./address.txt","r")
lines = f.readlines()
for num in range(0,N):
	print lines[num]
f.close()