from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import glob,os,re,sys
T={}
for f in ['en_runs1.py','en_runs2.py','en_runs3.py','en_runs4.py']:
    ns={}; exec(open(f).read(),ns); T.update(ns['T'])
ns={}; src=open('tr02.py').read(); exec(src.split('PICS=')[0].split('T={',1)[0]+'T={'+src.split('T={',1)[1].split('PICS=')[0],ns)
for k,v in ns['T'].items(): T[k+1]=v
# images: slide -> (shape_id, png)
IM={17:(9,'p17_en.png'),19:(17,'p19_en.png')}
for f in glob.glob('ren/out/s*.png'):
    n=int(re.findall(r's(\d+)',os.path.basename(f))[0]); sid=[int(x.split('_')[1]) for x in [os.path.basename(g) for g in glob.glob(f'pics/s{n:03d}_*')]][0]
    IM[n]=(sid,f)
p=Presentation('it.pptx'); miss=[]
def walk(shs,m,si):
    for sh in shs:
        if sh.shape_type==MSO_SHAPE_TYPE.GROUP: walk(sh.shapes,m,si); continue
        if not sh.has_text_frame: continue
        for pi,para in enumerate(sh.text_frame.paragraphs):
            k=(sh.shape_id,pi)
            if k in m:
                new=m.pop(k); runs=para.runs
                if len(runs)!=len(new): print('RUNCOUNT',si,k,len(runs),len(new)); 
                for r,t in zip(runs,new): r.text=t
for si,s in enumerate(p.slides,1):
    m=dict(T.get(si,{}))
    walk(s.shapes,m,si)
    if m: miss.append((si,list(m)))
for si,(sid,f) in IM.items():
    sh=[x for x in p.slides[si-1].shapes if x.shape_id==sid][0]
    rid=sh._element.xpath('.//a:blip/@r:embed')[0]
    sh.part.related_part(rid)._blob=open(f,'rb').read()
p.save(sys.argv[1] if len(sys.argv)>1 else 'en_full.pptx')
print('missing',miss); print('images',sorted(IM))
