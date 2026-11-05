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


@chapter("03")
def ch03(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 03",lines=["Three side","by side."],sub="ChatGPT, Claude and Gemini.")]
    t=c.scene("The first thing to know")
    S.append(dict(type="list",t0=t,kicker="In common",title="More alike than they seem.",mark="check",items=[
        dict(text="Chat with web search and files",at=c("All three have a chat")),
        dict(text="Projects with instructions and documents",at=c("All three have projects")),
        dict(text="Memory and connected apps",at=c("All three have a memory")),
        dict(text="Agents for multi-step tasks",at=c("and have agents")),
        dict(text="About twenty dollars a month",at=c("And the individual plan"))]))
    t=c.scene("The difference lies")
    S.append(dict(type="compare",t0=t,kicker="The difference",title="Character and way of working.",cols=["ChatGPT","Claude","Gemini"],me=1,rows=[
        dict(label="Character",vals=["Versatile and fast","Thoughtful and precise","Integrated with Google"],at=c("ChatGPT is versatile")),
        dict(label="Strong point",vals=["Images in chat","Long texts, graphics and layouts","Gmail, Drive and Docs"],at=c("long texts are")),
        dict(label="Works on",vals=["Apps in its ecosystem","Folders, connectors, browser","Google images and video"],at=c("and it works on folders"))]))
    t=c.scene("So, when do I use what")
    S.append(dict(type="list",t0=t,kicker="When to use what",title="The task decides.",items=[
        dict(text="Speed, an image on the fly",tool="ChatGPT",at=c("ChatGPT when")),
        dict(text="Work inside Gmail, Drive, Docs",tool="Gemini",at=c("Gemini when")),
        dict(text="Polished text, long documents, actions",tool="Claude",at=c("Claude when")),
        dict(text="If in doubt, same request on two",tool="Compare",at=c("And if in doubt"))]))
    t=c.scene("This isn't a battle")
    S.append(dict(type="statement",t0=t,lines=[dict(text="This isn't a battle",at=c("This isn't a battle")),dict(text="between fan clubs.",soft=True,at=c("between fan clubs"))],small="Anyone who can use one tool well learns the others in an hour.",smallAt=c("Anyone who can use")))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 03",title="Three side by side.",next="Next chapter: inside Claude."))
    return S

@chapter("04a")
def ch04a(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 04",lines=["Inside","Claude."],sub="How it's built and where to use it.")]
    t=c.scene("To find our way")
    S.append(dict(type="list",t0=t,kicker="The map",title="Eight building blocks.",sub="Start with chat and projects.",compact=True,items=[
        dict(text="Chat",tool="you reason",at=c("The chat")),dict(text="Projects",tool="the memory",at=c("Projects, your")),
        dict(text="Artifacts",tool="the finished work",at=c("Artifacts, in other")),dict(text="Scheduled tasks",tool="work at set times",at=c("Scheduled tasks")),
        dict(text="Personalisation",tool="who you are",at=c("Personalisation")),dict(text="Connectors",tool="the sockets",at=c("Connectors, the")),
        dict(text="Claude Design",tool="the designer",at=c("Claude Design, the")),dict(text="Claude Code",tool="the builder",at=c("And Claude Code"))]))
    t=c.scene("Where do you use Claude")
    S.append(dict(type="list",t0=t,kicker="Where to use it",title="The same Claude, in several places.",sub="Account, projects and artifacts are the same everywhere.",items=[
        dict(text="Desktop app",sub="Mac and Windows, the full version",at=c("There's the desktop app")),
        dict(text="Browser",sub="claude.ai, from any computer",at=c("There's the browser")),
        dict(text="Phone",sub="chat, dictate, follow tasks",at=c("There's the phone")),
        dict(text="Claude in Chrome",sub="browses and acts on websites",at=c("There's Claude in Chrome")),
        dict(text="Excel, PowerPoint, Google Workspace",sub="inside the files",at=c("There are Claude in Excel"))]))
    t=c.scene("So, desktop or browser")
    S.append(dict(type="statement",t0=t,kicker="Desktop or browser?",lines=[dict(text="The desktop app",at=c("the desktop app is the gateway")),dict(text="is the gateway to your computer.",soft=True,at=c("is the gateway"))],small="Folders, the built-in browser and computer control only work with the app open. Install it.",smallAt=c("Folders, the built-in")))
    t=c.scene("Now the latest change")
    S.append(dict(type="app",t0=t,kicker="What's new",title="One single conversation.",sub="Just write: Claude answers or gets to work.",nav="rec",panel=[
        dict(k="label",text="Progress"),dict(k="psteps",items=[dict(text="Reading the data",at=c("it gets to work")+.6),dict(text="Analysing the results",at=c("In Recents")),dict(text="Writing the report",at=c("There's no web"))]),
        dict(k="label",text="Output",at=c("For in-depth")),dict(k="outfile",text="Campaign report.docx",at=c("For in-depth"))],blocks=[
        dict(k="bubble",text="Prepare the report for the September campaign",at=c("If you ask for a piece")),
        dict(k="reply",text="Sure. I'll read the exports and prepare the report.",type=[c("it gets to work"),c("it gets to work")+2]),
        dict(k="bars",at=c("in the same conversation")),dict(k="spacer"),
        dict(k="chips",items=[dict(text="/deep research",at=c("slash deep research")),dict(text="Research",at=c("or choose Research"))]),
        dict(k="composer",chips=[dict(text="Manual",sel=True)])]))
    t=c.scene("Where did things end up")
    S.append(dict(type="list",t0=t,kicker="Where things are now",title="The new map.",items=[
        dict(text="General instructions",sub="Settings / General / Instructions for Claude",at=c("General instructions")),
        dict(text="Authorised folders",sub="Settings / Trusted folders",at=c("Authorised folders")),
        dict(text="Permissions",sub="in the box where you type: Manual or Auto",at=c("Permissions are chosen")),
        dict(text="Old tasks",sub="in Recents",at=c("You'll find your old")),
        dict(text="Deletions",sub="Claude always asks first",at=c("And for files"))]))
    t=c.scene("Let's take a tour")
    S.append(dict(type="app",t0=t,kicker="The workspace",title="A tour of the app.",sub="Sidebar, conversation, input box, progress.",nav="rec",panel=[
        dict(k="label",text="Progress",at=c("On the right")),dict(k="psteps",items=[dict(text="Reading the folder",at=c("step by step")),dict(text="Writing the draft",at=c("the context it's"))]),
        dict(k="label",text="Context",at=c("the context it's")),dict(k="rows",items=[dict(text="Marketing Claude",icon="folder",at=c("meaning folders")),dict(text="Mail",at=c("connectors and skills")),dict(text="Tone of voice",at=c("and skills"))]),
        dict(k="label",text="Output",at=c("and the outputs")),dict(k="outfile",text="Launch posts.docx",at=c("the files it created"))],blocks=[
        dict(k="bubble",text="Write three posts for the launch",at=c("In the middle")),
        dict(k="bars",at=c("with your requests")+.5),
        dict(k="rows",items=[dict(text="Read the Marketing folder?",chip="Allow",chipOn=c("Allow or Deny")+.4,at=c("Every now and then"))]),
        dict(k="spacer"),dict(k="composer",chips=[dict(text="Manual",sel=True)],at=c("At the bottom"))],
        cursor=[[c("On the left"),-170,240],[c("In the middle"),300,160],[c("Allow or Deny"),560,245],[c("At the bottom"),80,600],[c("the slash to"),140,600],[c("and next to it"),420,600],[c("On the right"),520,120]]))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 04",title="Inside Claude.",next="Part two: how Claude works."))
    return S

@chapter("09")
def ch09(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 09",lines=["Trust,","and the first step."])]
    t=c.scene("Always check")
    S.append(dict(type="list",t0=t,kicker="Always check",title="Before you publish.",mark="check",items=[
        dict(text="Rights, trademarks and guidelines",at=c("check rights")),dict(text="Real products: never invented",at=c("Real products")),
        dict(text="Numbers and data: double-checked",at=c("And numbers and data"))]))
    t=c.scene("The verification method")
    S.append(dict(type="steps",t0=t,kicker="The verification method",side=True,steps=[
        dict(h="Ask for sources",at=c("ask for sources")),dict(h="Compare",p="with data you know",at=c("compare with")),
        dict(h="Your judgment",p="as experts",at=c("use your expert")),dict(h="Test small",p="before you publish",at=c("and test small"))]))
    t=c.scene("Let me repeat")
    S.append(dict(type="statement",t0=t,lines=[dict(text="AI empowers the people who use it,",at=c("AI empowers")),dict(text="it doesn't replace judgment.",soft=True,at=c("it doesn't replace"))]))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 09",title="Trust.",next="Next chapter: an events office."))
    return S

@chapter("11b")
def ch11b(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 11",lines=["Leonardo AI,","part two."],sub="Costs, pipeline, things to watch.")]
    t=c.scene("On costs")
    S.append(dict(type="list",t0=t,kicker="Tokens and plans",title="Don't waste them.",sub="Free: 150 tokens a day. Paid: from about 12 to 60 dollars a month.",mark="check",items=[
        dict(text="One or two images at a time",at=c("generate one")),dict(text="Explore at low resolution",at=c("explore at")),
        dict(text="Only upscale the best ones",at=c("only upscale")),dict(text="Only animate the images you chose",at=c("and only animate"))]))
    t=c.scene("The last pipeline")
    S.append(dict(type="pipeline",t0=t,kicker="Pipeline",title="From idea to video.",steps=[
        dict(tool="Claude",text="Concept and scene prompts",at=c("Claude turns")),dict(tool="Leonardo",text="Images, a few at a time",at=c("Leonardo generates")),
        dict(tool="Leonardo",text="Touch-ups and upscale",at=c("Then it retouches")),dict(tool="Kling or Veo",text="The animation",at=c("It animates")),
        dict(tool="Claude",text="Editing, music, brand with HyperFrames",at=c("And finally"))],foot="The right images first, then the movement.",footAt=c("The right images")))
    t=c.scene("And a few things")
    S.append(dict(type="list",t0=t,kicker="Watch out",title="Five things.",items=[
        dict(text="Real products: reference or compositing",at=c("Real products")),dict(text="Add text afterwards",sub="Claude Design, InDesign or ChatGPT",at=c("Text in images")),
        dict(text="Commercial use: check the plan",at=c("Check the plan's")),dict(text="Brand palette, light and materials",at=c("Guide palette")),
        dict(text="State when AI was used",sub="when needed",at=c("And when needed"))]))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 11",title="Leonardo AI.",next="Last chapter: closing."))
    return S

@chapter("12")
def ch12(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Closing",lines=["Five takeaways","to keep."])]
    t=c.scene("One: every AI")
    S.append(dict(type="steps",t0=t,kicker="Five messages",side=True,steps=[
        dict(h="Every AI has its job",p="Perplexity searches, Claude works, Gemini lives in Google, ChatGPT is fast, Leonardo creates.",short="Each AI's job",at=c("One:")),
        dict(h="The prompt is everything",p="Role, context, task, format.",short="The prompt",at=c("Two:")),
        dict(h="Model, chats, folder",p="Fewer tokens and better quality.",short="Fewer tokens",at=c("Three:")),
        dict(h="Claude rewrites files",p="Ask Claude or work on a copy.",short="The copy",at=c("Four:")),
        dict(h="Five moves",p="Ask first, then delegate.",short="The five moves",at=c("Five:"))]))
    t=c.scene("And then the first step")
    S.append(dict(type="list",t0=t,kicker="By tomorrow",title="The first step.",sub="What's missing? Add it to the instructions.",items=[
        dict(text="Folder and linked project",at=c("create your work")),dict(text="Tone of voice and two texts in the Read me",at=c("put the tone")),
        dict(text="A variant of a real piece of content",at=c("ask Claude for")),dict(text="Judge the result",at=c("and judge"))]))
    t=c.scene("Because in the end")
    S.append(dict(type="statement",t0=t,lines=[dict(text="It doesn't replace your judgment.",at=c("AI doesn't replace")),dict(text="It multiplies it.",soft=True,at=c("It multiplies"))],small="Thanks for listening.",smallAt=c("Thanks for")))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="AI at Work",title="Thank you.",next="AI training for Marketing · Colombini Group"))
    return S

TITLES={"01":"Introduction and overview","02":"The prompt","03":"Three side by side","04a":"Inside Claude","04b":"Inside Claude, part two","05":"Working well","06a":"Skills and agents","06b":"Skills and agents, part two","07":"The ideal setup","08":"Automations","09":"Trust","10":"An events office","11a":"Leonardo AI","11b":"Leonardo AI, part two","12":"Closing"}
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
