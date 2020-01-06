#!/usr/bin/env python
# coding: utf-8
import io
import os
import glob
from narocessor import Processor

if __name__ == '__main__':
    for path in glob.glob('classified/*/N*.txt'):
        print(path)
        opath = path.replace('classified', 'processed')
        dirpath = os.path.dirname(opath)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        fout = open(opath, 'w')
        fin = open(path, 'r')
        p = Processor(fin, fout)
        p.preprocess()
        fin.close()
        fout.close()
