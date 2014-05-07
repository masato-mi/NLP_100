#coding : UTF-8
file = open("address.txt", "r")
new_set = set()
for line in file.readlines(): 
    item = line.split(" ") #１コラム目と２コラム目を１スペースで分けておく.
    new_set.add(item[0]) #１コラム目を集合(new_set)に加える.これより重複がなくなる.
 
print len(new_set),
 
file.close()