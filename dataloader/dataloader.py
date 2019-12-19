from narouresearch.utils.io_util import get_all_path
from random import random

class DataLoader:
    def __init__(self, path, validation_split=0.2, extention=[], exception=[]):
        self.path = path
        self.validation_split = validation_split
        self.extention = extention
        self.exception = exception
        self.val_index_tuple = set()
        print("starting appending indices to validation list") ## this must be logger.log
        index = 0
        for path in get_all_path(self.path, self.extention, self.exception):
            with open(path) as f:
                for line in f:
                    if random() < self.validation_split:
                        self.val_index_tuple.add(index)
                    index += 1
        print("finished appending indices to validation list") ## this must be logger.log

    def get_generator(self, mode="training"):
        if mode not in ["training", "validation"]: 
            raise Exception("mode must be training or validation.")
        index = 0
        for path in get_all_path(self.path, self.extention, self.exception):
            with open(path) as f:
                for line in f:
                    if mode == "training" and index in self.val_index_tuple:
                        index += 1
                        continue

                    if mode == "validation" and index not in self.val_index_tuple:
                        index += 1
                        continue

                    index += 1
                    yield line.rstrip()

