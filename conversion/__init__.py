from conversion import *
from conversion.conversion_list import *
import os
list = create_char_range_list()
pwd = __file__[:-11]+"convert.py" #実行ディレクトリの絶対パス取ってくる
f = open(pwd+"convert.py", "w")
f.close()
print_if_sentence_char2ID(pwd+"convert.py",list)
print_if_sentence_ID2char(pwd+"convert.py",list)
