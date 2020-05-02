import pandas as pd
import requests
import time
import sys

strt = int(sys.argv[1])
end = int(sys.argv[2])

pmcdata = pd.read_csv('PMC-ids.csv')
pmcid_full= pmcdata['PMCID']
data_type = 'PMC'
pmcid = pmcdata['PMCID'].str[3:]

pmcid_list = pmcid[strt:end]

url_1 = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='
#url_2 = '&tool=my_tool&email=my_email@example.com'
full_url = url_1+pmcid_list
#+url_2

for i in full_url.index.values:
    response = requests.get(full_url[i])
    with open(data_type+pmcid_list[i]+'.xml', 'wb') as file:
        file.write(response.content)
    file.close()
    time.sleep(1.5)
