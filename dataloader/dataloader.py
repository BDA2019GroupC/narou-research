from narouresearch.utils.io_util import get_all_path
import random

class DataLoader:
    def __init__(self, path, validation_split=0.0, seed=0, extention=[], exception=[], strip_one=False, shuffle=False):
        self.path = path
        self.validation_split = validation_split
        self.extention = extention
        self.exception = exception
        self.seed = seed
        self.strip_one = strip_one
        self.shuffle = shuffle

    def get_generator(self, mode="training"):
        random.seed(self.seed)
        if mode not in ["training", "validation"]: 
            raise Exception("mode must be training or validation.")
        for path in get_all_path(self.path, self.extention, self.exception, shuffle=self.shuffle):
            with open(path) as f:
                if self.strip_one: f.readline()
                for line in f:
                    rand = random.random()
                    if mode == "training" and rand < self.validation_split:
                        continue

                    if mode == "validation" and rand >= self.validation_split:
                        continue

                    yield path, line.rstrip()

class LengthDataLoader(DataLoader):
    def get_generator(self, length, mode="training"):
        random.seed(self.seed)
        if mode not in ["training", "validation"]: 
            raise Exception("mode must be \"training\" or \"validation\".")
        for path in get_path_by_length(self.path, self.extention, self.exception, shuffle=self.shuffle):
            with open(path) as f:
                if self.strip_one: f.readline()
                for line in f:
                    rand = random.random()
                    if mode == "training" and rand < self.validation_split:
                        continue

                    if mode == "validation" and rand >= self.validation_split:
                        continue

                    yield path, line.rstrip()

class LengthDataLoaderTwoDomain:
    def __init__(self, paths, validation_split=0.0, seed=0, extention=[], exception=[], strip_ones=(False,False), shuffle=False):
        if typeof(paths) != tuple: raise Exception("paths must be tuple")
        if typeof(strip_ones) != tuple: raise Exception("strip_one must be tuple")
        self.LDLs = [LengthDataLoader(path[i],validation_split,seed,extention,exception,strip_ones[i],shuffle) for i in range(2)]

    def get_generator(self, length, mode="training"):
        if mode not in ["training", "validation"]: 
            raise Exception("mode must be \"training\" or \"validation\".")

        generators = [self.LDLs[i].get_generator(length,mode) for i in range(2)]
        existFlag = [True, True]
        while sum(endFlag) > 0:
            for i in range(2):
                if random.random() < 0.5:
                    try:
                        yield generators[i].__next__()
                    except StopIteration: existFlag[i] = False