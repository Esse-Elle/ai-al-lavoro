import json,glob,os,re,subprocess
S='/tmp/claude-0/-home-claude/9246d2b0-a976-528c-81cc-8b69e6ccc473/scratchpad/en'
scripts={os.path.basename(f)[:-4]:open(f).read().split() for f in glob.glob(S+'/scripts/*.txt')}
scripts['02']="There is no best AI.".split()
found={}
def walk(x):
    if isinstance(x,str) and x.startswith('{"audio_url'): yield x
    elif isinstance(x,dict):
        for v in x.values(): yield from walk(v)
    elif isinstance(x,list):
        for v in x: yield from walk(v)
for line in open('/root/.claude/projects/-home-claude/9246d2b0-a976-528c-81cc-8b69e6ccc473.jsonl'):
    if 'word_timestamps' not in line: continue
    for s in walk(json.loads(line)):
        d=json.loads(s); w=[x['word'] for x in d['word_timestamps'] if x['word'] not in('<start>','<end>')]
        for k,sw in scripts.items():
            if w[:8]==sw[:8] and len(w)>=len(sw)-3: found[k]=d
for k,d in sorted(found.items()):
    os.makedirs(S+'/ts',exist_ok=True)
    w=[[x['word'],round(x['start'],3),round(x['end'],3)] for x in d['word_timestamps'] if x['word'] not in('<start>','<end>')]
    json.dump({"dur":round(d['duration'],2),"w":w},open(f'{S}/ts/{k}.json','w'),ensure_ascii=False)
    wav=f'{S}/audio/{k}.wav'
    if not os.path.exists(wav):
        subprocess.run(['curl','-sS','-o',wav,d['audio_url']],check=True)
    print(k,round(d['duration'],1),len(w),os.path.getsize(wav))
