from narouresearch.networks.styleEncoder.worksConversion.createList import *
import os
path = __file__[:-11]+"convert.py"
f = open(path, "w")
f.close()
pathlist = createMultiDomainList(("Data/aozora_length/train","Data/narou_length/train"))
printIfStatementPath2Id(path, pathlist)