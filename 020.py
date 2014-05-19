#coding:utf-8

#import
import sys,re 

#これだと英字の羅列を拾ってしまいます(ex.リンクなど)
emotion = re.compile(u".*([\(\（][^(一-龠|ぁ-ん|ァ-ヴ|@)]*[\)\）]).*")

for line in sys.stdin:
	line_u = unicode(line, "utf-8")
	match_emo = re.match(emotion,line_u)
	if match_emo:
		print match_emo.group(1)
		