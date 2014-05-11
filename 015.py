# coding:UTF-8

# sys,reモジュールをimport
import sys
import re

# 変数
account = re.compile(r"^@[a-zA-Z][a-zA-Z0-9]*") # ユーザ名の正規表現

# 関数の定義
def users(x):
    print '<a href="https://twitter.com/#!/%s">%s</a>' %(x,x)


for line in sys.stdin: # 標準入力をlineに入れながらfor文をまわし,
    match_account = re.findall(account, line) #accountを探し
    if match_account:　#マッチしたら
        map (users, match_account) #map関数を用いて、match_accountを引数としてusers関数を呼び出す