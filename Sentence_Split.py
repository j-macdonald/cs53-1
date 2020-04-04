#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys
import glob
import nltk.data
import multiprocessing as mp

def handleonetxtfile(inpname):
    basename = os.path.basename(inpname).split('.')[0]
    basename_txt = os.path.join(basename+".txt")
    outname = os.path.join(basename+"_setnence_converted.txt")
    fp = open(basename_txt)
    data = fp.read()
    paragraphs = [p for p in data.split('\n') if p]
    with open(outname, "a") as out:
        for paragraph in paragraphs:
            out.write('\n')
            out.write('\n'.join(tokenizer.tokenize(paragraph)))
            out.write('\n')
    out.close()

    
if __name__ == "__main__":
    POOLSIZE  = 6 # number of CPUs
    pool = mp.Pool(POOLSIZE)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fnames = glob.glob("*.txt")
    for x in pool.imap_unordered(handleonetxtfile, fnames, 1):
        pass

