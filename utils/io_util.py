import os
import random

def detect_encoding(file):
    from chardet.universaldetector import UniversalDetector
    det = UniversalDetector()
    with open(file,'rb') as f:
        for bin in f:
            det.feed(bin)
            if det.done : break
            det.close()
    return det.result["encoding"]

def get_all_path(rootpath, extention=[], exception=[], absolute=False, shuffle=False, seed=0, randobj=None, init=True):
    if init: randobj = random.Random(seed)
    rootpath = rootpath.rstrip('/')
    files = os.listdir(rootpath)
        
    if shuffle: randobj.shuffle(files)
    for file in files:
        if file in exception: continue
        
        joinedpath = os.path.join(rootpath, file)
        if os.path.isdir(joinedpath):
            for path in get_all_path(joinedpath, extention, exception, absolute, shuffle, seed, randobj, init=False):
                yield path
        else:
            ext = file.split('.')[-1]
            if len(extention) == 0 or ext in extention:
                yield joinedpath

def get_path_valiations(rootpath, length=None, path_limit_rate=None, extention=[], exception=[], absolute=False, shuffle=False, seed=0, randobj=None, init=True):
    if init: randobj = random.Random(seed)
    rootpath = rootpath.rstrip('/')
    files = os.listdir(rootpath)
    if length is not None and len(files)!=0 and '.txt' in files[0]:
        if '{}.txt'.format(length) in files: files = ['{}.txt'.format(length)]
        else: return
    if shuffle: randobj.shuffle(files)
    for file in files:
        if file in exception: continue
        joinedpath = os.path.join(rootpath, file)

        if path_limit_rate is not None:
            if os.path.isdir(joinedpath):
                if randobj.random() > path_limit_rate: continue
        
        if os.path.isdir(joinedpath):
            for path in get_path_valiations(joinedpath, length, path_limit_rate, extention, exception, absolute, shuffle, seed, randobj, init=False):
                yield path
        else:
            ext = file.split('.')[-1]
            if len(extention) == 0 or ext in extention:
                yield joinedpath

def get_workpath(rootpath, path_limit_rate=None, exception=[]):
    pathlist = []
    for i,(pathname, dirnames, filenames) in enumerate(os.walk(rootpath)):
        if len(filenames) > 0 and '.txt' in filenames[0]:
            if pathname in exception: continue
            pathlist.append(pathname)
    return pathlist