#!/usr/bin/env python
# coding: utf-8
import io
import glob
from narocessor import Processor

if __name__ == '__main__':
    for path in glob.glob('classified/*/N*.txt'):
        print(path.replace('classified', 'processed'))
        exit()
        fout = open('', 'w')
        fin = open(path, 'r')
        p = Processor(fin, fout)
        p.preprocess()
        fin.close()
        fout.close()
        exit() # only one
