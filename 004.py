wtr = open("reunion.txt","w")
for fst,sec in zip(open("./col1.txt","r").readlines(),open("./col2.txt","r").readlines()):
	wtr.write(fst.strip("\n") + "\t"+sec)f
wtr.close()
