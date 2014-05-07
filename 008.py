#cording:UTF-8
d={} #空の辞書を用意.
f=open("./address.txt","r")

for line in f.readlines():
	line=line.split("\t") #タブで１コラム目と２コラム目を区切る.
	k=line[1] #２コラム目をk(Key)に入れる
	v=line[0] #１コラム目をv(Value)に入れる
	d[k]=v　#「２コラム目を辞書順にソート」なので,あえて２コラム目をKeyにしている
f.close()
for k,v in sorted(d.items()): #辞書順にソート
	print v + "\t" + k
	