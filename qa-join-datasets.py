import os
import json

ftypes = {
     'Appended-Snippet':'snippet-2sent.json'
    ,'Full-Abstract':'full-annotated.json'
    ,'Snippet-as-is':'snippet-annotated.json'
}

base_dir = 'f"datasets/QA/BioASQ-{N}b/train/"'
N = 6

j = eval(base_dir)

jsons = {}

tasks = ['list','factoid','yesno']

for task in tasks:
    jsons[task] = {}
    for N in ['6','7']:
        base = eval(base_dir)
        print(base)
        jsons[task][N] = {}
        for ftype in ftypes.keys():
            ifiles = os.listdir(f'{base}{ftype}')
            fname = [f for f in ifiles if task in f][0]
            with open(f'{base}{ftype}/{fname}','r') as infile:
                jsons[task][N][ftype] = json.load(infile)

shared_qs = []


def json_merge(task,N,test_only=False):
    merge_json = {}
    merge_json['data'] = []
    merge_json['version'] = f'BioASQ{N}b'
    merge_json['data'].append({})
    merge_json['data'][0]['title'] = f'BioASQ{N}b'
    merge_json['data'][0]['paragraphs'] = []
    for ftype in  ftypes.keys():
        json_in = jsons[task][N][ftype]
        for ipar in json_in['data'][0]['paragraphs']:
            if test_only and N=='7':
                qid = ipar['qas'][0]['id']
                if qid not in shared_qs:
                    merge_json['data'][0]['paragraphs'].append(ipar)
            else:
                merge_json['data'][0]['paragraphs'].append(ipar)    
    return merge_json

def get_shared_qs():
    N='6'
    shared_qs = []
    for task in tasks:
        for ftype in  ftypes.keys():
            json_in = jsons[task][N][ftype]
            for ipar in json_in['data'][0]['paragraphs']:
                qid = ipar['qas'][0]['id']
                if qid not in shared_qs:
                    shared_qs.append(qid)
    
    return shared_qs

shared_qs = get_shared_qs()

os.makedirs('./datasets/QA/merged', exist_ok=True)

for task in tasks:
    for N in ['6','7']:
        if N=='6':
            output = json_merge(task,N)
            with open(f'datasets/QA/merged/QA-merged-{task}-{N}b.json','w') as outfile:
                json.dump(output, outfile)
        else:
            output = json_merge(task,N,test_only=True)
            with open(f'datasets/QA/merged/QA-merged-{task}-{N}b-test.json','w') as outfile:
                json.dump(output, outfile)

os.makedirs('datasets/QA/test_only', exist_ok=True)

for task in tasks:
    jsons[task] = {}
    for N in ['7']:
        base = eval(base_dir)
        print(base)
        jsons[task][N] = {}
        for ftype in ftypes.keys():
            ifiles = os.listdir(f'{base}{ftype}')
            fname = [f for f in ifiles if task in f][0]
            with open(f'{base}{ftype}/{fname}','r') as infile:
                jsons[task][N][ftype] = json.load(infile)
            if N == '7':
                to_dump = jsons[task][N][ftype]
                to_dump['data'][0]['paragraphs'] = [
                    ipar for ipar in to_dump['data'][0]['paragraphs']
                    if ipar['qas'][0]['id'] not in shared_qs
                    ]
                with open(f'datasets/QA/test_only/test-{task}-{ftype}.json','w') as outfile:
                    json.dump(to_dump, outfile)


for task in tasks:
    for N in ['7']:
        output = jsons[task][N][ftype]
        output['data'][0]['paragraphs'] = [
            i for i in output['data'][0]['paragraphs'] if i['qas'][0]['id'] not in shared_qs
            ]
        with open(f'datasets/QA/test_only/test'


qlens = np.array([
    len(jsons[task]['7'][ftype]['data'][0]['paragraphs'][0]['qas'])
    for task in tasks for ftype in ftypes.keys()
    ])

print(qlens)
