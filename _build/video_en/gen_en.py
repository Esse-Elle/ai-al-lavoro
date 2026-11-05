#!/usr/bin/env python3
"""Versione inglese: stesse scene del motore, testi e tempi dalla voce inglese (ts_en/)."""
import json, os, sys, re
sys.argv=[sys.argv[0]]+sys.argv[1:]
import importlib.util
spec_=importlib.util.spec_from_file_location("gen","gen.py"); g=importlib.util.module_from_spec(spec_)
src=open("gen.py",encoding="utf-8").read().replace('if __name__ == "__main__":','if False:')
exec(compile(src,"gen.py","exec"),g.__dict__)
Cues=g.Cues
class CuesEN(Cues):
    def __init__(self,k):
        d=json.load(open(f"ts_en/{k}.json")); self.dur=d["dur"]
        self.words=[(g.norm(w.strip('"')),a,b) for w,a,b in d["w"]]; self.anchor=0
CH={}
def chapter(k):
    def deco(f): CH[k]=f; return f
    return deco

@chapter("02")
def ch02(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 02",lines=["There is no","best AI."],sub="There's the right one for the task.",subAt=c("There's the right"))]
    t=c.scene("Chapter two")
    S.append(dict(type="statement",t0=t,kicker="Chapter 02",lines=[dict(text="The prompt.",at=t+.4),dict(text="How you talk to an AI.",soft=True,at=c("in other words"))],small="Whatever tool you choose, everything starts there.",smallAt=c("Whatever tool")))
    t=c.scene("Let's start with")
    S.append(dict(type="app",t0=t,kicker="Before",title="A vague prompt.",sub="Copy that would work for any brand.",nav="rec",blocks=[
        dict(k="bubble",text="Write an Instagram post for the new kitchen",at=c("write an Instagram")),
        dict(k="reply",text="Discover the new kitchen: design, functionality and style for your home! #kitchen #design #home",type=[c("I get generic"),c("I get generic")+3.0]),
        dict(k="spacer"),dict(k="composer",chips=[dict(text="Manual",sel=True)])]))
    t=c.scene("If instead I")
    full="You are the social media manager of a high-end kitchen brand. Write three caption variants for the launch of a new model. The audience is architects and families. Elegant tone, 300 characters maximum, three hashtags."
    S.append(dict(type="app",t0=t,kicker="After",title="A complete prompt.",sub="The result changes completely.",nav="rec",blocks=[
        dict(k="label",text="New chat"),
        dict(k="field",text=full,focus=True,type=[c("You are the social"),c.end("three hashtags")],h=250),
        dict(k="bars",at=c("the result changes"),w=[100,92,78,55]),
        dict(k="spacer"),dict(k="composer",chips=[dict(text="Manual",sel=True)])]))
    t=c.scene("That second request")
    S.append(dict(type="list",t0=t,kicker="The four ingredients",title="Of every good prompt.",items=[
        dict(text="The role",sub="who the AI should be",at=c("The role")),dict(text="The context",sub="the situation, the brand, the audience",at=c("The context")),
        dict(text="The task",sub="exactly what it has to do",at=c("The task")),dict(text="The format",sub="how you want the result",at=c("And the format"))]))
    t=c.scene("On top of these")
    S.append(dict(type="list",t0=t,kicker="Three tricks",title="They always work.",items=[
        dict(text="Give it a precise role",sub="You are our brand's copywriter",at=c("The first")),
        dict(text="Show examples",sub="two or three approved texts: the most powerful trick",at=c("The second")),
        dict(text="Iterate in the same conversation",sub="shorter, fewer adjectives, a call to action",at=c("The third"))]))
    t=c.scene("And a bonus")
    S.append(dict(type="statement",t0=t,kicker="Bonus",lines=[dict(text="Before you write,",at=c("before you write")),dict(text="ask me what you need to know.",soft=True,at=c("ask me what"))],small="It saves you half the corrections.",smallAt=c("saves you half")))
    t=c.scene("Now let's see")
    S.append(dict(type="pipeline",t0=t,kicker="Pipeline",title="Three 2027 trends, three posts.",steps=[
        dict(tool="Perplexity",text="Deep research: three trends with sources",at=c("Step one")),
        dict(tool="You",you=True,text="Open the sources and discard the weak ones",at=c("Step two")),
        dict(tool="Claude",text="One post per trend, in the brand's tone",at=c("Step three")),
        dict(tool="Leonardo AI",text="A concept image for each post",at=c("Step four")),
        dict(tool="Claude Design",text="4:5 layout in the brand colours",at=c("Step five"))],
        foot="Each tool does what it does best. The final review is yours.",footAt=c("Each tool does")))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 02",title="The prompt.",next="Next chapter: three side by side."))
    return S

TITLES={"02":"The prompt"}
def build(k):
    c=CuesEN(k); S=CH[k](c); total=round(c.dur+3.4,2)
    for i,s in enumerate(S):
        s["t1"]=S[i+1]["t0"] if i+1<len(S) else total
        s.setdefault("paper",s["type"] in ("cards","pipeline","compare"))
    num=k[:2]
    spec={"id":k,"total":total,"dur":c.dur,"chromeL":f"AI at Work · Chapter {num}" if k!="12" else "AI at Work · Closing","chromeR":TITLES[k],"scenes":S}
    html=open("engine_en.html",encoding="utf-8").read().replace("/*SPEC*/null",json.dumps(spec,ensure_ascii=False))
    os.makedirs("out_en",exist_ok=True)
    open(f"out_en/{k}.html","w",encoding="utf-8").write(html)
    json.dump(spec,open(f"out_en/{k}.json","w"),ensure_ascii=False,indent=1); return spec
for k in (sys.argv[1:] or list(CH)):
    sp=build(k); print(k,sp["total"],len(sp["scenes"]))
