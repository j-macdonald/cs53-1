import os
import sys
import glob
import multiprocessing as mp
from bs4 import BeautifulSoup


def handleonexmlfile(inpname):
    basename = os.path.basename(inpname).split('.')[0]
    basename_txt = os.path.join(basename+".txt")
    outname = os.path.join("/home/ec2-user/PMC_Data/first_xml_text_files/"+basename+".txt")
    with open(inpname) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        p_data= soup.find_all('p')
        with open(outname, 'a') as out:
            for x in p_data:
                line = x.text
                out.write(line)
        out.close()

        
        
if __name__ == "__main__":
    POOLSIZE  = 6 # number of CPUs
    pool = mp.Pool(POOLSIZE)
    fnames = glob.glob("/home/ec2-user/PMC_Data/oai_xml/PMC*.xml")
    for x in pool.imap_unordered(handleonexmlfile, fnames, 1):
        pass
