# coding:UTF-8

#sysモジュールをimport
import sys

# 標準入力をlineに入れながらfor文をまわし,"拡散希望"が含まれていたら出力
for line in sys.stdin:
    if "拡散希望" in line:
    	print line,
    