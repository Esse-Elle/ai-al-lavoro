import json,glob,os,subprocess,re
N=lambda x:re.sub(r'[^a-z0-9]','',x.lower())
S='/tmp/claude-0/-home-claude/9246d2b0-a976-528c-81cc-8b69e6ccc473/scratchpad/en'
scripts={os.path.basename(f)[:-4]:open(f).read().split() for f in glob.glob(S+'/scripts/*.txt')}
for f in glob.glob('/root/.claude/projects/-home-claude/9246d2b0-a976-528c-81cc-8b69e6ccc473/tool-results/mcp-Heygen*speech*.txt'):
    d=json.load(open(f)); ws=d['original_words']
    w=[[x['text'],round(x['start_time'],3),round(x['end_time'],3)] for x in ws if x['text'].strip() and x['text'] not in('<start>','<end>')]
    tw=[x[0] for x in w]
    for k,sw in scripts.items():
        if [N(x) for x in tw[:8]]==[N(x) for x in sw[:8]] and len(tw)>=len(sw)-3:
            if len(tw)==len(sw): w=[[a]+b[1:] for a,b in zip(sw,w)]
            else: print(k,'WORDCOUNT MISMATCH',len(tw),len(sw))
            json.dump({"dur":round(d['duration'],2),"w":w},open(f'{S}/ts/{k}.json','w'),ensure_ascii=False)
            wav=f'{S}/audio/{k}.wav'
            if not os.path.exists(wav): subprocess.run(['curl','-sS','-o',wav,d['audio_url']],check=True)
            print(k,round(d['duration'],1),len(w),len(sw),os.path.getsize(wav))
