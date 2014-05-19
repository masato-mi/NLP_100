#coding:utf-8
#output is ok

#import
import sys
import re

#こんな感じなのが取れました→ 加藤さん、ゴローちゃんなど
nicknames = re.compile(r"[一-龠ぁ-んァ-ヴ]+(さん|氏|ちゃん)")

for line in sys.stdin:
	match_nick = re.match(nicknames,line)
	if match_nick:
		print match_nick.group(0)
		
	