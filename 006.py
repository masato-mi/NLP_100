import sys
N = int(sys.argv[1])
f = open("./address.txt","r")
lines = f.readlines()
lcnt = len(lines)
end = lcnt-1
for num in reversed(range(end,end-N,-1)):
	print lines[num]
f.close()