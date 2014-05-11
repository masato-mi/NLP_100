# coding:UTF-8

# sys,reモジュールをimport
import sys
import re

# 変数
tweet = re.compile(r"[^RT]+RT") # 正規表現:[RT]以外の一回以上の繰り返し


for line in sys.stdin: # 標準入力をlineに入れながらfor文をまわし,
    match_tweet = re.match(tweet, line) #tweetを探しだし
    if match_tweet: #マッチしたら出力
        print match_tweet.group(0)