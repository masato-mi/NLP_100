#cording:UTF-8
d={}
f=open("./address.txt","r")

for line in f.readlines():
	line=line.split("\t")
	k=line[1]
	v=line[0]
	d[k]=v
	#ここまでの流れは(8)と同じ
f.close()
for k,v in sorted(d.items(),reverse = True): # 辞書の逆順にソート
	print v + "\t" + k