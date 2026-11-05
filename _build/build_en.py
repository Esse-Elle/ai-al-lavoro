#!/usr/bin/env python3
"""Genera en.html (versione inglese) da index.html. Per aggiungere un capitolo inglese:
mettere audio_en/NN.mp3, video_en/NN.mp4 + .jpg, slide in slides_en/ e aggiornare i dati EN qui sotto."""
import re, os, json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s=open(os.path.join(ROOT,"index.html"),encoding="utf-8").read()

# ---------- dati inglesi ----------
TR_ALL=[
 ("01","Introduction and overview","Why AI in marketing, how a generative AI thinks and the five tools: ChatGPT, Claude, Gemini, Perplexity and Leonardo.",1),
 ("02","The prompt","Role, context, task and format. Three tricks and a pipeline from trends to posts.",16),
 ("03","Three side by side","ChatGPT, Claude and Gemini: what they have in common and when to use which.",21),
 ("04a","Inside Claude","The eight building blocks, where to use Claude, desktop or browser, the single conversation and the workspace.",26),
 ("04b","Inside Claude, part two","How Claude works, permissions, models and tokens, seven habits to use less.",34),
 ("05","Working well","Projects, connected folder, instructions, artifact or file, the golden rule and Claude Design.",42),
 ("06a","Skills and agents","What skills are, the marketplace, custom skills and agents.",53),
 ("06b","Skills and agents, part two","Connectors, scheduled tasks, Claude Code, security and the product launch pipeline.",62),
 ("07","The ideal setup","Ten moves, personal instructions, memory, privacy and mistakes to avoid.",70),
 ("08","Automations","The five moves of every automation, the invoice example, other cases and six golden rules.",75),
 ("09","Trust","The four-step verification method.",86),
 ("10","An events office","A digital team built with a project, skills, agents and scheduled tasks.",90),
 ("11a","Leonardo AI","Tools, image and video models, how to choose and how to write the prompt.",101),
 ("11b","Leonardo AI, part two","Costs, the pipeline from idea to video and what to watch out for.",109),
 ("12","Closing","Five takeaways and the first step to take by tomorrow.",88)]
EN_AUDIO={"02":151,"03":90,"04a":196,"07":117,"09":35,"11b":82,"12":73}            # tracce inglesi pronte: durata in secondi
EN_VIDEO={"02":[["02",154]],"03":[["03",93]],"04":[["04a",199]],"07":[["07",120]],"09":[["09",38]],"11":[["11b",85]],"12":[["12",76]]}
PARTIAL={"04":" Part 1 of 2: part 2 coming soon.","11":" Part 2 of 2: part 1 coming soon."}   # videolezioni inglesi pronte
EN_SLIDES=list(range(16,21))   # slide gia' tradotte (slides_en/NNN.jpg)
LEZ_EN=[("01","Introduction and overview","Why AI in marketing, how a generative AI thinks and the five tools."),
 ("02","The prompt","Role, context, task and format. Three tricks and a pipeline from trends to posts."),
 ("03","Three side by side","ChatGPT, Claude and Gemini: what they have in common and when to use which."),
 ("04","Inside Claude","The eight building blocks, where to use Claude, the workspace, how it works, permissions, models and tokens."),
 ("05","Working well","Projects, connected folder, instructions, artifact or file, the golden rule and Claude Design."),
 ("06","Skills and agents","What skills are, the marketplace and agents. Then connectors, scheduled tasks, Claude Code and security."),
 ("07","The ideal setup","Ten moves to start well: personal instructions, memory, privacy and mistakes to avoid."),
 ("08","Automations","The five moves of every automation, the invoice example, other cases and six golden rules."),
 ("09","Trust","The four-step verification method."),
 ("10","An events office","A digital team built with a project, skills, agents and scheduled tasks."),
 ("11","Leonardo AI","Tools, image and video models, how to write the prompt. Then costs, the pipeline from idea to video and what to watch out for."),
 ("12","Closing","Five takeaways and the first step to take by tomorrow.")]
CHAP_EN=[["Overview",6],["Prompt",16],["Comparison",21],["Inside Claude",26],["Working well",42],["Skills and agents",53],["Setup",70],["Automations",75],["Trust",86],["Events office",90],["Leonardo AI",101]]
ALL_DONE = len(EN_AUDIO)==len(TR_ALL)
EN_DATE = "10 November"
EN_DATE_SHORT = "10 Nov"
IT_DUR = dict(zip([t[0] for t in TR_ALL],[302,155,92,219,194,296,213,214,119,290,34,234,216,88,75]))
IT_VID = {"01":[["01",305]],"02":[["02",158]],"03":[["03",95]],"04":[["04a",222],["04b",197]],"05":[["05",299]],"06":[["06a",216],["06b",217]],"07":[["07",122]],"08":[["08",293]],"09":[["09",37]],"10":[["10",237]],"11":[["11a",219],["11b",91]],"12":[["12",78]]}
NOTE_IT = "English audio online on "+EN_DATE+"."

def R(a,b,count=1):
    global s
    n=s.count(a); assert n==count,(a[:70],n); s=s.replace(a,b)
def RX(pat,repl):
    global s
    s2,n=re.subn(pat,repl,s,flags=re.S); assert n==1,(pat[:60],n); s=s2

# ---------- blocchi dati ----------
tr=TR_ALL
def _trk(a,b,c,d):
    en=a in EN_AUDIO
    return " {n:%s,t:%s,d:%s,s:%d,a:%s,it:%s}"%(json.dumps(a),json.dumps(b),json.dumps(c if en else c+" "+NOTE_IT),d,json.dumps(("audio_en/" if en else "audio/")+a+".mp3"),"false" if en else "true")
js_tr="const TRACKS = [\n"+",\n".join(_trk(*t) for t in tr)+"\n];"
RX(r"const TRACKS = \[.*?\n\];",js_tr.replace("\\","\\\\"))
RX(r"const DUR = \[[^\]]*\];","const DUR = "+json.dumps([EN_AUDIO.get(t[0],IT_DUR[t[0]]) for t in tr])+";")
RX(r"const CHAPTERS = \[.*?\]\];","const CHAPTERS = "+json.dumps(CHAP_EN,ensure_ascii=False)+";")
lez=[]
for n,t,d in LEZ_EN:
    o={"n":n,"t":t,"d":d}
    parts=[]; itp=False
    en={x[0]:x for x in EN_VIDEO.get(n,[])}
    for f,du in IT_VID[n]:
        if f in en: parts.append(en[f])
        else: parts.append(["it:"+f,du]); itp=True
    o["p"]=parts
    if itp:
        o["d"]=d+(" "+NOTE_IT if len(parts)==1 or all(x[0].startswith("it:") for x in parts) else " One part still in Italian: English audio online on "+EN_DATE+".")
        o["it"]=True
    lez.append(o)
RX(r"const LEZ=\[.*?\n\];","const LEZ="+json.dumps(lez,ensure_ascii=False).replace("\\","\\\\")+";")

# ---------- percorsi ----------
R('audio.src = src("audio/"+TRACKS[i].n+".mp3")','audio.src = src(TRACKS[i].a)')
R('saveFile("audio/"+tr.n+".mp3","L\'AI al lavoro "+tr.n+" "+tr.t+".mp3")','saveFile(tr.a,"AI at Work "+tr.n+" "+tr.t+(tr.it?" (IT audio)":"")+".mp3")')
R('vid.poster="video/"+f+".jpg"; vid.src="video/"+f+".mp4";','const VP=x=>x.startsWith("it:")?"video/"+x.slice(3):"video_en/"+x; vid.poster=VP(f)+".jpg"; vid.src=VP(f)+".mp4";')
R("""style.backgroundImage='url("video/'+l.p[0][0]+'.jpg")'""","""style.backgroundImage='url("'+(l.p[0][0].startsWith("it:")?"video/"+l.p[0][0].slice(3):"video_en/"+l.p[0][0])+'.jpg")'""")
R('const pad = n => String(n).padStart(3,"0");','const pad = n => String(n).padStart(3,"0"); const SLEN='+json.dumps(EN_SLIDES)+'; const SP = n => (SLEN.includes(n)?"slides_en/":"slides/")+pad(n)+".jpg";')
R('img.src = src("slides/"+pad(slide)+".jpg");','img.src = src(SP(slide));')
R('pre.src=src("slides/"+pad(slide+1)+".jpg");','pre.src=src(SP(slide+1));')
R('store.get("podcast-pos")','store.get("podcast-pos-en")',2)
R('store.set("podcast-pos",','store.set("podcast-pos-en",')

# ---------- testi ----------
T=[('<html lang="it">','<html lang="en">'),("<title>L'AI al lavoro · Podcast</title>","<title>AI at Work · Podcast</title>"),
 ("<span>Formazione AI · Marketing</span>","<span>AI training · Marketing</span>"),
 ("Podcast e videolezioni · Ottobre 2026","Podcast and video lessons · October 2026"),
 ("<h1>L'AI al lavoro</h1>","<h1>AI at Work</h1>"),
 ("La formazione AI per il marketing, da ascoltare in macchina, in pausa o mentre sistemi la posta.","AI training for marketing, to listen to in the car, on a break or while you sort out your inbox."),
 ("<b>12</b>capitoli","<b>12</b>chapters"),("</b>videolezioni</div>","</b>video lessons</div>"),("<b>15</b>tracce","<b>%d</b>%s"%(len(tr),"tracks" if len(tr)>1 else "track")),
 ("</b>di ascolto</div>","</b>of listening</div>"),("<div><b>112</b>slide</div>","<div><b>112</b>slides</div>"),
 ('$("vidcount").textContent=ready.length;','$("vidcount").textContent=ready.length; if(ready.length===1) $("vidcount").nextSibling.textContent="video lesson";'),
 ("Ascolta dall'inizio","Listen from the start"),('href="#videolezioni">Guarda le videolezioni','href="#videolezioni">Watch the video lessons'),
 ("Sfoglia la presentazione","Browse the presentation"),("Video di introduzione al corso","Course intro video"),
 ('<span id="vidSoundLbl">Attiva l\'audio</span>','<span id="vidSoundLbl">Sound on</span>'),
 ('<h2 id="h-guarda">Guarda le videolezioni</h2>','<h2 id="h-guarda">Watch the video lessons</h2>'),
 ("Dodici capitoli raccontati in motion graphic, pochi minuti ciascuno. Guardali in fila dal primo o scegli quello che ti serve.",
  "Twelve chapters told in motion graphics, a few minutes each. Watch them in order or pick the one you need."+("" if ALL_DONE else " Lessons marked “Italian audio” switch to English on "+EN_DATE+".")),
 ('aria-label="Videolezione"','aria-label="Video lesson"'),('<div class="now" id="vNow">Capitolo 02</div>','<div class="now" id="vNow">Chapter 02</div>'),
 ('<h2 id="h-ascolta">Ascolta</h2>','<h2 id="h-ascolta">Listen</h2>'),
 ("Le tracce vanno in sequenza: alla fine di una parte subito la successiva. Riprendi da dove avevi lasciato.",
  "Tracks play in sequence: when one part ends, the next one starts. Pick up where you left off."+("" if ALL_DONE else " Tracks marked “Italian audio” switch to English on "+EN_DATE+".")),
 ('aria-label="Lettore"','aria-label="Player"'),('<div class="now" id="pNow">Traccia 1 di 15</div>','<div class="now" id="pNow">Track 1</div>'),
 ('>Posizione</label>','>Position</label>'),('aria-label="Traccia precedente"','aria-label="Previous track"'),('aria-label="Indietro di 15 secondi"','aria-label="Back 15 seconds"'),
 ('aria-label="Riproduci"','aria-label="Play"'),('aria-label="Avanti di 30 secondi"','aria-label="Forward 30 seconds"'),('aria-label="Traccia successiva"','aria-label="Next track"'),
 ('aria-label="Velocità di riproduzione"','aria-label="Playback speed"'),("Vai alle slide del capitolo","Go to the chapter slides"),
 ('<h2 id="h-deck">La presentazione</h2>','<h2 id="h-deck">The presentation</h2>'),
 ("Le 112 slide del corso. Usa le frecce, il cursore o i capitoli per muoverti.","The 112 slides of the course. Use the arrows, the slider or the chapters to move around."+("" if ALL_DONE else " Slides already translated are in English, the others are still in Italian.")),
 ('alt="Slide 1 di 112"','alt="Slide 1 of 112"'),
 ('aria-label="Slide precedente"','aria-label="Previous slide"',2),('aria-label="Slide successiva"','aria-label="Next slide"',2),
 (">Scorri le slide</label>",">Scroll through the slides</label>"),(">Schermo intero</button>",">Full screen</button>"),
 ("Scarica il PowerPoint","Download the PowerPoint"),("Scarica il PDF","Download the PDF"),("Scarica tutti gli audio","Download all audio"),
 ("Il PowerPoint originale si scarica dalla versione condivisa su OneDrive. Qui trovi il PDF con le stesse 112 slide.","The original PowerPoint can be downloaded from the version shared on OneDrive. Here you'll find the PDF with the same 112 slides."),
 ("Colombini Group · Formazione AI per il Marketing · Ottobre 2026","Colombini Group · AI training for Marketing · October 2026"),
 ("Voce generata con AI a partire dallo script del corso","Voice generated with AI from the course script"),
 ('d.textContent="Scarica MP3"','d.textContent="Download MP3"'),
 ('"Traccia "+(cur+1)+" di "+TRACKS.length+" · "+tr.n','"Track "+(cur+1)+" of "+TRACKS.length+" · "+tr.n'),
 ('audio.paused?"Riproduci":"Pausa"','audio.paused?"Play":"Pause"'),
 ('"Riprendi da "','"Resume from "'),
 ('''$("vidSoundLbl").textContent = on ? "Disattiva l'audio" : "Attiva l'audio";''','''$("vidSoundLbl").textContent = on ? "Sound off" : "Sound on";'''),
 ('''$("vidSoundLbl").textContent="Attiva l'audio";''','''$("vidSoundLbl").textContent="Sound on";'''),
 ('img.alt = "Slide "+slide+" di "+SLIDES;','img.alt = "Slide "+slide+" of "+SLIDES;'),
 ('"Il download non è disponibile in questa vista. Apri la pagina su claude.ai."','"Download isn\'t available in this view. Open the page on claude.ai."'),
 ('"Preparo il file…"','"Preparing the file…"'),('"File scaricato."','"File downloaded."'),('"Non sono riuscito a scaricare il file. Riprova tra poco."','"The file couldn\'t be downloaded. Try again shortly."'),
 ('"Capitolo "+l.n+" · videolezione"+(multi?" · parte "+(pi+1)+" di "+l.p.length:"")','"Chapter "+l.n+" · video lesson"+(multi?" · part "+(pi+1)+" of "+l.p.length:"")'),
 ('(multi&&pi>0?", seconda parte":"")','(multi&&pi>0?", part two":"")'),('"Durata "+fmt','"Length "+fmt'),
 ('nx="Poi: seconda parte"','nx="Next: part two"'),('"Poi: "+LEZ[j].t : "Altre lezioni in arrivo"','"Next: "+LEZ[j].t : "More lessons coming soon"'),
 ('.textContent="Capitolo "+l.n;','.textContent="Chapter "+l.n;'),('" parti, una dopo l\'altra"','" parts, back to back"'),
 ('"Guarda il capitolo "','"Watch chapter "'),('tag.textContent="In arrivo"','tag.textContent="Coming soon"'),
]
for x in T:
    if len(x)==3: R(x[0],x[1],x[2])
    else: R(x[0],x[1])
# download: finche' non c'e' il deck inglese completo, i file restano quelli italiani
if not ALL_DONE:
    R('<div class="dl" id="dlRow">','<p class="note">The downloadable PowerPoint, PDF and audio are still the Italian versions.</p>\n    <div class="dl" id="dlRow">')
    R("Download the PowerPoint","Download the PowerPoint (IT)"); R("Download the PDF","Download the PDF (IT)"); R("Download all audio","Download all audio (IT)")
    R('"files/L-AI-al-lavoro_audio.zip","L\'AI al lavoro - audio.zip"','"files/L-AI-al-lavoro_audio.zip","L\'AI al lavoro - audio IT.zip"')

# badge "Italian audio"
if "in ascolto" in s: s=s.replace("in ascolto","now playing")
R('b.querySelector(".vt").textContent=l.t;','b.querySelector(".vt").textContent=l.t; if(l.it){ const it=document.createElement("span"); it.className="itag"; it.textContent="IT audio · EN "+'+json.dumps(EN_DATE_SHORT)+'; b.querySelector(".vtx").appendChild(it); }')
R('b.querySelector(".t").textContent = tr.t;','b.querySelector(".t").textContent = tr.t; if(tr.it){ const it=document.createElement("span"); it.className="itag"; it.textContent="IT audio"; b.querySelector(".t").appendChild(it); }')
R('.vcard .vp{','.itag{display:inline-block;margin:6px 0 0 0;font-size:.68rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);border:1px solid var(--accent);border-radius:999px;padding:2px 8px}\n.trk .t .itag{margin-left:8px;vertical-align:middle}\n.vcard .itag{display:table}\n.vcard .vp{')
# selettore lingua: EN attivo
s=s.replace('<a href="index.html" class="lg" aria-current="true" lang="it">IT</a><a href="en.html" class="lg" lang="en">EN</a>',
            '<a href="index.html" class="lg" lang="it">IT</a><a href="en.html" class="lg" aria-current="true" lang="en">EN</a>')
s=s.replace('aria-label="Lingua"','aria-label="Language"')
left=[w for w in ["Capitolo","Scarica","Riproduci","videolezione","Traccia ","Guarda ","In arrivo","Ascolta","Attiva l'"] if w in s.split("<script")[0]+"".join(s.split("<script")[1:])]
open(os.path.join(ROOT,"en.html"),"w",encoding="utf-8").write(s)
print("en.html ok; residui:",left)
