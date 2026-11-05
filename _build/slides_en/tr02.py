from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
import sys
T={
 15:{(2,0):['The prompt'],(6,0):["Section 02 · How you talk to an AI"]},
 16:{(2,0):['Before and after'],(5,0):['COMPLETE PROMPT'],(5,1):['“You are the social media manager of a high-end kitchen brand. Write 3 caption variants for the launch of a new model, for an audience of architects and families. Elegant tone, max 300 characters, 3 hashtags.”'],
     (6,0):['VAGUE PROMPT'],(6,1):['“Write an Instagram post for the new kitchen.”'],(6,2):['Result: generic, fits any brand.']},
 17:{(2,0):['Three tricks','that work'],(5,0):['1. Give it a role: “You are our brand\'s copywriter”. It changes register and depth.'],(5,1):['2. Show examples: paste 2 or 3 approved texts and ask for the same style.'],
     (5,2):['3. Iterate in the same chat: “shorter”, “fewer adjectives”, “add a call to action”.'],(5,3):["Bonus: ask the AI to ask you questions before it answers. “Before you write, ask me what you need to know.”"]},
 18:{(12,0):['Pipeline: 3 trends for 2027'],(14,0):['Suggested path: three 2027 living room trends, one post for each.']},
 19:{(2,0):['The pipeline','prompts'],(5,0):["1. Perplexity: “What are the 2027 living room trends? Three trends with industry sources, each with materials, colours and an example.”"],
     (5,1):['2. You: open the sources, drop anything weak.'],(5,2):["3. Claude, in the brand project: “For each of these 3 trends, suggest an Instagram post with a caption in our tone of voice.”"],
     (5,3):['4. Leonardo AI: one image prompt per trend (see section 11).'],(5,4):['5. Claude Design: “Lay out the 3 posts in 4:5 format in the brand colours.”']},
}
PICS={16:(9,'p17_en.png'),18:(17,'p19_en.png')}
p=Presentation(sys.argv[1])
for si,m in T.items():
    s=p.slides[si]
    for sh in s.shapes:
        if not sh.has_text_frame: continue
        for pi,para in enumerate(sh.text_frame.paragraphs):
            k=(sh.shape_id,pi)
            if k in m:
                runs=para.runs; new=m.pop(k); assert len(runs)==len(new),(si,k,len(runs))
                for r,t in zip(runs,new): r.text=t
    assert not m,(si,m)
for si,(sid,f) in PICS.items():
    sh=[x for x in p.slides[si].shapes if x.shape_id==sid][0]
    rid=sh._element.xpath('.//a:blip/@r:embed')[0]
    part=sh.part.related_part(rid); part._blob=open(f,'rb').read()
p.save(sys.argv[2]); print('ok')
