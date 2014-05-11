# coding:UTF-8

# sys,reモジュールをimport
import sys
import re

#　変数
tweet = re.compile("なう$") # 正規表現:なうで終了する

for line in sys.stdin:　# 標準入力をlineに入れながらfor文をまわし,
    match_tweet = re.search(tweet, line) #tweetを探しだし
    if match_tweet: #マッチしたら出力
    	print line,
