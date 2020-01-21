import os
from narouresearch.utils.io_util import get_all_path

def createDic(datapath, pathdic=[]):
	for path in get_all_path(datapath):
		tmp = pathdic
		splitlist = path.split("/")
		for i in range(-len(splitlist),-1):
			print(splitlist[i])
		break
			# tmp = tmp[elm]
	# 	dirc = "/".join(path.split("/")[:-1])
	# 	if pathlist[-1] != direc:
	# 		pathlist.append(dirc)
	# return pathlist

def createMultiDomainDic(datapaths):
	pathlist = []
	for datapath in datapaths:
		pathlist = createList(datapath, pathlist)
	return pathlist

def printIfStatementPath2Id(filename, pathlist):
	with open(filename, "a") as f:
		f.write("def path2id(path):\n")
		for i, path in enumerate(pathlist):
			f.write("\tif path=={}:")