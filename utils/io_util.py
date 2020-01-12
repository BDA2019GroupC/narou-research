import os
import random

def get_all_path(rootpath, extention=[], exception=[], absolute=False, shuffle=False, seed=0, init=True):
    if init: random.seed(seed)
    rootpath = rootpath.rstrip('/')
    files = os.listdir(rootpath)
        
    if shuffle: random.shuffle(files)
    for file in files:
        if file in exception: continue
        
        joinedpath = os.path.join(rootpath, file)
        if os.path.isdir(joinedpath):
            for path in get_all_path(joinedpath, extention, exception, absolute, shuffle, init=False):
                yield path
        else:
            ext = file.split('.')[-1]
            if len(extention) == 0 or ext in extention:
                yield joinedpath

def detect_encoding(file):
    from chardet.universaldetector import UniversalDetector
    det = UniversalDetector()
    with open(file,'rb') as f:
        for bin in f:
            det.feed(bin)
            if det.done : break
            det.close()
    return det.result["encoding"]

def get_path_by_length(rootpath, length, extention=[], exception=[], absolute=False, shuffle=False, seed=0, init=True):
    if init: random.seed(seed)
    rootpath = rootpath.rstrip('/')
    files = os.listdir(rootpath)

    if shuffle: random.shuffle(files)
    for file in files:
        if file in exception: continue
        
        joinedpath = os.path.join(rootpath, file)
        if os.path.isdir(joinedpath):
            for path in get_path_by_length(joinedpath, extention, exception, absolute, shuffle, init=False):
                if int(path.split("/")[-1].split('.')[0]) == length:
                    yield path
        else:
            ext = file.split('.')[-1]
            if len(extention) == 0 or ext in extention:
                yield joinedpath