from narouresearch.dataloader.dataloader import DataLoader
import os
import logging

def data_alignment_by_length(from_rootpath, to_rootpath):
	os.makedirs(to_rootpath, exist_ok=True)
	dl = DataLoader(path,validation_split=0)
	generator = dl.get_generator()
	for i, sentence in enumerate(generator):
		write_sentence_by_length(to_rootpath, sentence)

def write_sentence_by_length(rootpath,sentence):
	length = str(len(sentence))
	with open(rootpath+'/'+length+'.txt','a') as f:
		f.write(sentence)
		f.write('\n')

def split_file_by_sentence_length(root, generator, start=0):
  for j,(tpath,sentence) in enumerate(generator):
      if j < start : continue
      if j % 10000 == 0: 
          logging.info("{} sentences are processed".format(j))

      direc = root+'Data/narou_sentences_by_length/'+'/'.join(tpath.split('/')[-2:]).split(".")[0]
      write_sentence_by_length(direc, sentence)
      logging.debug(str(j),direc,sentence)