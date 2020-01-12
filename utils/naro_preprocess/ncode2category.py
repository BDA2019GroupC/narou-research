#!/usr/bin/env python
# coding: utf-8
import json
import os
import glob

if __name__ == '__main__':
    ncode = input("Ncode: ")
    path = glob.glob('/content/drive/My Drive/Shared/files/fujiwara_naro_scrape/classified/*/{}.txt'.format(ncode))
    if len(path) == 0:
        print("No such ncode")
    else:
        with open(path[0], 'r') as f:
            meta = json.loads(f.readline())
            print(meta['category'])
