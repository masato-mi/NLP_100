#coding:utf-8
#

#import 
import sys,re

#実際にはこれだと制約が強すぎて一つもヒットしないのでは?
#マッチするはずの文字列:〒123-4567 奈良県 生駒市
address = re.compile(u"(〒?\d{3}-\d{4})\s*[一-龠]{2,3}(都|道|府|県)\s*[一-龠あ-ん]+(市|町|村)")


for line in sys.stdin:
	line_u = unicode(line, "utf-8")
	match_address = re.match(address,line_u)
	if match_address:
		print match_address.group()
		
