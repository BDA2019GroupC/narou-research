def get_all_path(rootpath, extention=[], exception=[], absolute=False):
    import os
    rootpath = rootpath.rstrip('/')
    files = os.listdir(rootpath)
        
    for file in files:
        if file in exception: continue
        
        joinedpath = os.path.join(rootpath, file)
        if os.path.isdir(joinedpath):
            for path in get_all_path(joinedpath, extention, exception, absolute):
                yield path
        else:
            ext = file.split('.')[-1]
            if len(extention) is 0 or ext in extention:
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