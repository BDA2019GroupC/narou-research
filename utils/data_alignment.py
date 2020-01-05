from narouresearch.dataloader.dataloader import DataLoader
import os

def data_alignment_by_length(from_rootpath, to_rootpath):
	os.mkdirs(rootpath, exist_ok=True)
	dl = DataLoader(path,validation_split=0)
	generator = dl.get_generator()
	for i, sentence in enumerate(generator):
		write_sentence_by_length(to_rootpath, sentence)

def write_sentence_by_length(rootpath,sentence):
	length = str(len(sentence))
	with open(rootpath+'/'+length+'.txt','a') as f:
		f.write(sentence)
		f.write('\n')