from narouresearch.utils.io_util import get_all_path
import random

class DataLoader:
    def __init__(self, path, validation_split=0.2, seed=0, extention=[], exception=[]):
        self.path = path
        self.validation_split = validation_split
        self.extention = extention
        self.exception = exception
        self.seed = seed

    def get_generator(self, mode="training"):
        random.seed(self.seed)
        if mode not in ["training", "validation"]: 
            raise Exception("mode must be training or validation.")
        for path in get_all_path(self.path, self.extention, self.exception):
            with open(path) as f:
                for line in f:
                    rand = random.random()
                    if mode == "training" and rand < self.validation_split:
                        continue

                    if mode == "validation" and rand >= self.validation_split:
                        continue

                    yield path, line.rstrip()

