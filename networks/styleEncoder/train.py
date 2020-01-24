import os
import time
import random
import numpy as np
import torch
import torch.optim as optim
from narouresearch.networks.styleEncoder.model import StyleDisperser
from narouresearch.dataloader.dataloader import DataLoader
from narouresearch.dataloader.dataloader import GeneratorRandomMixer
from narouresearch.dataloader.dataloader import BatchDataGenerator
from narouresearch.dataloader.dataloader import LengthsDataGenerator
# from narouresearch.networks.char2vec.plot import plot_from_files
from narouresearch.dataloader.dataloader import get_random_sentence_in_work
from narouresearch.utils.io_util import get_workpath

def train(paths, save_dir):

	pathlist = []
	for path in paths: pathlist.append(get_workpath(path))
	for i in range(len(pathlist)): pathlist[i] = (i, pathlist[i])
	random.seed(0)
	train_pathlist = random.sample(int(len(pathlist)*0.9))
	validation_pathlist = [path if path not in train_pathlist for path in pathlist]

	def get_generator(mode="training"):
		def get_paths(length, samerand=(32,32)):
			if mode == "training": plist = train_pathlist
			if mode == "validation": plist = validation_pathlist
	        min_len = 11
    	    max_len = 70
			while True:
				paths = []
				while len(paths) >= samerand[1]+1:
					wid, dirc = random.choice(plist)
					path = os.path.join(dirc,str(length)+".txt")
					if os.path.exists(path): paths.append((wid, path))

				retlist = [(paths[0][0], get_random_sentence_in_work(paths[0][1], samerand[0]))]
				for path in paths[1:]:
					retlist.append((path[0],get_random_sentence_in_work(path[1], 1)))
				yield retlist

	