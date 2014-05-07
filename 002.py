import re
print re.compile("\t").sub(" ",file("./address.txt","r").read())
