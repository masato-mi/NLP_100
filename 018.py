# coding:utf-8

#import 
import sys
import re

#実際にはこんな感じで取れました→　仙台市青葉区
sendaishi = re.compile(r"(仙台市?)((太白|宮城野|若林|青葉|泉)区?)?[^はもで。、]*")

for line in sys.stdin:
	match_sendaishi = re.match(sendaishi,line)
	if match_sendaishi:
		print match_sendaishi.group(0)