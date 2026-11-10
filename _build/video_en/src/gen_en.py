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

sentences_segs=g.sentences_segs

@chapter("01")
def ch01(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 01",lines=["Introduction","and overview."],sub="AI training for marketing.")]
    t=c.scene("Let's start with the why")
    S.append(dict(type="statement",t0=t,kicker="In marketing, time goes in two ways",lines=[dict(text="Creating content.",at=c("creating content")),dict(text="Handling the repetitive.",soft=True,at=c("handling repetitive"))],small="AI helps on both, without betraying the brand.",smallAt=c("Artificial intelligence can")))
    t=c.scene("By the end of this")
    S.append(dict(type="list",t0=t,kicker="By the end of the episode",title="Three things in hand.",items=[dict(text="Which AI to use for what",at=c("First: you'll know")),dict(text="Claude, set up properly from day one",at=c("Second: you'll know")),dict(text="A method to automate on your own",at=c("Third: you'll have"))]))
    t=c.scene("The course has eleven")
    S.append(dict(type="list",t0=t,kicker="The course",title="Eleven chapters.",compact=True,mark="dot",items=[dict(text="The landscape and the prompt",at=c("The tool landscape")),dict(text="ChatGPT, Claude and Gemini",at=c("ChatGPT, Claude and")),dict(text="Inside Claude and working well",at=c("Then we go inside")),dict(text="Skills, agents and the ideal setup",at=c("skills and agents")),dict(text="Automations and trust",at=c("Then automations")),dict(text="An events office and Leonardo AI",at=c("an events office"))]))
    t=c.scene("And before we begin")
    S.append(dict(type="statement",t0=t,kicker="Keep in mind",lines=[dict(text="AI doesn't replace people.",at=c("AI doesn't replace")),dict(text="It empowers the people who use it.",soft=True,at=c("It empowers the"))]))
    t=c.scene("Chapter one: the landscape")
    S.append(dict(type="statement",t0=t,kicker="Chapter 01",lines=[dict(text="The landscape.",at=t+.4)],small="The world of AI moves fast.",smallAt=c("the world of AI")))
    t=c.scene("Only a few months")
    S.append(dict(type="list",t0=t,kicker="From March to today",title="Almost everything has changed.",mark="dot",items=[dict(text="Claude: Opus 5.5 and Sonnet 5.5",at=c("Claude has gone")),dict(text="ChatGPT: the GPT-6 family",at=c("ChatGPT has moved")),dict(text="Gemini: series 3, Gemini 4 on the way",at=c("Gemini works with")),dict(text="Claude Design, now inside Claude",at=c("Claude Design was born")),dict(text="One single conversation, no more Chat and Cowork",at=c("And in the Claude app"))]))
    t=c.scene("I'm not telling you")
    S.append(dict(type="statement",t0=t,lines=[dict(text="Learn the method,",at=c("learn the method")),dict(text="not the buttons.",soft=True,at=c("not the buttons"))],small="The buttons change every month. The method stays.",smallAt=c("The buttons change")))
    t=c.scene("And the method starts")
    S.append(dict(type="list",t0=t,kicker="How an AI thinks",title="It completes text in the most likely way.",items=[dict(text="Where information is missing, it fills the gaps",sub="with generic answers, sometimes made up",at=c("Where information is")),dict(text="More context, more the result is yours",at=c("The more context")),dict(text="It always needs rereading",sub="a brilliant collaborator, not an oracle",at=c("And it always needs"))]))
    t=c.scene("Picture it as")
    S.append(dict(type="statement",t0=t,lines=[dict(text="Very talented,",at=c("very talented")),dict(text="on their first day at work.",soft=True,at=c("on their first"))],small="Capable and fast, but knows neither the company nor the customers.",smallAt=c("capable, fast")))
    t=c.scene("With that said")
    sp=[c("ChatGPT, by OpenAI"),c("Claude, by Anthropic"),c("Gemini, by Google"),c("Perplexity is the researcher"),c("Leonardo AI is the visual")]
    S.append(dict(type="cards",t0=t,kicker="The AI landscape",title="Five tools, five jobs.",spot=sp,cards=[
        dict(ck="Text and ideas",nm="ChatGPT",by="by OpenAI",job="The generalist",pts=["Brainstorming and drafts","Images in chat"],at=t+.8),
        dict(ck="Text and work",nm="Claude",by="by Anthropic",job="The collaborator who reasons",pts=["Copy in the brand's tone","Works on files and tools"],dark=True,at=t+1.1),
        dict(ck="Google ecosystem",nm="Gemini",by="by Google",job="The assistant in Gmail and Drive",pts=["Summarises threads and files","NotebookLM"],at=t+1.4),
        dict(ck="Research",nm="Perplexity",by="by Perplexity AI",job="The researcher",pts=["Trends and competitors","Clickable sources"],at=t+1.7),
        dict(ck="Images and video",nm="Leonardo AI",by="a platform of models",job="The visual studio",pts=["Moodboards and concepts","Video teasers"],at=t+2.0)]))
    t=c.scene("Let's put it into practice")
    S.append(dict(type="list",t0=t,kicker="In practice",title="Who does what.",compact=True,items=[
        dict(text="Trends, data and competitors",tool="Perplexity",at=c("If you need to find")),dict(text="Copy, press releases, product sheets",tool="Claude",at=c("If you need to write")),
        dict(text="Work inside Gmail or Drive",tool="Gemini",at=c("If the work is")),dict(text="Quick brainstorm, an image on the fly",tool="ChatGPT",at=c("For a quick brainstorm")),
        dict(text="Moodboards and settings",tool="Leonardo",at=c("For moodboards and")),dict(text="Automating a repetitive job",tool="Claude",at=c("And to automate"))]))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 01",title="The landscape.",next="Next chapter: the prompt."))
    return S

@chapter("04b")
def ch04b(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 04",lines=["Inside Claude,","part two."],sub="How it works, models and tokens.")]
    t=c.scene("So how does Claude work")
    S.append(dict(type="steps",t0=t,kicker="The work cycle",side=True,steps=[
        dict(h="Understands",p="Reads the request and, if needed, asks.",at=c("It understands")),dict(h="Plans",p="Breaks the work down into steps.",at=c("It plans")),
        dict(h="Uses tools",p="Files, web, connectors.",at=c("It uses tools")),dict(h="Asks",p="Waits for your OK on important actions.",at=c("It asks for")),
        dict(h="Delivers",p="Saves files or artifacts and sums up.",at=c("And it delivers"))]))
    t=c.scene("So before you start")
    S.append(dict(type="list",t0=t,kicker="Before you start",title="Three choices.",items=[
        dict(text="Permissions: Manual to begin with",sub="Auto only when the workflow is proven",at=c("Permissions: Manual")),
        dict(text="Where: a dedicated folder",sub="never the whole disk",at=c("Where it works")),
        dict(text="With what: only what you need",sub="the connectors and skills for that job",at=c("And with what"))]))
    t=c.scene("Now a topic that")
    S.append(dict(type="statement",t0=t,kicker="Time and money",lines=[dict(text="Models",at=c("models and tokens")),dict(text="and tokens.",soft=True,at=c("and tokens"))]))
    t=c.scene("The model is the brain")
    S.append(dict(type="cards",t0=t,kicker="The models",title="Engines of different power.",cards=[
        dict(ck="Light",nm="Haiku",job="Quick",pts=["Simple tasks"],at=c("Haiku is quick")),
        dict(ck="Every day",nm="Sonnet",job="Balanced",pts=["The everyday model"],dark=True,at=c("Sonnet is balanced")),
        dict(ck="Deep",nm="Opus",job="Reasoning",pts=["Serious work"],at=c("Opus is for deep")),
        dict(ck="Autonomous",nm="Fable",job="Long projects",pts=["Carried forward on its own"],at=c("Fable is designed"))],
        foot="The number is the generation. <b>The effort is how much it thinks.</b>",footAt=c("The number next to")))
    t=c.scene("A token, on the other")
    S.append(dict(type="statement",t0=t,kicker="The token",lines=[dict(text="A piece of a word,",at=c("a piece of a word")),dict(text="three or four characters.",soft=True,at=c("about three or four"))],small="Everything is measured in tokens: request, attachments, reasoning and answer.",smallAt=c("Everything is measured")))
    t=c.scene("And above all")
    S.append(dict(type="statement",t0=t,kicker="Good to know",lines=[dict(text="With every message",at=c("with every message")),dict(text="Claude rereads everything.",soft=True,at=c("Claude rereads the whole"))],small="The eighth message costs as much as the seven before it. The limit resets every five hours.",smallAt=c("Think about it")))
    t=c.scene("The same goes for models")
    S.append(dict(type="list",t0=t,kicker="Usage",title="More power, more tokens.",sub="Opus to summarise an email? Like grocery shopping in a Formula One car.",items=[
        dict(text="Haiku",tool="Low",at=c("Haiku uses little")),dict(text="Sonnet",tool="Medium",at=c("Sonnet a medium")),
        dict(text="Opus",tool="High",at=c("Opus a lot")),dict(text="Fable",tool="Very high",at=c("Fable a huge"))]))
    t=c.scene("So how do you choose")
    S.append(dict(type="list",t0=t,kicker="How to choose",title="Four questions.",sub="Start with Sonnet. Move up only if the answer isn't good enough.",items=[
        dict(text="Is it simple and quick?",tool="Haiku",at=c("Is it simple")),dict(text="Is it everyday work?",tool="Sonnet",at=c("Is it everyday")),
        dict(text="Do I need to think it through?",tool="Opus",at=c("Do I need to")),dict(text="Is it long and autonomous?",tool="Fable",at=c("Is it long"))]))
    t=c.scene("Seven habits")
    S.append(dict(type="list",t0=t,kicker="Mindful use",title="Seven habits.",mark="check",compact=True,items=[
        dict(text="Model and effort that fit the task",at=c("Choose a model and")),dict(text="One chat per topic",at=c("One chat per topic")),
        dict(text="No re-uploaded files: use the folder",at=c("Don't upload the same")),dict(text="Group your questions",at=c("Group your questions")),
        dict(text="Short answers when they're enough",at=c("Ask for short")),dict(text="Deep research only when needed",at=c("Only use deep")),
        dict(text="A look at your usage",at=c("And every now and"))]))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 04",title="Inside Claude.",next="Next chapter: working well."))
    return S

@chapter("05")
def ch05(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 05",lines=["Working","well."],sub="How you set up the work counts.")]
    t=c.scene("Let's start with the chat")
    S.append(dict(type="list",t0=t,kicker="Before you hit enter",title="Three choices change the answer.",items=[
        dict(text="The model, with its effort",at=c("the model with its")),dict(text="The tools you turn on",at=c("the tools you turn")),
        dict(text="The project you're in",at=c("and the project you're"))]))
    t=c.scene("And a few good habits")
    S.append(dict(type="list",t0=t,kicker="Good habits",title="In chat.",mark="check",items=[
        dict(text="One chat per topic",at=c("one chat per")),dict(text="Attach the material",sub="instead of summarising it in words",at=c("attach the material")),
        dict(text="Ask for sources",at=c("ask for sources")),dict(text="Rename important chats",at=c("and rename important"))]))
    t=c.scene("Then projects")
    S.append(dict(type="app",t0=t,kicker="Projects",title="Your collaborator's memory.",sub="Set it up once, it always knows you.",nav="prj",blocks=[
        dict(k="label",text="Projects"),dict(k="title",text="Marketing"),dict(k="text",text="Permanent instructions and materials, in every conversation.",at=c("A project is a space")),
        dict(k="rows",items=[dict(text="On claude.ai",small="in your account, shareable",at=c("The ones on")),dict(text="In the desktop app",small="folders, memory, scheduled tasks",at=c("The ones in the desktop")),dict(text="They can be linked",at=c("And the two can"))])]))
    t=c.scene("And here's the move")
    S.append(dict(type="list",t0=t,kicker="The move that changes everything",title="The project linked to a folder.",sub="Claude works on your desk, not on copies.",mark="check",items=[
        dict(text="Reads documents without uploading them",at=c("It reads documents")),dict(text="Always sees the latest version",at=c("It always sees")),
        dict(text="Saves outputs there",at=c("It saves outputs")),dict(text="Saves you tokens and time",at=c("And it saves you"))]))
    t=c.scene("How should you organise")
    S.append(dict(type="app",t0=t,kicker="The folder",title="One structure for everyone.",sub="Rules, materials and outputs: Claude knows where to look.",nav="prj",blocks=[
        dict(k="label",text="Marketing Claude"),dict(k="tree",items=[
            dict(text="00_ReadMe",small="instructions, tone, rules",dir=True,at=c("a folder called zero")),dict(text="01_Brand",small="brand book, logo, palette",dir=True,at=c("One for the brand")),
            dict(text="02_Products",small="catalogues, sheets, price lists",dir=True,at=c("One for products")),dict(text="03_Approved examples",small="texts and posts to imitate",dir=True,at=c("One for approved")),
            dict(text="04_Input",small="briefs, exports, materials",dir=True,at=c("One for inputs")),dict(text="05_Output",small="Claude's work",dir=True,at=c("One for outputs")),
            dict(text="99_Archive",small="old versions",dir=True,at=c("And an archive"))])]))
    t=c.scene("The ideal project is set up")
    S.append(dict(type="steps",t0=t,kicker="The ideal project · Seven steps",side=True,steps=[
        dict(h="Create the folder",short="The folder",at=c("Create the folder with")),dict(h="Projects, +, existing folder",short="Project from the folder",at=c("In the desktop app")),
        dict(h="Name and description",short="Name and description",at=c("Give the project")),dict(h="The instructions",short="Instructions",at=c("Write the instructions")),
        dict(h="The team's project",p="If there is one, on claude.ai.",short="Team project",at=c("Link the team's")),dict(h="Only what you need",p="Connectors and skills.",short="Connectors and skills",at=c("Turn on only")),
        dict(h="The first test",p="Read 00_ReadMe and tell me what you understood.",short="First test",at=c("And run a first"))]))
    t=c.scene("An example of project instructions")
    txt="You are the brand's marketing collaborator. Before every job, read the Read me and Brand folders. Only use data found in the folder: if something's missing, ask, don't make it up. Elegant, warm tone, short sentences, no superlatives. Always save your work in the Output folder, named with date, topic and version. Never overwrite a file: create a new version. At the end, tell me what you did and where you saved it."
    S.append(dict(type="quote",t0=t,kicker="Example",title="Project instructions.",label="Project instructions",segs=sentences_segs(c,txt)))
    t=c.scene("Now a question everyone")
    S.append(dict(type="cards",t0=t,kicker="Everyone's question",title="Artifact or file?",cards=[
        dict(ck="Lives inside Claude",nm="Artifact",job="Shared with a link",pts=["In the Artifacts section","Edited in Claude"],dark=True,at=c("An artifact is a")),
        dict(ck="In your folder",nm="File",job="A real document",pts=["Word, PowerPoint, Excel, PDF","Opens with Office"],at=c("A file, instead"))],
        foot="Often you have both: <b>an artifact can be exported, a file can be published.</b>",footAt=c("Often you have both")))
    t=c.scene("The four most useful")
    S.append(dict(type="list",t0=t,kicker="Artifacts",title="The four most useful.",items=[
        dict(text="Docs",sub="documents to write and comment on together",at=c("are Docs")),dict(text="Slides",sub="presentations to project or export",at=c("Slides, presentations")),
        dict(text="Design",sub="graphics, mockups and pages",at=c("Design, meaning")),dict(text="Live pages",sub="trackers, calculators, dashboards",at=c("And live pages"))]))
    t=c.scene("And now a golden rule")
    S.append(dict(type="statement",t0=t,kicker="The golden rule",lines=[dict(text="Claude rewrites",at=c("it rewrites it")),dict(text="the file from scratch.",soft=True,at=c("from scratch"))],small="Touched up by hand and then regenerated? Your changes disappear.",smallAt=c("So if you've")))
    t=c.scene("There are two ways around")
    S.append(dict(type="list",t0=t,kicker="Two ways",title="Not to lose work.",items=[
        dict(n="A",text="Ask Claude to make the changes",sub="on slide 4 shorten the title, on slide 7 add the price",at=c("Option A")),
        dict(n="B",text="Duplicate and rename",sub="work on the copy: Claude won't touch it",at=c("Option B"))]))
    t=c.scene("Let's close the chapter")
    S.append(dict(type="app",t0=t,kicker="Claude Design",title="From brief to layout.",sub="It doesn't replace the designer: it speeds up the first versions. For photos, Leonardo.",nav="art",blocks=[
        dict(k="label",text="Artifacts / Design"),dict(k="bubble",text="Poster for the showroom event, in the brand colours",at=c("From a brief")),
        dict(k="rows",items=[dict(text="Landing page and newsletter mockups",at=c("we use it for landing")),dict(text="Social posts",at=c("social posts")),dict(text="Posters for showroom events",at=c("posters for showroom")),dict(text="Presentations in our style",at=c("and presentations in"))])]))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 05",title="Working well.",next="Next chapter: skills and agents."))
    return S

@chapter("06a")
def ch06a(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 06",lines=["Skills","and agents."],sub="The tools that power up Claude.")]
    t=c.scene("Let's start with skills")
    S.append(dict(type="statement",t0=t,kicker="The skill",lines=[dict(text="The manual",at=c("a manual on the")),dict(text="on the shelf.",soft=True,at=c("on the shelf"))],small="Method, tone, format. It switches on by itself or with the slash, in every project.",smallAt=c("It switches on")))
    t=c.scene("What's inside")
    S.append(dict(type="app",t0=t,kicker="Inside a skill",title="No code: it's text.",sub="The description decides when it kicks in.",nav="cus",blocks=[
        dict(k="label",text="SKILL.md"),
        dict(k="field",text="name: tone-of-voice\ndescription: use this skill when you write copy, posts, press releases or newsletters for the brand",focus=True,type=[c("At the top there's"),c.end("for the brand")],h=150),
        dict(k="label",text="The method",at=c("Below that is")),
        dict(k="rows",items=[dict(text="Tone of voice",at=c("the tone of voice")),dict(text="Words yes and words no",at=c("words to use")),dict(text="Approved examples",at=c("approved examples"))])]))
    t=c.scene("Where do you find skills")
    S.append(dict(type="app",t0=t,kicker="The marketplace",title="Plugins, connectors, agents.",sub="You get there from Customize.",nav="cus",blocks=[
        dict(k="label",text="Customize / Marketplace"),
        dict(k="rows",items=[dict(text="Word, Excel, PowerPoint and PDF",chip="Install",chip2="Installed",chipOn=c("You'll find")+1.5,at=c("You'll find")),
            dict(text="Marketing plugin",chip="Install",chip2="Installed",chipOn=c("Brand Voice"),at=c("like the Marketing")),
            dict(text="Brand Voice plugin",chip="Install",at=c("Brand Voice")),dict(text="Team skills",small="shared with everyone",at=c("and the skills your"))])]))
    t=c.scene("But the real value")
    S.append(dict(type="steps",t0=t,kicker="A custom skill",side=True,steps=[
        dict(h="A task you repeat",short="The task",at=c("Pick a task")),dict(h="Create a skill that…",short="The request",at=c("Ask Claude")),
        dict(h="Answer the questions",short="The questions",at=c("Claude asks you")),dict(h="Good and bad examples",short="The examples",at=c("Attach good examples")),
        dict(h="Try it on three cases",short="The test",at=c("Save it")),dict(h="Share it",p="With the whole team.",short="The team",at=c("and then share"))]))
    t=c.scene("A few ideas for marketing")
    S.append(dict(type="list",t0=t,kicker="Ideas for marketing",title="Seven skills.",sub="If you had to pick one: tone of voice.",compact=True,items=[
        dict(text="Tone of voice",at=c("A tone of voice"),hl=c("If you had to")),dict(text="Press release",at=c("One for press")),
        dict(text="Product sheet",at=c("One for product")),dict(text="Social posts",at=c("One for social")),dict(text="Campaign report",at=c("One for campaign")),
        dict(text="Presentations in the template",at=c("One for presentations")),dict(text="Briefs to agencies and photographers",at=c("And one for briefs"))]))
    t=c.scene("Let's move on to agents")
    S.append(dict(type="statement",t0=t,kicker="The agent",lines=[dict(text="A collaborator",at=c("a collaborator with")),dict(text="with its own desk.",soft=True,at=c("with its own"))],small="It carries out a whole task in a separate context and reports back only the result.",smallAt=c("Claude hands it")))
    t=c.scene("An agent is a role")
    S.append(dict(type="list",t0=t,kicker="A role file",title="Four elements.",sub="A project with role instructions is already a lightweight agent.",items=[
        dict(text="Name and description",sub="who it is and when to use it",at=c("name and description")),dict(text="Tools",sub="files, web, connectors",at=c("the tools it can")),
        dict(text="Model",sub="the one it works with",at=c("the model it works")),dict(text="Instructions",sub="its method",at=c("and the instructions"))]))
    t=c.scene("So, skill or agent")
    S.append(dict(type="cards",t0=t,kicker="Skill or agent?",title="Not a choice: they work together.",cards=[
        dict(ck="The skill",nm="The manual",job="Knowledge, method, format",pts=["Works in the conversation"],at=c("The skill is the manual")),
        dict(ck="The agent",nm="The collaborator",job="A role",pts=["You delegate a whole task"],dark=True,at=c("The agent is the collaborator"))],
        foot="Skills provide the method, agents do the work. <b>Skills first.</b>",footAt=c("Skills provide the")))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 06",title="Skills and agents.",next="Part two: connectors, scheduled tasks and Code."))
    return S

@chapter("06b")
def ch06b(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 06",lines=["Skills & agents,","part two."],sub="Connectors, scheduled tasks and Code.")]
    t=c.scene("An example of how")
    S.append(dict(type="app",t0=t,kicker="Example",title="Analysing a trade fair.",sub="Three agents in parallel, each with its own method.",nav="rec",panel=[
        dict(k="label",text="Progress"),dict(k="psteps",items=[dict(text="Stands analysed",at=c("A press agent")),dict(text="Press review ready",at=c("And a strategy agent")),dict(text="Conclusions",at=c("Each at its own"))]),
        dict(k="label",text="Output",at=c("Each at its own")),dict(k="outfile",text="Fair analysis.pptx",at=c("Each at its own"))],blocks=[
        dict(k="bubble",text="Analyse the September fair",at=c("analyse the September")),
        dict(k="reply",text="I'll coordinate three agents in parallel.",type=[c("Claude coordinates"),c("Claude coordinates")+1.8]),
        dict(k="toolcall",text="Photo agent",small="visual reading",at=c("A photo agent")),dict(k="toolcall",text="Press agent",small="press review",at=c("A press agent")),
        dict(k="toolcall",text="Strategy agent",small="tone of voice, report",at=c("And a strategy agent")),dict(k="spacer"),dict(k="composer",chips=[dict(text="Manual",sel=True)])]))
    t=c.scene("Then there are connectors")
    S.append(dict(type="app",t0=t,kicker="Connectors",title="The sockets to your tools.",sub="Behind them is MCP: a USB-C socket for lots of devices.",nav="cus",blocks=[
        dict(k="label",text="Customize / Connectors"),
        dict(k="rows",items=[dict(text="Mail",tog=c("mail,")),dict(text="Calendar",tog=c("calendar,")),dict(text="Drive",tog=c("Drive,")),dict(text="SharePoint",tog=c("SharePoint,")),dict(text="Canva",tog=c("Canva,")),dict(text="CRM",tog=c("the CRM"))]),
        dict(k="text",text="Claude only sees what you authorise.",at=c("Claude only sees"))]))
    t=c.scene("One clarification")
    S.append(dict(type="statement",t0=t,kicker="One clarification",lines=[dict(text="PowerPoint and Excel?",at=c("to create a PowerPoint")),dict(text="No connector needed.",soft=True,at=c("you don't need a connector"))],small="Claude can do that on its own. A connector is for reading from and writing to external systems.",smallAt=c("A connector is for")))
    t=c.scene("Scheduled tasks are the collaborator")
    S.append(dict(type="app",t0=t,kicker="Scheduled tasks",title="They work even without you.",sub="In the cloud, even with your computer off.",nav="pia",blocks=[
        dict(k="label",text="Scheduled"),dict(k="title",text="New task"),
        dict(k="chips",items=[dict(text="Every hour",at=c("every hour")),dict(text="Every day",at=c("every day")),dict(text="Every week",at=c("every week"),on=c("or on demand")),dict(text="On demand",at=c("or on demand"))]),
        dict(k="field",text="Every Monday at 8, read the exports in the folder and prepare the social report.",focus=True,type=[c("You create them"),c("They use the connectors")],h=120),
        dict(k="chips",items=[dict(text="Create with Claude",at=c("Create with Claude"),on=c("Create with Claude")+.5)])]))
    t=c.scene("And then Claude Code")
    S.append(dict(type="app",t0=t,kicker="Claude Code",title="The tool builder.",sub="Born for developers, useful for non-programmers too.",nav="",tab="code",blocks=[
        dict(k="label",text="Code / Marketing Claude"),
        dict(k="rows",items=[dict(text="Rename 500 photos from a shoot",at=c("renaming five hundred")),dict(text="A mini site for an event",at=c("creating a mini")),
            dict(text="From price list to product sheets",at=c("turning a price")),dict(text="Edit and cut a video",at=c("editing and cutting")),dict(text="Small custom tools",at=c("building small"))])]))
    t=c.scene("When is it better")
    S.append(dict(type="list",t0=t,kicker="When it's worth it",title="Code or chat?",sub="Describe the result, not the code. Try it on a few files.",items=[
        dict(text="Dozens or hundreds of files",at=c("When the work touches")),dict(text="A tool to reuse",at=c("when you need a tool")),
        dict(text="A technical result",sub="like a web page",at=c("or when you want"))]))
    t=c.scene("A final word on security")
    S.append(dict(type="cards",t0=t,kicker="Security",title="You decide how much autonomy.",cards=[
        dict(ck="Default",nm="Manual",job="Asks before acting",pts=["The starting point"],dark=True,at=c("Manual, the default")),
        dict(ck="Proven workflows",nm="Auto",job="Doesn't ask at every step",pts=["Only drafts and research"],at=c("Auto means"))],
        foot="Sending, paying, deleting, publishing: <b>always with your approval.</b>",footAt=c("Irreversible actions")))
    t=c.scene("Let's see it all together")
    S.append(dict(type="pipeline",t0=t,kicker="Pipeline",title="From a launch to all the content.",steps=[
        dict(tool="Project",text="Tone of voice and the new product sheet",at=c("First, the brand")),dict(tool="Claude",text="The press release, as a Doc",at=c("Second, Claude")),
        dict(tool="You",you=True,text="Review and approve",at=c("Third, you")),dict(tool="Claude",text="Three posts and a newsletter",at=c("Fourth, from")),
        dict(tool="Claude Design",text="The poster for the showroom",at=c("Fifth, with"))],foot="One single context, many formats.",footAt=c("One single context")))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 06",title="Skills and agents.",next="Next chapter: the ideal setup."))
    return S

@chapter("08")
def ch08(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 08",lines=["Automating","the repetitive."],sub="The method to do it on your own.")]
    t=c.scene("Every marketing department")
    S.append(dict(type="list",t0=t,kicker="Jobs that repeat",title="Always the same way.",sub="If you can explain them to a new colleague, Claude can carry them out.",mark="dot",items=[
        dict(text="Invoices to forward to whoever approves",at=c("Invoices from")),dict(text="Material requests from retailers",at=c("Material requests")),
        dict(text="Weekly social and campaign reports",at=c("Weekly reports")),dict(text="Press reviews and competitors",at=c("Press reviews")),dict(text="Shoot photos to file",at=c("Photos from shoots"))]))
    t=c.scene("Every automation, simple")
    S.append(dict(type="steps",t0=t,kicker="The five moves",side=True,steps=[
        dict(h="Trigger",p="When does it start? Every hour, every Monday, an email.",at=c("Trigger:")),dict(h="Read",p="The inbox, a folder, a file, a website.",at=c("Read: what")),
        dict(h="Decide",p="A table: if this happens, do that.",at=c("Decide:")),dict(h="Act",p="Forward, save, rename, write a draft.",at=c("Act: what")),
        dict(h="Log",p="Updates a file and sends a summary.",at=c("Log:"))]))
    t=c.scene("Let's take the invoice")
    S.append(dict(type="app",t0=t,kicker="Example",title="The invoice in the inbox.",sub="If it's unsure it doesn't guess: it flags it to you.",nav="pia",panel=[
        dict(k="label",text="Progress"),dict(k="psteps",items=[dict(text="Reads the emails",at=c("Claude looks at")),dict(text="Extracts the data",at=c("It extracts the")),dict(text="Sorts",at=c("If it finds it")),dict(text="Updates the log",at=c("At the end it updates"))]),
        dict(k="label",text="Output",at=c("At the end it updates")),dict(k="outfile",text="Invoice log.xlsx",at=c("At the end it updates")),dict(k="outfile",text="End-of-day summary",at=c("at the end of the day"))],blocks=[
        dict(k="label",text="Scheduled task · every hour"),
        dict(k="toolcall",text="New emails with a PDF",small="invoice?",at=c("Claude looks at")),
        dict(k="toolcall",text="Supplier, number, amount",small="extracted",at=c("It extracts the")),
        dict(k="toolcall",text="Who gets what table",small="checked",at=c("Then it looks up")),
        dict(k="rows",items=[dict(text="Social agency",small="to the contact",chip="Forwarded",at=c("If it finds it")),dict(text="Unknown supplier",chip="To check",at=c("If it's unsure"))])]))
    t=c.scene("The secret is to separate")
    S.append(dict(type="list",t0=t,kicker="Who gets what",title="The rules in a table.",sub="A contact changes? Update the table, the automation stays untouched.",items=[
        dict(text="Social agency",sub="Social invoices folder",tool="Maria",at=c("the social agency")),dict(text="Photo studio",sub="Shoots folder",tool="Luca",at=c("the photo studio")),
        dict(text="Trade fair organiser",sub="Events folder",tool="Anna",at=c("the trade fair"))]))
    t=c.scene("The task prompt")
    txt="Every hour, check the marketing inbox. For every new email with a PDF that looks like an invoice: read the supplier, number, date and amount; look up the supplier in the who gets what file; if you find it, forward it to the contact person and save the PDF in their folder; if you can't find it or you're unsure, do nothing and add it to the list to check; update the invoice log. At six pm, send me a summary."
    S.append(dict(type="quote",t0=t,kicker="Without a line of code",title="The prompt, in plain English.",sub="The five moves, as you'd say them to a colleague.",label="Task prompt",segs=sentences_segs(c,txt)))
    t=c.scene("The same pattern works")
    S.append(dict(type="list",t0=t,kicker="The same pattern",title="For many other jobs.",items=[
        dict(text="Requests from retailers",sub="a draft reply with the right link",tool="New email",at=c("Requests from retailers")),
        dict(text="Weekly social report",sub="a Doc with charts and commentary",tool="Monday 8:00",at=c("The weekly social")),
        dict(text="Press review and competitors",sub="a summary with sources",tool="Friday",at=c("Press review and competitors")),
        dict(text="Photo archive",sub="recognises, renames and sorts",tool="End of shoot",at=c("And the photo archive"))]))
    t=c.scene("There are also tools")
    S.append(dict(type="cards",t0=t,kicker="Tools compared",title="Rigid rules or judgment.",cards=[
        dict(ck="Classic automation",nm="Rigid rules",job="Fire instantly",pts=["Simple flows that never change"],at=c("There are also tools")),
        dict(ck="Claude",nm="Judgment",job="Understands texts, PDFs and emails",pts=["Written differently every time"],dark=True,at=c("Claude, on the other"))],
        foot="Often it pays to combine them. <b>The five moves work everywhere.</b>",footAt=c("Often it pays")))
    t=c.scene("Six golden rules")
    S.append(dict(type="list",t0=t,kicker="The golden rules",title="Six rules.",mark="check",compact=True,items=[
        dict(text="A small, frequent job",at=c("Start with a small")),dict(text="Rules explained as to a colleague",at=c("Write the rules")),
        dict(text="Manual for one or two weeks",at=c("Begin with permissions")),dict(text="Always the I don't know case",at=c("Always plan for")),
        dict(text="A log of everything",at=c("Keep a log")),dict(text="At first: no sending or payments",at=c("And at the start"))]))
    t=c.scene("And the pipeline to build")
    S.append(dict(type="pipeline",t0=t,kicker="Pipeline",title="Your first automation.",steps=[
        dict(tool="You",you=True,text="A small, frequent job",at=c("Choose a small")),dict(tool="You",you=True,text="Five moves and a rules table",at=c("Fill in the five")),
        dict(tool="Claude",text="Scheduled, Create with Claude",at=c("Go to Scheduled")),dict(tool="Claude",text="Two weeks on Manual",at=c("Let it run")),
        dict(tool="You",you=True,text="Fix it, then more autonomy",at=c("Then fix the rules"))],foot="Start small, observe, expand. Never the other way round.",footAt=c("Start small, observe")))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 08",title="Automations.",next="Next chapter: trust."))
    return S

@chapter("10")
def ch10(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 10",lines=["An events office","with Claude."],sub="All the building blocks, on a concrete case.")]
    t=c.scene("The idea is this")
    S.append(dict(type="statement",t0=t,kicker="The idea",lines=[dict(text="A digital team.",at=c("as a digital team")),dict(text="You are the director.",soft=True,at=c("And you are the"))],small="Each agent has a role and its own hours. They all work in the same folder.",smallAt=c("Each has its own")))
    t=c.scene("At the centre is")
    S.append(dict(type="cards",t0=t,kicker="The Events Office project",title="Four blocks around the project.",cards=[
        dict(ck="The method",nm="Skills",pts=["Event brief","Run sheet","Invitations","Report"],at=c("Skills: event")),
        dict(ck="The roles",nm="Agents",pts=["Venues and suppliers","Communication","Logistics","Analysis"],dark=True,at=c("Agents: venues")),
        dict(ck="The sockets",nm="Connectors",pts=["Mail","Calendar","Drive or SharePoint","Excel"],at=c("Connectors: mail")),
        dict(ck="The hours",nm="Scheduled",pts=["Monday status","Guest list","Reminders","Final report"],at=c("And scheduled tasks"))],
        foot="The outputs: <b>Docs, Slides, Design and Excel files.</b>",footAt=c("The outputs arrive")))
    t=c.scene("The events folder has")
    S.append(dict(type="app",t0=t,kicker="The folder",title="The office's real asset.",sub="Suppliers and venues, with contacts and prices.",nav="prj",blocks=[
        dict(k="label",text="Events Office"),dict(k="tree",items=[
            dict(text="00_ReadMe",small="rules, tone, typical budget",at=c("a Read me with")),dict(text="Suppliers and venues.xlsx",small="contacts and prices",at=c("a suppliers and venues")),
            dict(text="Templates",small="briefs, budgets, run sheets, invitations",dir=True,at=c("templates for briefs")),dict(text="Events",dir=True,at=c("an Events folder")),
            dict(text="2026-11_Showroom",small="brief, guests, photos, report",dir=True,d=1,at=c("with a subfolder")),dict(text="Archive",dir=True,at=c("and an archive"))])]))
    t=c.scene("The pipeline for an event")
    S.append(dict(type="pipeline",t0=t,kicker="Pipeline",title="From brief to final report.",steps=[
        dict(tool="Claude",text="Concept, goals and budget",at=c("Claude turns the brief")),dict(tool="Claude",text="Venues, suppliers, quotes",at=c("Then it looks for")),
        dict(tool="You",you=True,text="Choose and confirm",at=c("You choose and")),dict(tool="Claude",text="Timeline, invitations, posts, poster",at=c("Claude prepares the timeline")),
        dict(tool="Claude",text="Guests, reminders, run sheet",at=c("Then it keeps")),dict(tool="Claude",text="Report, thank-yous, press review",at=c("And at the end"))],
        foot="Claude prepares, you decide: everything sent goes through your approval.",footAt=c("Claude prepares, you")))
    t=c.scene("Scheduled tasks are the heart")
    S.append(dict(type="list",t0=t,kicker="Scheduled tasks",title="The heart of the office.",items=[
        dict(text="Status of events and deadlines",tool="Monday 9:00",at=c("Every Monday at")),dict(text="Invitation replies, guest list",tool="Every day",at=c("Every day, reading")),
        dict(text="Reminders to suppliers, as drafts",tool="-14 / -7 / -1",at=c("Fourteen, seven")),dict(text="Thank-yous and collecting photos",tool="Day after",at=c("The day after")),
        dict(text="Report: attendance, costs, results",tool="+7 days",at=c("A week later"))]))
    t=c.scene("prompt to paste into")
    txt="You are the assistant of the marketing events office. Read the Read me and the suppliers and venues file. For a new event, create its folder with brief, budget and timeline. Keep the guest list updated from emails and forms. Prepare invitations, communications and reminders only as drafts: nothing gets sent without my OK. Every Monday, send me the status of the events."
    S.append(dict(type="quote",t0=t,kicker="To paste into the project",title="The kick-off prompt.",label="Project instructions",segs=sentences_segs(c,txt)))
    t=c.scene("Setup takes eight steps")
    S.append(dict(type="steps",t0=t,kicker="Setup · Eight steps",side=True,steps=[
        dict(h="The folder",short="Folder",at=c("create the folder")),dict(h="Suppliers and templates",short="Suppliers and templates",at=c("fill in the suppliers")),
        dict(h="Linked project",short="Project",at=c("create the project")),dict(h="The instructions",short="Instructions",at=c("write the instructions")),
        dict(h="The skills",short="Skills",at=c("create the skills")),dict(h="Connectors with IT",short="Connectors",at=c("connect mail")),
        dict(h="Scheduled tasks on Manual",short="Scheduled",at=c("create the scheduled")),dict(h="A small event",p="Half a day plus two weeks of running in.",short="Test",at=c("and test everything"))]))
    t=c.scene("What's left out")
    S.append(dict(type="cards",t0=t,kicker="What's left out",title="Claude organises. The rest, dedicated tools.",cards=[
        dict(ck="Claude",nm="Organises",job="Writes, checks, remembers",pts=["Reads data via connector"],dark=True,at=c("Claude organises")),
        dict(ck="Dedicated tools",nm="The rest",job="Registration and ticketing",pts=["QR code check-in","Payments, attendee apps"],at=c("But for online"))],
        foot="You don't need another AI: <b>you need a well set-up office.</b>",footAt=c("The message of this")))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 10",title="An events office.",next="Next chapter: Leonardo AI."))
    return S

@chapter("11a")
def ch11a(c):
    S=[dict(type="title",t0=0,kicker="AI at Work · Chapter 11",lines=["Leonardo AI,","the visual studio."],sub="Images and video in detail.")]
    t=c.scene("How does it work")
    S.append(dict(type="steps",t0=t,kicker="How it works",steps=[
        dict(h="Describe",p="the image in words",at=c("You describe")),dict(h="Choose",p="a model and a format",at=c("choose a model")),
        dict(h="Generate",p="a few variants",at=c("and Leonardo generates")),dict(h="Refine",p="retouch, upscale, animate",at=c("Then you can"))]))
    t=c.scene("Three things to know")
    S.append(dict(type="list",t0=t,kicker="Good to know",title="Three things.",items=[
        dict(text="It's an aggregator",sub="many different models",at=c("it's an aggregator")),dict(text="Every generation costs tokens",at=c("every generation")),
        dict(text="On paid plans, images are private",at=c("and on paid"))]))
    t=c.scene("The workspace has six")
    S.append(dict(type="list",t0=t,kicker="The workspace",title="Six tools.",compact=True,items=[
        dict(text="Image",tool="prompt and model",at=c("Image, where")),dict(text="Flow State",tool="dozens of variants",at=c("Flow State")),
        dict(text="Editor",tool="edits in words",at=c("The editor")),dict(text="Upscaler",tool="resolution",at=c("The upscaler")),
        dict(text="Video",tool="animates an image",at=c("Video, to")),dict(text="Blueprints",tool="ready-made flows",at=c("And Blueprints"))]))
    t=c.scene("There are many image models")
    S.append(dict(type="list",t0=t,kicker="Images",title="A model for every speciality.",compact=True,items=[
        dict(text="Lucid Origin",tool="All-rounder",at=c("Lucid Origin")),dict(text="Lucid Realism",tool="Photorealism",at=c("Lucid Realism")),
        dict(text="Nano Banana",tool="Edits in words",at=c("Nano Banana")),dict(text="Seedream 4.0",tool="Native 4K",at=c("Seedream")),
        dict(text="Ideogram 3.0",tool="Readable text",at=c("Ideogram")),dict(text="GPT Image",tool="Editing and mockups",at=c("GPT Image")),
        dict(text="Flux 2 Pro",tool="Faithful colours",at=c("Flux")),dict(text="Phoenix",tool="Vector style",at=c("And Phoenix"))]))
    t=c.scene("For video, too")
    S.append(dict(type="list",t0=t,kicker="Video",title="A wide choice.",sub="Video starts from an image: it becomes the first frame.",compact=True,items=[
        dict(text="Veo 3.1",tool="Advertising",at=c("Veo")),dict(text="Kling 3.0",tool="Cinematic camera",at=c("Kling")),
        dict(text="Kling Omni",tool="Video editing",at=c("Kling Omni")),dict(text="Seedance",tool="Several consistent scenes",at=c("Seedance")),
        dict(text="MiniMax",tool="Native audio",at=c("MiniMax")),dict(text="LTX-2",tool="4K",at=c("LTX")),dict(text="Motion 2.0",tool="Social teasers",at=c("And Motion"))]))
    t=c.scene("How do you choose, in practice")
    S.append(dict(type="list",t0=t,kicker="In practice",title="How to choose.",compact=True,items=[
        dict(text="Concepts and moodboards",tool="Lucid Origin",at=c("For concepts")),dict(text="Photorealistic setting",tool="Realism or Flux",at=c("For a photorealistic")),
        dict(text="Fixing a detail",tool="Nano Banana",at=c("To fix a detail")),dict(text="Poster with text",tool="Ideogram",at=c("For a poster")),
        dict(text="Print and advertising",tool="Seedream 4K",at=c("For print")),dict(text="Social teaser",tool="Motion",at=c("For a social")),
        dict(text="Video with the product",tool="Veo or Kling",at=c("For an advertising"))]))
    t=c.scene("An image prompt has six")
    S.append(dict(type="quote",t0=t,kicker="The prompt",title="Six blocks.",sub="Subject, setting, light, framing, style, format. Models work best in English: Claude can translate it.",label="Prompt",segs=[
        c.seg("a modern living","fabric sofa,","A modern living room with a low bouclé fabric sofa, "),
        c.seg("in front of a large","oak floor,","in front of a large window overlooking the lake, oak floor, "),
        c.seg("soft morning light","warm tones,","soft morning light, warm tones, "),
        c.seg("shot at eye","eye level,","wide-angle shot at eye level, "),
        c.seg("editorial interior","minimal, photorealistic,","editorial interior photography, minimal, photorealistic, "),
        c.seg("sixteen by nine","nine format.","16:9 format.")]))
    t=c.scene("Text alone isn't enough")
    S.append(dict(type="list",t0=t,kicker="For consistency",title="Reference images.",items=[
        dict(text="Style",sub="make it like this photo",at=c("style references")),dict(text="Content",sub="shape and composition",at=c("content references")),
        dict(text="Character",sub="the same subject across images",at=c("and character references")),dict(text="Touch-ups",sub="edits, upscaling, format expansion",at=c("Then there are"))]))
    S.append(dict(type="outro",t0=c.dur+.3,kicker="Chapter 11",title="Leonardo AI.",next="Part two: costs, pipeline and things to watch."))
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
