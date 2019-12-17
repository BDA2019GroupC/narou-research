from conversion import *
from conversion.conversion_list import *
import os
list = create_char_range_list()
now = os.getcwd() #実行ディレクトリの絶対パス取ってくる
pwd = now + "/conversion/"
f = open(pwd+"convert.py", "w")
f.close()
print_if_sentence_char2ID(pwd+"convert.py",list)
print_if_sentence_ID2char(pwd+"convert.py",list)
