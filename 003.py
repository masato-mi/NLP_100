f = open("./address.txt","r")
wpf = open("col1.txt","w");
wps = open("col2.txt","w");
for line in f.readlines():
	line = line.split("\t")
	First = line[0]
	Second = line[1]
	wpf.write(First + "\n")
	wps.write(Second)
f.close()
wpf.close()
wps.close()
	