# coding:UTF-8

# sys,reモジュールをimport
import sys
import re

# 変数
tweet = re.compile(r"^@[a-zA-Z][a-zA-Z0-9]*") #正規表現:ユーザー名

for line in sys.stdin:　# 標準入力をlineに入れながらfor文をまわし,
    mtweet = re.search(tweet, line) #tweetを探しだし
    if mtweet:　#マッチしたら出力
    	print mtweet.group(0)
