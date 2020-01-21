## For Usage
from narouresearch.utils.data_alignment import data_alignment_by_length

source_rootpath = "Data/aozora_utf8_sentences/"
dest_rootpath = "Data/aozora_sentences_by_length/"
data_alignment_by_length(source_rootpath, dest_rootpath, 2)