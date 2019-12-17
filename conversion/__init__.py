from narouresearch.conversion.conversion_list import *
import os
list = create_char_range_list()
path = __file__[:-11]+"convert.py"
f = open(path, "w")
f.close()
print_if_sentence_char2ID(path,list)
print_if_sentence_ID2char(path,list)
