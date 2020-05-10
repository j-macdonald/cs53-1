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
    for N in ['7']:
        base = eval(base_dir)
        print(base)
        jsons[task][N] = {}
        for ftype in ftypes.keys():
            ifiles = os.listdir(f'{base}{ftype}')
            fname = [f for f in ifiles if task in f][0]
            with open(f'{base}{ftype}/{fname}','r') as infile:
                jsons[task][N][ftype] = json.load(infile)

shared_qs = []




task = tasks[1]
i = 4
eval(tfile)





counter = 0
missings = []


trainsets = pd.DataFrame()

for task in tasks:



task = 'yesno'

trainsets = pd.DataFrame()
tfile = "f'datasets/QA/BioASQ-7b/train/{ftype}'"
for ftype in ftypes.keys():
    #for task in tasks:
    idir = eval(tfile)
    for ifile in [i for i in os.listdir(idir) if i.endswith('.json') and task in  i]:
        jfile = idir + '/' + ifile
        with open(jfile,'r') as infile:
            matcher = json.load(infile)['data'][0]['paragraphs']
            df = pd.DataFrame()
            df['qid'] = [ipar['qas'][0]['id'] for ipar in matcher]
            df['question'] = [ipar['qas'][0]['question'] for ipar in matcher]
            df['context'] = [ipar['context'] for ipar in matcher]
            df['answer'] = [ipar['qas'][0]['answers'] for ipar in matcher]
            df['is_impossible'] = [ipar['qas'][0].get('is_impossible',None) for ipar in matcher]
            df['ftype'] = ftype
            df['task'] = task
            df['i'] = ifile
            trainsets= pd.concat([trainsets,df])


testsets = pd.DataFrame()
tfile = "f'datasets/QA/BioASQ-6b/test/{ftype}'"
for ftype in ftypes.keys():
    #for task in tasks:
    idir = eval(tfile)
    for ifile in [i for i in os.listdir(idir) if i.endswith('.json') and task in i and 'snippet-all' not in i]:
        jfile = idir + '/' + ifile
        with open(jfile,'r') as infile:
            matcher = json.load(infile)['data'][0]['paragraphs']
            df = pd.DataFrame()
            df['qid'] = [ipar['qas'][0]['id'] for ipar in matcher]
            df['question'] = [ipar['qas'][0]['question'] for ipar in matcher]
            df['context'] = [ipar['context'] for ipar in matcher]
            df['ftype'] = ftype
            df['task'] = task
            df['i'] = ifile
            testsets = pd.concat([testsets,df])

testsets = testsets.merge(trainsets[['qid','answer']].drop_duplicates(), how="left")

def get_test_answer(question, context, verbose=False):
    criteria = (trainsets['question']==question)&(trainsets['context'].str.contains(context))
    if verbose:
        print(question, context)
    return trainsets[criteria]['answer'].values[0]

counter=0
tfile = "f'datasets/QA/BioASQ-6b/test/{ftype}'"
for ftype in ftypes.keys():
    #for task in tasks:
    idir = eval(tfile)
    for ifile in [i for i in os.listdir(idir) if i.endswith('.json') and task in i and 'snippet-all' not in i]:
        jfile = idir + '/' + ifile
        with open(jfile,'r') as infile:
            matcher = json.load(infile)
            for ipar in matcher['data'][0]['paragraphs']:
                ipar['answer'] = get_test_answer(ipar['qas'][0]['question'],ipar['context'], verbose=True)
                counter += 1
            with open(jfile+'.answered','w') as outfile:
                json.dump(matcher, outfile)






def get_answer(qid):
    answer = trainsets[trainsets['qid']==qid]['answer']
    return answer



to_merge = trainsets[['question','context','answer','is_impossible']].drop_duplicates()
testsets.merge(to_merge, how="left")

def get_answer(task,ftype,question, context):
    q = [ipar for ipar in jsons[task]['7'][ftype]['data'][0]['paragraphs']
         if ipar['qas']['question']==question and ipar['contex']==contex]
    return q




                
                for ipar in matcher['data'][0]['paragraphs']:
                    try:
                        counter += 1
                        qid = ipar['qas'][0]['id']
                        matched_q = [ipar for ipar in jsons[task]['7'][ftype]['data'][0]['paragraphs'] if ipar['qas'][0]['id']==qid][0]
                        ipar['is_impossible'] = matched_q['is_impossible']
                        ipar['answers'] = matched_q['answers']
                    except:
                        missings += [qid]


df = pd.DataFrame()
























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
