#coding : UTF-8
#アプローチ:defaultdict関数の引数をintにすることで要素の数え上げをする.

from collections import defaultdict #collectionsモジュールからdefaultdictをインポート.

# default関数がint()を呼んでデフォルトのカウント0を生成し,インクリメント操作が数え上げる.
words = defaultdict(int)
for word in open("./col2.txt", "r"):
    words[word] += 1

#dict型をvalue値でソートしたいので,lambda式を使う.
for k,v in sorted(words.items(),key=lambda x:x[1],reverse = True):
	print str(k).strip("\n") +":" + str(v)
