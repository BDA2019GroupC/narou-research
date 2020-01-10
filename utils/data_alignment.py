from narouresearch.dataloader.dataloader import DataLoader
import os
import logging
import sys

def data_alignment_by_length(source_rootpath, dest_rootpath, depth):
    os.makedirs(dest_rootpath, exist_ok=True)
    dl = DataLoader(source_rootpath)
    generator = dl.get_generator()
    for i, (path, sentence) in enumerate(generator):
        if i%100000==0: print(i)
        logging.info("{} sentences are processed".format(i))
        destdir = dest_rootpath + "/".join(path.split("/")[-depth:]).split(".")[0]+"/"
        os.makedirs(destdir, exist_ok=True)
        write_sentence_by_length(destdir, sentence)
        logging.debug(str(i),dest_rootpath,path,sentence)

def write_sentence_by_length(rootpath,sentence):
    length = str(len(sentence))
    with open(rootpath+length+'.txt','a') as f:
        f.write(sentence)
        f.write('\n')