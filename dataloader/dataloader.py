from narouresearch.utils.io_util import get_path_valiations
import random

class DataLoader:
    def __init__(self, path, path_limit_rate=1., validation_split=0.0, seed=0, extention=[], exception=[], shuffle=False):
        self.path = path
        self.path_limit_rate = path_limit_rate
        self.validation_split = validation_split
        self.extention = extention
        self.exception = exception
        self.seed = seed
        self.shuffle = shuffle

    def get_generator(self, mode="training"):
        random.seed(self.seed)
        def _generator(length=None):
            if mode not in ["training", "validation"]: raise Exception("mode must be training or validation.")
            for path in get_path_valiations(self.path, length, self.path_limit_rate, self.extention, self.exception, shuffle=self.shuffle):
                with open(path) as f:
                    for line in f:
                        rand = random.random()
                        if mode == "training" and rand < self.validation_split: continue
                        if mode == "validation" and rand >= self.validation_split: continue
                        yield path, line.rstrip()
        return _generator

def GeneratorRandomMixer(generators, labels=None):
    def _generator(length=None):
        if type(generators) not in [list, tuple]: raise Exception("generators must be list or tuple")
        if labels is not None and len(labels) != len(generators): raise Exception("labels size must be the same of generators size")
        domain_size = len(generators)
        existFlag = [True for _ in range(domain_size)]
        selfgen = [generator(length) for generator in generators]
        while sum(existFlag) > 0:
            domain = random.randint(0,domain_size-1)
            try:
                ret = selfgen[domain].__next__()
                if labels is not None: 
                    ret = tuple([labels[domain]]+[e for e in ret])
                yield ret
            except StopIteration: existFlag[domain] = False
    return _generator

def BatchDataGenerator(generator, max_batch_size):
    def _generator(length=None):
        selfgen = generator(length)
        while True:
            ret_list = []
            for i, datum in enumerate(selfgen,1):
                ret_list.append(datum)
                if i >= max_batch_size: break
            if len(ret_list) == 0: break
            yield ret_list
    return _generator

class RandomLengthDataGenerator: # faster than function
    def __init__(self, generator, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len
        self.generators = [generator(length) for length in range(min_len, max_len+1)]

    def __call__(self):
        existFlag = [True for _ in range(self.max_len-self.min_len+1)]
        while sum(existFlag) > 0:
            selected_len = random.randint(0, self.max_len-self.min_len)
            try: yield self.generators[selected_len].__next__()
            except StopIteration: existFlag[selected_len] = False

def RandomLengthDataGenerator_(generator, min_len, max_len): # slower than class
    def _generator():
        generators = [generator(length) for length in range(min_len, max_len+1)]
        max_l = max_len
        min_l = min_len
        existFlag = [True for _ in range(max_l-min_l+1)]
        while sum(existFlag) > 0:
            selected_len = random.randint(0, max_l-min_l)
            try: yield generators[selected_len].__next__()
            except StopIteration: existFlag[selected_len] = False
    return _generator