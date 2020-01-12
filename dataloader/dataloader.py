from narouresearch.utils.io_util import get_all_path, get_path_by_length
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
        for path in get_path_by_length(self.path, length, self.extention, self.exception, shuffle=self.shuffle):
            with open(path) as f:
                if self.strip_one: f.readline()
                for line in f:
                    rand = random.random()
                    if mode == "training" and rand < self.validation_split:
                        continue

                    if mode == "validation" and rand >= self.validation_split:
                        continue

                    yield path, line.rstrip()

class LengthDataLoaderMultiDomain:
    def __init__(self, domainVolume, paths, validation_split=0.0, seed=0, extention=[], exception=[], strip_ones=None, shuffle=False, labels=None):
        if len(paths) != domainVolume: 
            raise Exception("paths length must be the same value of domainVolume")
        if strip_ones is None: strip_ones = tuple(False for _ in range(domainVolume))
        if len(strip_ones) != domainVolume: 
            raise Exception("strip_ones length must be the same value of domainVolume")
        if labels is not None and len(labels) != domainVolume:
            raise Exception("labels length must be the same value of domainVolume")

        self.labels = labels
        self.LDLs = [LengthDataLoader(paths[i],validation_split,seed,extention,exception,strip_ones[i],shuffle) for i in range(domainVolume)]
        self.domainVolume = domainVolume

    def get_generator(self, length, mode="training"):
        if mode not in ["training", "validation"]: 
            raise Exception("mode must be \"training\" or \"validation\".")

        generators = [self.LDLs[i].get_generator(length,mode) for i in range(self.domainVolume)]
        existFlag = [True for _ in range(self.domainVolume)]
        while sum(existFlag) > 0:
            domain = random.randint(0,self.domainVolume-1)
            try:
                ret = generators[domain].__next__()
                if self.labels is not None:
                    ret = tuple([self.labels[domain]]+[e for e in ret])
                yield ret
            except StopIteration: existFlag[domain] = False

def BatchDataLoaderWrapper(generator, max_batch_size, only_sentence=False):
    while True:
        ret_list = []
        for i in range(max_batch_size):
            try:
                if only_sentence:
                    ret_list.append(generator.__next__()[1])
                else:  
                    ret_list.append(generator.__next__())
            except StopIteration:
                break
        if len(ret_list) == 0: break
        yield ret_list

class RandomLengthBatchDataLoaderMultiDomain:
    def __init__(self, paths, min_len, max_len, max_batch_size,
            validation_split=0.0, seed=0, extention=[], exception=[], 
            strip_ones=None, shuffle=False, labels=None):

        if labels is None: labels = range(len(paths))
        self.range_len = max_len - min_len + 1
        self.seed = seed
        LDLMD = LengthDataLoaderMultiDomain(len(paths), paths, validation_split, seed, extention, exception, strip_ones, shuffle, labels)
        self.generators = [BatchDataLoaderWrapper(LDLMD.get_generator(i, mode), max_batch_size) for i in range(min_len, max_len+1)]

    def get_generator(self, mode="training"):
        random.seed(self.seed)
        existFlag = [True for _ in self.range_len]
        while sum(existFlag) > 0:
          selected_len = random.randint(0, self.range_len-1)
          try:
            yield self.generators[selected_len].__next__()
          except StopIteration:
            existFlag[selected_len] = False