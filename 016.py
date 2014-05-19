#coding:utf-8

#import
import sys,re

#実際にこんなのが取れました→ 拡張現実(AR)
tweet = re.compile(u"([一-龠]+)\(([A-Z]+)\)")


for line in sys.stdin:
	line_u = unicode(line, "utf-8")
	match_tweet = re.match(tweet,line_u)
	if match_tweet:
		#実際の出力例: 拡張現実	AR
		print match_tweet.group(1)+"\t"+match_tweet.group(2)
		
		
		




