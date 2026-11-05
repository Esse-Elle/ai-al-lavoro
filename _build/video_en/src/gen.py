#!/usr/bin/env python3
"""Genera le composizioni dei video per capitolo a partire dai tempi parola per parola."""
import json, re, sys, os, unicodedata

def fix(w):
    try: return w.encode('latin1').decode('utf8')
    except Exception: return w

def norm(w):
    w = fix(w).lower().replace('’', "'")
    w = re.sub(r"[^0-9a-zàèéìíòóùú']", "", w)
    return w

class Cues:
    def __init__(self, k):
        d = json.load(open(f"ts/{k}.json"))
        self.dur = d["dur"]
        self.words = [(norm(w), a, b) for w, a, b in d["w"]]
        self.anchor = 0
    def find(self, phrase, frm=None):
        toks = [norm(x) for x in phrase.split() if norm(x)]
        start = self.anchor if frm is None else frm
        n = len(self.words)
        for i in range(start, n - len(toks) + 1):
            if all(self.words[i + j][0] == toks[j] for j in range(len(toks))):
                return i
        raise KeyError(f"frase non trovata: {phrase!r} da {start}")
    def __call__(self, phrase, lead=0.12):
        i = self.find(phrase)
        return round(max(0, self.words[i][1] - lead), 3)
    def end(self, phrase):
        toks = [x for x in phrase.split() if norm(x)]
        i = self.find(phrase)
        return round(self.words[i + len(toks) - 1][2], 3)
    def scene(self, phrase):
        i = self.find(phrase)
        self.anchor = i
        return round(max(0, self.words[i][1] - 0.35), 3)
    def seg(self, first, last, text=None):
        a = self(first, 0.05); b = self.end(last)
        return {"a": a, "b": b, "text": text}

CH = {}
def chapter(k):
    def deco(f): CH[k] = f; return f
    return deco

def sentences_segs(c, text):
    """text diviso in frasi; ogni frase digitata tra inizio e fine nella voce"""
    out = []
    pos = c.anchor
    for s in [x for x in re.split(r'(?<=[.!?:;])\s+', text) if x.strip()]:
        ws = [w for w in s.split() if norm(w)]
        i = c.find(" ".join(ws[:2]), pos)
        j = i + len(ws) - 1
        out.append({"a": round(c.words[i][1] - 0.05, 3), "b": round(c.words[j][2], 3), "text": s + " "})
        pos = j
    return out

# ---------------------------------------------------------------- capitoli
@chapter("01")
def ch01(c):
    S = []
    S.append(dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 01", lines=["Introduzione", "e panorama."], sub="La formazione AI per il marketing."))
    t = c.scene("Partiamo dal perché")
    S.append(dict(type="statement", t0=t, kicker="Nel marketing il tempo se ne va in due modi", lines=[dict(text="Creare contenuti.", at=c("creare contenuti")), dict(text="Gestire il ripetitivo.", soft=True, at=c("gestire operazioni"))], small="L'AI aiuta su entrambi, senza tradire il brand.", smallAt=c("L'intelligenza artificiale")))
    t = c.scene("Alla fine di questo ascolto")
    S.append(dict(type="list", t0=t, kicker="Alla fine dell'ascolto", title="Tre cose in mano.", items=[dict(text="Quale AI usare per cosa", at=c("Primo: saprete")), dict(text="Claude, impostato bene dal primo giorno", at=c("Secondo: conoscerete")), dict(text="Un metodo per automatizzare da soli", at=c("Terzo: avrete"))]))
    t = c.scene("Il percorso è in undici capitoli")
    S.append(dict(type="list", t0=t, kicker="Il percorso", title="Undici capitoli.", compact=True, mark="dot", items=[dict(text="Il panorama e il prompt", at=c("Il panorama")), dict(text="ChatGPT, Claude e Gemini", at=c("Il confronto")), dict(text="Dentro Claude e lavorare bene", at=c("Poi entriamo")), dict(text="Skill, agenti e il setup ideale", at=c("skill e agenti")), dict(text="Automazioni e fiducia", at=c("Poi le automazioni")), dict(text="Un ufficio eventi e Leonardo AI", at=c("un ufficio eventi"))]))
    t = c.scene("E prima di cominciare")
    S.append(dict(type="statement", t0=t, kicker="Da tenere a mente", lines=[dict(text="L'AI non sostituisce le persone.", at=c("l'AI non sostituisce")), dict(text="Potenzia quelle che la usano.", soft=True, at=c("Potenzia quelle"))]))
    t = c.scene("Capitolo uno: il panorama")
    S.append(dict(type="statement", t0=t, kicker="Capitolo 01", lines=[dict(text="Il panorama.", at=t + .4)], small="Il mondo dell'AI corre.", smallAt=c("il mondo dell'AI corre")))
    t = c.scene("Dalla prima formazione")
    S.append(dict(type="list", t0=t, kicker="Da marzo a oggi", title="È cambiato quasi tutto.", mark="dot", items=[dict(text="Claude: Opus 5.5 e Sonnet 5.5", at=c("Claude è passato")), dict(text="ChatGPT: la famiglia GPT-6", at=c("ChatGPT è passato")), dict(text="Gemini: serie 3, in arrivo Gemini 4", at=c("Gemini lavora")), dict(text="Claude Design, oggi dentro Claude", at=c("È nato Claude Design")), dict(text="Una sola conversazione, niente più Chat e Cowork", at=c("E nell'app di Claude"))]))
    t = c.scene("Ve lo racconto")
    S.append(dict(type="statement", t0=t, lines=[dict(text="Impariamo il metodo,", at=c("impariamo il metodo")), dict(text="non i pulsanti.", soft=True, at=c("non i pulsanti"))], small="I pulsanti cambiano ogni mese. Il metodo resta.", smallAt=c("I pulsanti cambiano")))
    t = c.scene("E il metodo parte")
    S.append(dict(type="list", t0=t, kicker="Come ragiona un'AI", title="Completa il testo nel modo più probabile.", items=[dict(text="Dove mancano informazioni, riempie", sub="con risposte generiche, a volte inventate", at=c("Dove mancano")), dict(text="Più contesto, più il risultato è vostro", at=c("Più contesto")), dict(text="Va sempre riletta", sub="un collaboratore brillante, non un oracolo", at=c("E va sempre"))]))
    t = c.scene("Immaginatela come")
    S.append(dict(type="statement", t0=t, lines=[dict(text="Bravissima,", at=c("bravissima")), dict(text="al primo giorno di lavoro.", soft=True, at=c("al suo primo"))], small="Capace e veloce, ma non conosce né l'azienda né i clienti.", smallAt=c("capace, veloce")))
    t = c.scene("Detto questo, vediamo")
    sp = [c("ChatGPT, di OpenAI"), c("Claude, di Anthropic"), c("Gemini, di Google"), c("Perplexity è il"), c("Leonardo AI è lo")]
    S.append(dict(type="cards", t0=t, kicker="Il panorama AI", title="Cinque strumenti, cinque mestieri.", spot=sp, cards=[
        dict(ck="Testo e idee", nm="ChatGPT", by="di OpenAI", job="Il generalista", pts=["Brainstorming e bozze", "Immagini in chat"], at=t + .8),
        dict(ck="Testo e lavoro", nm="Claude", by="di Anthropic", job="Il collaboratore che ragiona", pts=["Testi nel tono del brand", "Lavora su file e strumenti"], dark=True, at=t + 1.1),
        dict(ck="Ecosistema Google", nm="Gemini", by="di Google", job="L'assistente di Gmail e Drive", pts=["Riassume thread e file", "NotebookLM"], at=t + 1.4),
        dict(ck="Ricerca", nm="Perplexity", by="di Perplexity AI", job="Il ricercatore", pts=["Trend e competitor", "Fonti cliccabili"], at=t + 1.7),
        dict(ck="Immagini e video", nm="Leonardo AI", by="piattaforma di modelli", job="Lo studio visivo", pts=["Moodboard e concept", "Teaser video"], at=t + 2.0)]))
    t = c.scene("Mettiamola in pratica")
    S.append(dict(type="list", t0=t, kicker="In pratica", title="Chi fa cosa.", compact=True, items=[
        dict(text="Trend, dati e competitor", tool="Perplexity", at=c("Se dovete trovare")),
        dict(text="Copy, comunicati, schede prodotto", tool="Claude", at=c("Se dovete scrivere")),
        dict(text="Lavoro dentro Gmail o Drive", tool="Gemini", at=c("Se il lavoro")),
        dict(text="Brainstorming lampo, immagine al volo", tool="ChatGPT", at=c("Per un brainstorming")),
        dict(text="Moodboard e ambientazioni", tool="Leonardo", at=c("Per moodboard")),
        dict(text="Automatizzare un lavoro ripetitivo", tool="Claude", at=c("E per automatizzare"))]))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 01", title="Il panorama.", next="Prossimo capitolo: il prompt."))
    return S

@chapter("02")
def ch02(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 02", lines=["Non esiste", "l'AI migliore."], sub="Esiste quella giusta per il compito.", subAt=c("Esiste quella"))]
    t = c.scene("Capitolo due")
    S.append(dict(type="statement", t0=t, kicker="Capitolo 02", lines=[dict(text="Il prompt.", at=t + .4), dict(text="Come si parla a un'AI.", soft=True, at=c("cioè come"))], small="Qualunque strumento scegliate, tutto parte da lì.", smallAt=c("Qualunque strumento")))
    t = c.scene("Facciamo subito un esempio")
    S.append(dict(type="app", t0=t, kicker="Prima", title="Un prompt vago.", sub="Un testo che andrebbe bene per qualsiasi marchio.", nav="rec", blocks=[
        dict(k="bubble", text="Scrivi un post Instagram per la nuova cucina", at=c("scrivi un post")),
        dict(k="reply", text="Scopri la nuova cucina: design, funzionalità e stile per la tua casa! #cucina #design #casa", type=[c("ottengo un testo"), c("ottengo un testo") + 3.5]),
        dict(k="spacer"), dict(k="composer", chips=[dict(text="Manuale", sel=True)])]))
    t = c.scene("Se invece scrivo")
    full = "Sei il social media manager di un brand di cucine di alta gamma. Scrivi tre varianti di caption per il lancio di un nuovo modello. Il pubblico sono architetti e famiglie. Tono elegante, massimo 300 caratteri, tre hashtag."
    S.append(dict(type="app", t0=t, kicker="Dopo", title="Un prompt completo.", sub="Il risultato cambia completamente.", nav="rec", blocks=[
        dict(k="label", text="Nuova conversazione"),
        dict(k="field", text=full, focus=True, type=[c("Sei il social"), c.end("tre hashtag")], h=250),
        dict(k="bars", at=c("il risultato cambia"), w=[100, 92, 78, 55]),
        dict(k="spacer"), dict(k="composer", chips=[dict(text="Manuale", sel=True)])]))
    t = c.scene("In quella seconda richiesta")
    S.append(dict(type="list", t0=t, kicker="I quattro ingredienti", title="Ogni buon prompt.", items=[
        dict(text="Il ruolo", sub="chi deve essere l'AI", at=c("Il ruolo")), dict(text="Il contesto", sub="la situazione, il brand, il pubblico", at=c("Il contesto")),
        dict(text="Il compito", sub="cosa deve fare, esattamente", at=c("Il compito")), dict(text="Il formato", sub="come volete il risultato", at=c("E il formato"))]))
    t = c.scene("A questi aggiungo")
    S.append(dict(type="list", t0=t, kicker="Tre trucchi", title="Funzionano sempre.", items=[
        dict(text="Dare un ruolo preciso", sub="Sei il copywriter del nostro brand", at=c("Il primo:")),
        dict(text="Mostrare degli esempi", sub="due o tre testi approvati: il trucco più potente", at=c("Il secondo:")),
        dict(text="Iterare nella stessa conversazione", sub="più breve, meno aggettivi, una call to action", at=c("Il terzo:"))]))
    t = c.scene("E un bonus")
    S.append(dict(type="statement", t0=t, kicker="Bonus", lines=[dict(text="Prima di scrivere,", at=c("prima di scrivere")), dict(text="chiedimi cosa ti serve sapere.", soft=True, at=c("chiedimi cosa"))], small="Vi evita metà delle correzioni.", smallAt=c("vi evita")))
    t = c.scene("Ora vediamo come")
    S.append(dict(type="pipeline", t0=t, kicker="Pipeline", title="Tre tendenze 2027, tre post.", steps=[
        dict(tool="Perplexity", text="Ricerca approfondita: tre tendenze con fonti", at=c("Primo passo")),
        dict(tool="Voi", you=True, text="Aprite le fonti e scartate il debole", at=c("Secondo passo")),
        dict(tool="Claude", text="Un post per tendenza, nel tono del brand", at=c("Terzo passo")),
        dict(tool="Leonardo AI", text="Un'immagine di concept per post", at=c("Quarto passo")),
        dict(tool="Claude Design", text="Impaginazione 4:5 nei colori del brand", at=c("Quinto passo"))],
        foot="Ogni strumento fa ciò che sa fare meglio. La revisione finale è vostra.", footAt=c("Ogni strumento fa")))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 02", title="Il prompt.", next="Prossimo capitolo: tre a confronto."))
    return S

@chapter("03")
def ch03(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 03", lines=["Tre a", "confronto."], sub="ChatGPT, Claude e Gemini.")]
    t = c.scene("La prima cosa da sapere")
    S.append(dict(type="list", t0=t, kicker="In comune", title="Si assomigliano più di quanto sembri.", mark="check", items=[
        dict(text="Chat con ricerca web e file", at=c("Tutti e tre hanno una chat")),
        dict(text="Progetti con istruzioni e documenti", at=c("Tutti e tre hanno progetti")),
        dict(text="Memoria e app collegate", at=c("Tutti e tre hanno una memoria")),
        dict(text="Agenti per compiti in più passaggi", at=c("e hanno agenti")),
        dict(text="Circa venti dollari al mese", at=c("E il piano individuale"))]))
    t = c.scene("La differenza sta")
    S.append(dict(type="compare", t0=t, kicker="La differenza", title="Il carattere e il modo di lavorare.", cols=["ChatGPT", "Claude", "Gemini"], me=1, rows=[
        dict(label="Carattere", vals=["Versatile e veloce", "Riflessivo e preciso", "Integrato con Google"], at=c("ChatGPT è versatile")),
        dict(label="Punto di forza", vals=["Immagini in chat", "Testi lunghi, grafiche e layout", "Gmail, Drive e Documenti"], at=c("i testi lunghi")),
        dict(label="Lavora su", vals=["App del suo ecosistema", "Cartelle, connettori, browser", "Immagini e video Google"], at=c("e lavora su cartelle"))]))
    t = c.scene("Quindi, quando uso cosa")
    S.append(dict(type="list", t0=t, kicker="Quando uso cosa", title="Il compito decide.", items=[
        dict(text="Velocità, un'immagine al volo", tool="ChatGPT", at=c("ChatGPT quando")),
        dict(text="Lavoro dentro Gmail, Drive, Documenti", tool="Gemini", at=c("Gemini quando")),
        dict(text="Testo curato, documenti lunghi, azioni", tool="Claude", at=c("Claude quando")),
        dict(text="Nel dubbio, stessa richiesta su due", tool="Confronto", at=c("E nel dubbio"))]))
    t = c.scene("Non è una guerra")
    S.append(dict(type="statement", t0=t, lines=[dict(text="Non è una guerra", at=c("Non è una guerra")), dict(text="tra tifoserie.", soft=True, at=c("tra tifoserie"))], small="Chi sa usare bene uno strumento impara gli altri in un'ora.", smallAt=c("Chi sa usare")))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 03", title="Tre a confronto.", next="Prossimo capitolo: dentro Claude."))
    return S

@chapter("04a")
def ch04a(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 04", lines=["Dentro", "Claude."], sub="Come è fatto e dove si usa.")]
    t = c.scene("Per orientarci")
    S.append(dict(type="list", t0=t, kicker="La mappa", title="Otto mattoni.", sub="Si parte da chat e progetti.", compact=True, items=[
        dict(text="Chat", tool="si ragiona", at=c("La chat")), dict(text="Progetti", tool="la memoria", at=c("I progetti")),
        dict(text="Artifact", tool="il lavoro finito", at=c("Gli artifact")), dict(text="Attività pianificate", tool="lavorano a orario", at=c("Le attività pianificate")),
        dict(text="Personalizzazione", tool="chi siete", at=c("La personalizzazione")), dict(text="Connettori", tool="le prese", at=c("I connettori")),
        dict(text="Claude Design", tool="il grafico", at=c("Claude Design")), dict(text="Claude Code", tool="il costruttore", at=c("E Claude Code"))]))
    t = c.scene("Dove si usa Claude")
    S.append(dict(type="list", t0=t, kicker="Dove si usa", title="Lo stesso Claude, in più posti.", sub="Account, progetti e artifact sono gli stessi ovunque.", items=[
        dict(text="App desktop", sub="Mac e Windows, la versione completa", at=c("C'è l'app desktop")),
        dict(text="Browser", sub="claude.ai, da qualsiasi computer", at=c("C'è il browser")),
        dict(text="Telefono", sub="chattare, dettare, seguire le attività", at=c("C'è l'app per")),
        dict(text="Claude in Chrome", sub="naviga e agisce sui siti", at=c("C'è Claude in Chrome")),
        dict(text="Excel, PowerPoint, Google Workspace", sub="dentro i file", at=c("Ci sono Claude in Excel"))]))
    t = c.scene("Ma allora, desktop o browser")
    S.append(dict(type="statement", t0=t, kicker="Desktop o browser?", lines=[dict(text="L'app desktop", at=c("l'app desktop è la porta")), dict(text="è la porta verso il computer.", soft=True, at=c("è la porta"))], small="Cartelle, browser integrato e controllo del computer funzionano solo con l'app aperta. Installatela.", smallAt=c("Le cartelle, il browser")))
    t = c.scene("Ora la novità")
    S.append(dict(type="app", t0=t, kicker="La novità", title="Una sola conversazione.", sub="Scrivete e basta: Claude risponde o si mette al lavoro.", nav="rec", panel=[
        dict(k="label", text="Avanzamento"), dict(k="psteps", items=[dict(text="Leggo i dati", at=c("si mette al lavoro") + .6), dict(text="Analizzo i risultati", at=c("In Recenti")), dict(text="Scrivo il report", at=c("Non c'è più"))]),
        dict(k="label", text="Output", at=c("Per una ricerca")), dict(k="outfile", text="Report campagna.docx", at=c("Per una ricerca"))], blocks=[
        dict(k="bubble", text="Prepara il report della campagna di settembre", at=c("Se chiedete un lavoro")),
        dict(k="reply", text="Certo. Leggo gli export e preparo il report.", type=[c("si mette al lavoro"), c("si mette al lavoro") + 2]),
        dict(k="bars", at=c("nella stessa conversazione")), dict(k="spacer"),
        dict(k="chips", items=[dict(text="/deep research", at=c("barra deep research")), dict(text="Research", at=c("si sceglie Research"))]),
        dict(k="composer", chips=[dict(text="Manuale", sel=True)])]))
    t = c.scene("Dove sono finite")
    S.append(dict(type="list", t0=t, kicker="Dove sono finite le cose", title="La nuova mappa.", items=[
        dict(text="Istruzioni generali", sub="Impostazioni / Generali / Istruzioni per Claude", at=c("Le istruzioni generali")),
        dict(text="Cartelle autorizzate", sub="Impostazioni / Cartelle attendibili", at=c("Le cartelle autorizzate")),
        dict(text="Permessi", sub="nel riquadro dove scrivete: Manuale o Auto", at=c("I permessi")),
        dict(text="Vecchie attività", sub="in Recenti", at=c("Le vecchie attività")),
        dict(text="Cancellazioni", sub="Claude chiede sempre prima", at=c("E per i file"))]))
    t = c.scene("Facciamo un giro")
    S.append(dict(type="app", t0=t, kicker="L'area di lavoro", title="Un giro dell'app.", sub="Barra laterale, conversazione, riquadro, avanzamento.", nav="rec", panel=[
        dict(k="label", text="Avanzamento", at=c("A destra")), dict(k="psteps", items=[dict(text="Leggo la cartella", at=c("passo per passo")), dict(text="Scrivo la bozza", at=c("il contesto"))]),
        dict(k="label", text="Contesto", at=c("il contesto")), dict(k="rows", items=[dict(text="Marketing Claude", icon="folder", at=c("cioè cartelle")), dict(text="Mail", at=c("connettori")), dict(text="Tono di voce", at=c("e skill"))]),
        dict(k="label", text="Output", at=c("e gli output")), dict(k="outfile", text="Post lancio.docx", at=c("i file creati"))], blocks=[
        dict(k="bubble", text="Scrivi tre post per il lancio", at=c("Al centro")),
        dict(k="bars", at=c("con le vostre richieste") + .5),
        dict(k="rows", items=[dict(text="Leggere la cartella Marketing?", chip="Consenti", chipOn=c("Consenti o Nega") + .4, at=c("Ogni tanto compare"))]),
        dict(k="spacer"), dict(k="composer", chips=[dict(text="Manuale", sel=True)], at=c("In basso"))],
        cursor=[[c("A sinistra"), -170, 240], [c("Al centro"), 300, 160], [c("Consenti o Nega"), 560, 245], [c("In basso"), 80, 600], [c("la barra per"), 140, 600], [c("e accanto la scelta"), 420, 600], [c("A destra"), 520, 120]]))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 04", title="Dentro Claude.", next="Seconda parte: come lavora Claude."))
    return S

@chapter("04b")
def ch04b(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 04", lines=["Dentro Claude,", "seconda parte."], sub="Come lavora, modelli e token.")]
    t = c.scene("E come lavora Claude")
    S.append(dict(type="steps", t0=t, kicker="Il ciclo di lavoro", side=True, steps=[
        dict(h="Capisce", p="Legge la richiesta e, se serve, chiede.", at=c("Capisce:")), dict(h="Pianifica", p="Scompone il lavoro in passi.", at=c("Pianifica:")),
        dict(h="Usa gli strumenti", p="File, web, connettori.", at=c("Usa gli strumenti")), dict(h="Chiede", p="Aspetta il via libera per le azioni importanti.", at=c("Chiede:")),
        dict(h="Consegna", p="Salva file o artifact e riassume.", at=c("E consegna"))]))
    t = c.scene("Prima di partire, quindi")
    S.append(dict(type="list", t0=t, kicker="Prima di partire", title="Tre scelte.", items=[
        dict(text="Permessi: Manuale per iniziare", sub="Auto solo quando il flusso è collaudato", at=c("I permessi:")),
        dict(text="Dove: una cartella dedicata", sub="mai tutto il disco", at=c("Dove lavora")),
        dict(text="Con cosa: solo ciò che serve", sub="i connettori e le skill di quel lavoro", at=c("E con cosa"))]))
    t = c.scene("Adesso un tema")
    S.append(dict(type="statement", t0=t, kicker="Tempo e soldi", lines=[dict(text="Modelli", at=c("modelli e token")), dict(text="e token.", soft=True, at=c("e token"))]))
    t = c.scene("Il modello è il cervello")
    S.append(dict(type="cards", t0=t, kicker="I modelli", title="Motori di potenza diversa.", cards=[
        dict(ck="Leggero", nm="Haiku", job="Rapido", pts=["Compiti semplici"], at=c("Haiku è rapido")),
        dict(ck="Tutti i giorni", nm="Sonnet", job="Equilibrato", pts=["Il modello di base"], dark=True, at=c("Sonnet è equilibrato")),
        dict(ck="Profondo", nm="Opus", job="Ragionamento", pts=["I lavori seri"], at=c("Opus è per")),
        dict(ck="Autonomo", nm="Fable", job="Progetti lunghi", pts=["Da portare avanti da solo"], at=c("Fable è pensato"))],
        foot="Il numero indica la generazione. <b>L'effort, quanto ragiona.</b>", footAt=c("Il numero accanto")))
    t = c.scene("Il token invece")
    S.append(dict(type="statement", t0=t, kicker="Il token", lines=[dict(text="Un pezzo di parola,", at=c("un pezzo di parola")), dict(text="tre o quattro caratteri.", soft=True, at=c("circa tre"))], small="Tutto si misura in token: richiesta, allegati, ragionamento e risposta.", smallAt=c("Tutto si misura")))
    t = c.scene("E soprattutto: a ogni messaggio")
    S.append(dict(type="statement", t0=t, kicker="Da sapere", lines=[dict(text="A ogni messaggio", at=c("a ogni messaggio")), dict(text="Claude rilegge tutto.", soft=True, at=c("Claude rilegge"))], small="L'ottavo messaggio costa quanto i sette precedenti. Il limite si ricarica ogni cinque ore.", smallAt=c("Pensateci")))
    t = c.scene("Lo stesso vale per i modelli")
    S.append(dict(type="list", t0=t, kicker="Consumo", title="Più potenza, più token.", sub="Opus per riassumere una mail? Come fare la spesa in Formula Uno.", items=[
        dict(text="Haiku", tool="Basso", at=c("Haiku consuma")), dict(text="Sonnet", tool="Medio", at=c("Sonnet medio")),
        dict(text="Opus", tool="Alto", at=c("Opus tanto")), dict(text="Fable", tool="Molto alto", at=c("Fable tantissimo"))]))
    t = c.scene("Come si sceglie, allora")
    S.append(dict(type="list", t0=t, kicker="Come si sceglie", title="Quattro domande.", sub="Partite da Sonnet. Salite solo se la risposta non basta.", items=[
        dict(text="È semplice e veloce?", tool="Haiku", at=c("È semplice")), dict(text="È lavoro di tutti i giorni?", tool="Sonnet", at=c("È lavoro di")),
        dict(text="Devo ragionarci sopra?", tool="Opus", at=c("Devo ragionarci")), dict(text="È lungo e autonomo?", tool="Fable", at=c("È lungo"))]))
    t = c.scene("Sette abitudini")
    S.append(dict(type="list", t0=t, kicker="Consapevolezza", title="Sette abitudini.", mark="check", compact=True, items=[
        dict(text="Modello ed effort adatti al compito", at=c("Scegliete modello")), dict(text="Una chat per argomento", at=c("Una chat per")),
        dict(text="Niente file ricaricati: la cartella", at=c("Non ricaricate")), dict(text="Domande raggruppate", at=c("Raggruppate")),
        dict(text="Risposte brevi quando bastano", at=c("Chiedete risposte")), dict(text="Ricerca approfondita solo se serve", at=c("Usate la ricerca")),
        dict(text="Uno sguardo all'utilizzo", at=c("E una volta"))]))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 04", title="Dentro Claude.", next="Prossimo capitolo: lavorare bene."))
    return S

@chapter("05")
def ch05(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 05", lines=["Lavorare", "bene."], sub="Conta come impostate il lavoro.")]
    t = c.scene("Partiamo dalla chat")
    S.append(dict(type="list", t0=t, kicker="Prima di premere invio", title="Tre scelte cambiano la risposta.", items=[
        dict(text="Il modello, con il suo effort", at=c("il modello con")), dict(text="Gli strumenti che attivate", at=c("gli strumenti che")),
        dict(text="Il progetto in cui vi trovate", at=c("e il progetto"))]))
    t = c.scene("E qualche buona abitudine")
    S.append(dict(type="list", t0=t, kicker="Buone abitudini", title="In chat.", mark="check", items=[
        dict(text="Una chat per argomento", at=c("una chat per")), dict(text="Allegate il materiale", sub="invece di riassumerlo a parole", at=c("allegate il")),
        dict(text="Chiedete le fonti", at=c("chiedete le fonti")), dict(text="Rinominate le chat importanti", at=c("e rinominate"))]))
    t = c.scene("Poi i progetti")
    S.append(dict(type="app", t0=t, kicker="I progetti", title="La memoria del collaboratore.", sub="Si configura una volta, vi conosce sempre.", nav="prj", blocks=[
        dict(k="label", text="Progetti"), dict(k="title", text="Marketing"), dict(k="text", text="Istruzioni e materiali permanenti, in ogni conversazione.", at=c("Un progetto è uno spazio")),
        dict(k="rows", items=[dict(text="Su claude.ai", small="nell'account, condivisibile", at=c("Quelli su claude.ai")), dict(text="Sull'app desktop", small="cartelle, memoria, pianificate", at=c("Quelli sull'app")), dict(text="Collegabili tra loro", at=c("E si possono collegare"))])]))
    t = c.scene("E qui c'è la mossa")
    S.append(dict(type="list", t0=t, kicker="La mossa che cambia tutto", title="Il progetto collegato a una cartella.", sub="Claude lavora sul vostro tavolo, non su copie.", mark="check", items=[
        dict(text="Legge i documenti senza caricarli", at=c("Legge i documenti")), dict(text="Vede sempre l'ultima versione", at=c("Vede sempre")),
        dict(text="Salva lì gli output", at=c("Salva gli output")), dict(text="Fa risparmiare token e tempo", at=c("E vi fa risparmiare"))]))
    t = c.scene("Come organizzare la cartella")
    S.append(dict(type="app", t0=t, kicker="La cartella", title="Una struttura uguale per tutti.", sub="Regole, materiali e output: Claude sa dove guardare.", nav="prj", blocks=[
        dict(k="label", text="Marketing Claude"), dict(k="tree", items=[
            dict(text="00_Leggimi", small="istruzioni, tono, regole", dir=True, at=c("zero zero Leggimi")), dict(text="01_Brand", small="brand book, logo, palette", dir=True, at=c("Una con il brand")),
            dict(text="02_Prodotti", small="cataloghi, schede, listini", dir=True, at=c("Una con i prodotti")), dict(text="03_Esempi approvati", small="testi e post da imitare", dir=True, at=c("Una con gli esempi")),
            dict(text="04_Input", small="brief, export, materiali", dir=True, at=c("Una per gli input")), dict(text="05_Output", small="i lavori di Claude", dir=True, at=c("Una per gli output")),
            dict(text="99_Archivio", small="versioni vecchie", dir=True, at=c("E un archivio"))])]))
    t = c.scene("Il progetto ideale si imposta")
    S.append(dict(type="steps", t0=t, kicker="Il progetto ideale · Sette passi", side=True, steps=[
        dict(h="Create la cartella", short="La cartella", at=c("Create la cartella")), dict(h="Progetti, +, cartella esistente", short="Progetto dalla cartella", at=c("Nell'app desktop")),
        dict(h="Nome e descrizione", short="Nome e descrizione", at=c("Date nome")), dict(h="Le istruzioni", short="Istruzioni", at=c("Scrivete le istruzioni")),
        dict(h="Il progetto del team", p="Se esiste, su claude.ai.", short="Progetto del team", at=c("Collegate, se esiste")), dict(h="Solo ciò che serve", p="Connettori e skill.", short="Connettori e skill", at=c("Attivate solo")),
        dict(h="Il primo test", p="Leggi 00_Leggimi e dimmi cosa hai capito.", short="Primo test", at=c("E fate un primo"))]))
    t = c.scene("Un esempio di istruzioni di progetto")
    txt = "Sei il collaboratore del marketing del brand. Prima di ogni lavoro leggi le cartelle Leggimi e Brand. Usa solo dati presenti nella cartella: se manca qualcosa chiedilo, non inventare. Tono elegante, caldo, frasi brevi, niente superlativi. Salva sempre i lavori nella cartella Output, con nome data, tema e versione. Non sovrascrivere mai un file: crea una nuova versione. Alla fine dimmi cosa hai fatto e dove hai salvato."
    S.append(dict(type="quote", t0=t, kicker="Esempio", title="Istruzioni di progetto.", label="Istruzioni del progetto", segs=sentences_segs(c, txt)))
    t = c.scene("Ora una domanda")
    S.append(dict(type="cards", t0=t, kicker="La domanda di tutti", title="Artifact o file?", cards=[
        dict(ck="Vive dentro Claude", nm="Artifact", job="Si condivide con un link", pts=["Nella sezione Artifact", "Si modifica in Claude"], dark=True, at=c("L'artifact è")),
        dict(ck="Nella vostra cartella", nm="File", job="Un documento vero", pts=["Word, PowerPoint, Excel, PDF", "Si apre con Office"], at=c("Il file invece"))],
        foot="Spesso esistono entrambi: <b>un artifact si esporta, un file si pubblica.</b>", footAt=c("Spesso esistono")))
    t = c.scene("Gli artifact più utili")
    S.append(dict(type="list", t0=t, kicker="Artifact", title="I quattro più utili.", items=[
        dict(text="Docs", sub="documenti da scrivere insieme e commentare", at=c("Docs,")), dict(text="Slides", sub="presentazioni da proiettare o esportare", at=c("Slides,")),
        dict(text="Design", sub="grafiche, mockup e pagine", at=c("Design, cioè")), dict(text="Pagine vive", sub="tracker, calcolatori, dashboard", at=c("E le pagine vive"))]))
    t = c.scene("E adesso una regola")
    S.append(dict(type="statement", t0=t, kicker="La regola d'oro", lines=[dict(text="Claude riscrive", at=c("lo riscrive")), dict(text="il file da zero.", soft=True, at=c("da zero"))], small="Ritoccato a mano e poi rigenerato? Le vostre modifiche spariscono.", smallAt=c("Quindi, se avete")))
    t = c.scene("Le strade sono due")
    S.append(dict(type="list", t0=t, kicker="Due strade", title="Per non perdere lavoro.", items=[
        dict(n="A", text="Chiedete a Claude le modifiche", sub="nella slide 4 accorcia il titolo, nella 7 aggiungi il prezzo", at=c("Strada A")),
        dict(n="B", text="Duplicate e rinominate", sub="lavorate sulla copia: Claude non la toccherà", at=c("Strada B"))]))
    t = c.scene("Chiudiamo il capitolo")
    S.append(dict(type="app", t0=t, kicker="Claude Design", title="Dal brief al layout.", sub="Non sostituisce il grafico: accelera le prime versioni. Per le foto, Leonardo.", nav="art", blocks=[
        dict(k="label", text="Artifact / Design"), dict(k="bubble", text="Locandina per l'evento in showroom, nei colori del brand", at=c("Dal brief")),
        dict(k="rows", items=[dict(text="Mockup di landing page e newsletter", at=c("lo usiamo per mockup")), dict(text="Post social", at=c("post social")), dict(text="Locandine per eventi in showroom", at=c("locandine")), dict(text="Presentazioni nel nostro stile", at=c("e presentazioni"))])]))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 05", title="Lavorare bene.", next="Prossimo capitolo: skill e agenti."))
    return S

@chapter("06a")
def ch06a(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 06", lines=["Skill", "e agenti."], sub="Gli strumenti che potenziano Claude.")]
    t = c.scene("Partiamo dalle skill")
    S.append(dict(type="statement", t0=t, kicker="La skill", lines=[dict(text="Il manuale", at=c("quella del manuale")), dict(text="sullo scaffale.", soft=True, at=c("sullo scaffale"))], small="Metodo, tono, formato. Si attiva da sola o con la barra, in tutti i progetti.", smallAt=c("Si attiva da sola")))
    t = c.scene("Com'è fatta dentro")
    S.append(dict(type="app", t0=t, kicker="Dentro una skill", title="Nessun codice: è un testo.", sub="È la descrizione a decidere quando scatta.", nav="cus", blocks=[
        dict(k="label", text="SKILL.md"),
        dict(k="field", text="name: tono-di-voce\ndescription: usa questa skill quando scrivi copy, post, comunicati o newsletter per il brand", focus=True, type=[c("In alto c'è"), c.end("per il brand")], h=150),
        dict(k="label", text="Il metodo", at=c("Sotto c'è il metodo")),
        dict(k="rows", items=[dict(text="Tono di voce", at=c("il tono di voce")), dict(text="Parole sì e parole no", at=c("le parole sì")), dict(text="Esempi approvati", at=c("gli esempi approvati"))])]))
    t = c.scene("Dove si trovano le skill")
    S.append(dict(type="app", t0=t, kicker="Il marketplace", title="Plugin, connettori, agenti.", sub="Ci si arriva da Customize.", nav="cus", blocks=[
        dict(k="label", text="Customize / Marketplace"),
        dict(k="rows", items=[dict(text="Word, Excel, PowerPoint e PDF", chip="Installa", chip2="Installata", chipOn=c("Trovate skill pronte") + 1.5, at=c("Trovate skill")),
            dict(text="Plugin Marketing", chip="Installa", chip2="Installato", chipOn=c("Brand Voice"), at=c("come i plugin")),
            dict(text="Plugin Brand Voice", chip="Installa", at=c("Brand Voice")), dict(text="Skill del team", small="condivise con tutti", at=c("e le skill che il team"))])]))
    t = c.scene("Ma il vero valore")
    S.append(dict(type="steps", t0=t, kicker="Una skill su misura", side=True, steps=[
        dict(h="Un compito che ripetete", short="Il compito", at=c("Scegliete un compito")), dict(h="Crea una skill che…", short="La richiesta", at=c("Chiedete a Claude")),
        dict(h="Rispondete alle domande", short="Le domande", at=c("Claude vi fa")), dict(h="Esempi buoni e cattivi", short="Gli esempi", at=c("Allegate esempi")),
        dict(h="Provatela su tre casi", short="La prova", at=c("Salvatela")), dict(h="Condividetela", p="Con tutto il team.", short="Il team", at=c("e poi condividetela"))]))
    t = c.scene("Qualche idea per il marketing")
    S.append(dict(type="list", t0=t, kicker="Idee per il marketing", title="Sette skill.", sub="Se doveste sceglierne una: il tono di voce.", compact=True, items=[
        dict(text="Tono di voce", at=c("Una skill per il tono"), hl=c("Se doveste")), dict(text="Comunicato stampa", at=c("Una per il comunicato")),
        dict(text="Scheda prodotto", at=c("Una per la scheda")), dict(text="Post social", at=c("Una per i post")), dict(text="Report di campagna", at=c("Una per il report")),
        dict(text="Presentazioni nel template", at=c("Una per le presentazioni")), dict(text="Brief ad agenzie e fotografi", at=c("E una per i brief"))]))
    t = c.scene("Passiamo agli agenti")
    S.append(dict(type="statement", t0=t, kicker="L'agente", lines=[dict(text="Un collaboratore", at=c("un collaboratore")), dict(text="con la sua scrivania.", soft=True, at=c("con la sua"))], small="Svolge un compito intero in un contesto separato e riporta solo il risultato.", smallAt=c("Claude gli affida")))
    t = c.scene("Un agente è un file")
    S.append(dict(type="list", t0=t, kicker="Un file di ruolo", title="Quattro elementi.", sub="Un progetto con istruzioni di ruolo è già un agente leggero.", items=[
        dict(text="Nome e descrizione", sub="chi è e quando usarlo", at=c("nome e descrizione")), dict(text="Strumenti", sub="file, web, connettori", at=c("gli strumenti che")),
        dict(text="Modello", sub="con cui lavora", at=c("il modello con")), dict(text="Istruzioni", sub="il suo metodo", at=c("e le istruzioni"))]))
    t = c.scene("Skill o agente, quindi")
    S.append(dict(type="cards", t0=t, kicker="Skill o agente?", title="Non è una scelta: si compongono.", cards=[
        dict(ck="La skill", nm="Il manuale", job="Sapere, metodo, formato", pts=["Lavora nella conversazione"], at=c("La skill è il manuale")),
        dict(ck="L'agente", nm="Il collaboratore", job="Un ruolo", pts=["Gli delegate un compito intero"], dark=True, at=c("L'agente è il collaboratore"))],
        foot="Le skill danno il metodo, gli agenti fanno il lavoro. <b>Prima le skill.</b>", footAt=c("Le skill danno")))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 06", title="Skill e agenti.", next="Seconda parte: connettori, pianificate e Code."))
    return S

@chapter("06b")
def ch06b(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 06", lines=["Skill e agenti,", "seconda parte."], sub="Connettori, pianificate e Code.")]
    t = c.scene("Un esempio di come")
    S.append(dict(type="app", t0=t, kicker="Esempio", title="L'analisi di una fiera.", sub="Tre agenti in parallelo, ognuno con il suo metodo.", nav="rec", panel=[
        dict(k="label", text="Avanzamento"), dict(k="psteps", items=[dict(text="Stand analizzati", at=c("Un agente stampa")), dict(text="Rassegna pronta", at=c("E un agente strategia")), dict(text="Conclusioni", at=c("Ognuno alla sua"))]),
        dict(k="label", text="Output", at=c("Ognuno alla sua")), dict(k="outfile", text="Analisi fiera.pptx", at=c("Ognuno alla sua"))], blocks=[
        dict(k="bubble", text="Analizza la fiera di settembre", at=c("analizza la fiera")),
        dict(k="reply", text="Coordino tre agenti in parallelo.", type=[c("Claude coordina"), c("Claude coordina") + 1.8]),
        dict(k="toolcall", text="Agente foto", small="lettura visiva", at=c("Un agente foto")), dict(k="toolcall", text="Agente stampa", small="rassegna", at=c("Un agente stampa")),
        dict(k="toolcall", text="Agente strategia", small="tono di voce, report", at=c("E un agente strategia")), dict(k="spacer"), dict(k="composer", chips=[dict(text="Manuale", sel=True)])]))
    t = c.scene("Poi ci sono i connettori")
    S.append(dict(type="app", t0=t, kicker="I connettori", title="Le prese verso i vostri strumenti.", sub="Dietro c'è MCP: una presa USB-C per tanti dispositivi.", nav="cus", blocks=[
        dict(k="label", text="Customize / Connettori"),
        dict(k="rows", items=[dict(text="Mail", tog=c("mail,")), dict(text="Calendario", tog=c("calendario,")), dict(text="Drive", tog=c("Drive,")), dict(text="SharePoint", tog=c("SharePoint,")), dict(text="Canva", tog=c("Canva,")), dict(text="CRM", tog=c("il CRM"))]),
        dict(k="text", text="Claude vede solo quello che autorizzate.", at=c("Claude vede solo"))]))
    t = c.scene("Una precisazione")
    S.append(dict(type="statement", t0=t, kicker="Una precisazione", lines=[dict(text="PowerPoint ed Excel?", at=c("per creare un PowerPoint")), dict(text="Nessun connettore.", soft=True, at=c("non serve un connettore"))], small="È una competenza di Claude. Il connettore serve per leggere e scrivere nei sistemi esterni.", smallAt=c("Il connettore serve")))
    t = c.scene("Le attività pianificate")
    S.append(dict(type="app", t0=t, kicker="Le attività pianificate", title="Lavorano anche senza di voi.", sub="In cloud, anche a computer spento.", nav="pia", blocks=[
        dict(k="label", text="Pianificate"), dict(k="title", text="Nuova attività"),
        dict(k="chips", items=[dict(text="Ogni ora", at=c("ogni ora")), dict(text="Ogni giorno", at=c("ogni giorno")), dict(text="Ogni settimana", at=c("ogni settimana"), on=c("o su richiesta")), dict(text="Su richiesta", at=c("o su richiesta"))]),
        dict(k="field", text="Ogni lunedì alle 8 leggi gli export della cartella e prepara il report social.", focus=True, type=[c("Si creano da"), c("Usano i connettori")], h=120),
        dict(k="chips", items=[dict(text="Crea con Claude", at=c("Crea con Claude"), on=c("Crea con Claude") + .5)])]))
    t = c.scene("E poi Claude Code")
    S.append(dict(type="app", t0=t, kicker="Claude Code", title="Il costruttore di strumenti.", sub="Nasce per gli sviluppatori, serve anche a chi non programma.", nav="", tab="code", blocks=[
        dict(k="label", text="Code / Marketing Claude"),
        dict(k="rows", items=[dict(text="Rinominare 500 foto di uno shooting", at=c("rinominare cinquecento")), dict(text="Un mini sito per un evento", at=c("creare un mini")),
            dict(text="Dal listino alle schede prodotto", at=c("trasformare un listino")), dict(text="Editare e montare un video", at=c("editare e montare")), dict(text="Piccoli strumenti su misura", at=c("costruire piccoli"))])]))
    t = c.scene("Quando conviene usarlo")
    S.append(dict(type="list", t0=t, kicker="Quando conviene", title="Code o chat?", sub="Descrivete il risultato, non il codice. Provate su pochi file.", items=[
        dict(text="Decine o centinaia di file", at=c("Quando il lavoro tocca")), dict(text="Uno strumento da riusare", at=c("quando vi serve uno")),
        dict(text="Un risultato tecnico", sub="come una pagina web", at=c("o quando volete"))]))
    t = c.scene("Un'ultima parola")
    S.append(dict(type="cards", t0=t, kicker="Sicurezza", title="Quanta autonomia, la decidete voi.", cards=[
        dict(ck="Predefinito", nm="Manuale", job="Chiede prima di agire", pts=["Il punto di partenza"], dark=True, at=c("Manuale, il predefinito")),
        dict(ck="Flussi collaudati", nm="Auto", job="Non chiede a ogni passo", pts=["Solo bozze e ricerche"], at=c("Auto significa"))],
        foot="Inviare, pagare, cancellare, pubblicare: <b>sempre con la vostra approvazione.</b>", footAt=c("Le azioni irreversibili")))
    t = c.scene("Vediamo tutto insieme")
    S.append(dict(type="pipeline", t0=t, kicker="Pipeline", title="Dal lancio a tutti i contenuti.", steps=[
        dict(tool="Progetto", text="Tono di voce e scheda della novità", at=c("Primo, il progetto")), dict(tool="Claude", text="Il comunicato stampa, come Doc", at=c("Secondo, Claude")),
        dict(tool="Voi", you=True, text="Rivedete e approvate", at=c("Terzo, voi")), dict(tool="Claude", text="Tre post e una newsletter", at=c("Quarto,")),
        dict(tool="Claude Design", text="La locandina per lo showroom", at=c("Quinto,"))], foot="Un solo contesto, tanti formati.", footAt=c("Un solo contesto")))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 06", title="Skill e agenti.", next="Prossimo capitolo: il setup ideale."))
    return S

@chapter("08")
def ch08(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 08", lines=["Automatizzare", "il ripetitivo."], sub="Il metodo per farlo da soli.")]
    t = c.scene("Ogni ufficio marketing")
    S.append(dict(type="list", t0=t, kicker="Lavori che si ripetono", title="Tutti uguali.", sub="Se sapete spiegarli a un collega nuovo, Claude può eseguirli.", mark="dot", items=[
        dict(text="Fatture da girare a chi approva", at=c("Le fatture")), dict(text="Richieste di materiali dai rivenditori", at=c("Le richieste")),
        dict(text="Report settimanali social e campagne", at=c("I report")), dict(text="Rassegna stampa e competitor", at=c("La rassegna")), dict(text="Foto degli shooting da archiviare", at=c("Le foto degli"))]))
    t = c.scene("Ogni automazione, semplice")
    S.append(dict(type="steps", t0=t, kicker="Le cinque mosse", side=True, steps=[
        dict(h="Innesco", p="Quando parte? Ogni ora, ogni lunedì, una mail.", at=c("Innesco:")), dict(h="Lettura", p="La casella, una cartella, un file, un sito.", at=c("Lettura:")),
        dict(h="Decisione", p="Una tabella: se succede questo, fai quello.", at=c("Decisione:")), dict(h="Azione", p="Inoltra, salva, rinomina, scrive una bozza.", at=c("Azione:")),
        dict(h="Registro", p="Aggiorna un file e manda un riepilogo.", at=c("Registro:"))]))
    t = c.scene("Prendiamo l'esempio")
    S.append(dict(type="app", t0=t, kicker="Esempio", title="La fattura nella mail.", sub="Se ha un dubbio non indovina: la segnala a voi.", nav="pia", panel=[
        dict(k="label", text="Avanzamento"), dict(k="psteps", items=[dict(text="Legge le mail", at=c("Claude guarda")), dict(text="Estrae i dati", at=c("Ne estrae")), dict(text="Smista", at=c("Se lo trova")), dict(text="Aggiorna il registro", at=c("Alla fine aggiorna"))]),
        dict(k="label", text="Output", at=c("Alla fine aggiorna")), dict(k="outfile", text="Registro fatture.xlsx", at=c("Alla fine aggiorna")), dict(k="outfile", text="Riepilogo di fine giornata", at=c("a fine giornata"))], blocks=[
        dict(k="label", text="Attività pianificata · ogni ora"),
        dict(k="toolcall", text="Nuove mail con un PDF", small="fattura?", at=c("Claude guarda")),
        dict(k="toolcall", text="Fornitore, numero, importo", small="estratti", at=c("Ne estrae")),
        dict(k="toolcall", text="Tabella chi riceve cosa", small="cercato", at=c("Poi cerca")),
        dict(k="rows", items=[dict(text="Agenzia social", small="al referente", chip="Inoltrata", at=c("Se lo trova")), dict(text="Fornitore sconosciuto", chip="Da controllare", at=c("Se ha un dubbio"))])]))
    t = c.scene("Il segreto è separare")
    S.append(dict(type="list", t0=t, kicker="Chi riceve cosa", title="Le regole in una tabella.", sub="Cambia un referente? Si aggiorna la tabella, l'automazione non si tocca.", items=[
        dict(text="Agenzia social", sub="cartella Fatture social", tool="Maria", at=c("l'agenzia social")), dict(text="Studio fotografico", sub="cartella Shooting", tool="Luca", at=c("lo studio fotografico")),
        dict(text="Ente fiera", sub="cartella Eventi", tool="Anna", at=c("l'ente fiera"))]))
    t = c.scene("Il prompt dell'attività")
    txt = "Ogni ora controlla la casella marketing. Per ogni nuova mail con un PDF che sembra una fattura: leggi fornitore, numero, data e importo; cerca il fornitore nel file chi riceve cosa; se lo trovi, inoltra al referente e salva il PDF nella sua cartella; se non lo trovi o hai dubbi, non fare nulla e aggiungilo alla lista da controllare; aggiorna il registro fatture. Alle diciotto mandami un riepilogo."
    S.append(dict(type="quote", t0=t, kicker="Senza una riga di codice", title="Il prompt, in italiano.", sub="Le cinque mosse, come le direste a un collega.", label="Prompt dell'attività", segs=sentences_segs(c, txt)))
    t = c.scene("Lo stesso schema")
    S.append(dict(type="list", t0=t, kicker="Lo stesso schema", title="Per tanti altri lavori.", items=[
        dict(text="Richieste dai rivenditori", sub="risposta in bozza con il link giusto", tool="Nuova mail", at=c("Le richieste dai")),
        dict(text="Report social settimanale", sub="un Doc con grafici e commento", tool="Lunedì 8:00", at=c("Il report social")),
        dict(text="Rassegna e competitor", sub="sintesi con le fonti", tool="Venerdì", at=c("La rassegna stampa e i")),
        dict(text="Archivio foto", sub="riconosce, rinomina e smista", tool="Fine shooting", at=c("E l'archivio"))]))
    t = c.scene("Esistono anche strumenti")
    S.append(dict(type="cards", t0=t, kicker="Strumenti a confronto", title="Regole rigide o giudizio.", cards=[
        dict(ck="Automazione classica", nm="Regole rigide", job="Scattano all'istante", pts=["Flussi semplici e sempre uguali"], at=c("Esistono anche")),
        dict(ck="Claude", nm="Giudizio", job="Capisce testi, PDF e mail", pts=["Scritti ogni volta in modo diverso"], dark=True, at=c("Claude invece"))],
        foot="Spesso conviene combinarli. <b>Le cinque mosse valgono ovunque.</b>", footAt=c("Spesso conviene")))
    t = c.scene("Sei regole d'oro")
    S.append(dict(type="list", t0=t, kicker="Le regole d'oro", title="Sei regole.", mark="check", compact=True, items=[
        dict(text="Un lavoro piccolo e frequente", at=c("Partite da")), dict(text="Regole spiegate come a un collega", at=c("Scrivete le regole")),
        dict(text="Manuale per una o due settimane", at=c("Iniziate con")), dict(text="Sempre il caso non so", at=c("Prevedete sempre")),
        dict(text="Un registro di tutto", at=c("Tenete un registro")), dict(text="All'inizio: niente invii o pagamenti", at=c("E all'inizio"))]))
    t = c.scene("E la pipeline per costruire")
    S.append(dict(type="pipeline", t0=t, kicker="Pipeline", title="La vostra prima automazione.", steps=[
        dict(tool="Voi", you=True, text="Un lavoro piccolo e frequente", at=c("Scegliete un lavoro")), dict(tool="Voi", you=True, text="Cinque mosse e tabella delle regole", at=c("Compilate")),
        dict(tool="Claude", text="Pianificate, Crea con Claude", at=c("Andate in Pianificate")), dict(tool="Claude", text="Due settimane in Manuale", at=c("Lasciatela girare")),
        dict(tool="Voi", you=True, text="Correggete, poi più autonomia", at=c("Poi correggete"))], foot="Si parte piccoli, si osserva, si allarga. Mai il contrario.", footAt=c("Si parte piccoli")))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 08", title="Automazioni.", next="Prossimo capitolo: la fiducia."))
    return S

@chapter("09")
def ch09(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 09", lines=["La fiducia,", "e il primo passo."])]
    t = c.scene("Verificare sempre")
    S.append(dict(type="list", t0=t, kicker="Verificare sempre", title="Prima di pubblicare.", mark="check", items=[
        dict(text="Diritti, marchi e linee guida", at=c("controllate diritti")), dict(text="Prodotti reali: mai inventati", at=c("I prodotti reali")),
        dict(text="Numeri e dati: ricontrollati", at=c("E numeri e dati"))]))
    t = c.scene("Il metodo di verifica")
    S.append(dict(type="steps", t0=t, kicker="Il metodo di verifica", side=True, steps=[
        dict(h="Chiedete le fonti", at=c("chiedete le fonti")), dict(h="Confrontate", p="con dati che conoscete", at=c("confrontate con")),
        dict(h="Il vostro giudizio", p="da esperti", at=c("usate il vostro")), dict(h="Provate in piccolo", p="prima di pubblicare", at=c("e provate in piccolo"))]))
    t = c.scene("Ripeto la frase")
    S.append(dict(type="statement", t0=t, lines=[dict(text="L'AI potenzia chi la usa,", at=c("l'AI potenzia")), dict(text="non sostituisce il giudizio.", soft=True, at=c("non sostituisce"))]))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 09", title="La fiducia.", next="Prossimo capitolo: un ufficio eventi."))
    return S

@chapter("10")
def ch10(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 10", lines=["Un ufficio eventi", "con Claude."], sub="Tutti i mattoni, su un caso concreto.")]
    t = c.scene("L'idea è questa")
    S.append(dict(type="statement", t0=t, kicker="L'idea", lines=[dict(text="Una squadra digitale.", at=c("come una squadra")), dict(text="Voi siete il direttore.", soft=True, at=c("E voi siete"))], small="Ogni agente ha un ruolo e i suoi orari. Tutti lavorano sulla stessa cartella.", smallAt=c("Ognuno ha i suoi")))
    t = c.scene("Al centro c'è il progetto")
    S.append(dict(type="cards", t0=t, kicker="Il progetto Ufficio Eventi", title="Quattro blocchi intorno al progetto.", cards=[
        dict(ck="Il metodo", nm="Skill", pts=["Brief evento", "Scaletta", "Inviti", "Report"], at=c("Le skill:")),
        dict(ck="I ruoli", nm="Agenti", pts=["Location e fornitori", "Comunicazione", "Logistica", "Analisi"], dark=True, at=c("Gli agenti:")),
        dict(ck="Le prese", nm="Connettori", pts=["Mail", "Calendario", "Drive o SharePoint", "Excel"], at=c("I connettori:")),
        dict(ck="Gli orari", nm="Pianificate", pts=["Stato del lunedì", "Lista ospiti", "Promemoria", "Report finale"], at=c("E le attività pianificate"))],
        foot="Gli output: <b>Docs, Slides, Design e file Excel.</b>", footAt=c("Gli output arrivano")))
    t = c.scene("La cartella eventi")
    S.append(dict(type="app", t0=t, kicker="La cartella", title="Il patrimonio dell'ufficio.", sub="Fornitori e location, con contatti e prezzi.", nav="prj", blocks=[
        dict(k="label", text="Ufficio Eventi"), dict(k="tree", items=[
            dict(text="00_Leggimi", small="regole, tono, budget tipo", at=c("un Leggimi")), dict(text="Fornitori e location.xlsx", small="contatti e prezzi", at=c("un file fornitori")),
            dict(text="Template", small="brief, budget, scaletta, inviti", dir=True, at=c("i template")), dict(text="Eventi", dir=True, at=c("una cartella Eventi")),
            dict(text="2026-11_Showroom", small="brief, ospiti, foto, report", dir=True, d=1, at=c("con una sottocartella")), dict(text="Archivio", dir=True, at=c("e un archivio"))])]))
    t = c.scene("La pipeline di un evento")
    S.append(dict(type="pipeline", t0=t, kicker="Pipeline", title="Dal brief al report finale.", steps=[
        dict(tool="Claude", text="Concept, obiettivi e budget", at=c("Claude trasforma")), dict(tool="Claude", text="Location, fornitori, preventivi", at=c("Poi cerca")),
        dict(tool="Voi", you=True, text="Scegliete e confermate", at=c("Voi scegliete")), dict(tool="Claude", text="Cronoprogramma, inviti, post, locandina", at=c("Claude prepara cronoprogramma")),
        dict(tool="Claude", text="Ospiti, promemoria, scaletta", at=c("Poi tiene")), dict(tool="Claude", text="Report, grazie, rassegna", at=c("E alla fine"))],
        foot="Claude prepara, voi decidete: ogni invio passa dalla vostra approvazione.", footAt=c("Claude prepara, voi")))
    t = c.scene("Le attività pianificate sono il cuore")
    S.append(dict(type="list", t0=t, kicker="Le attività pianificate", title="Il cuore dell'ufficio.", items=[
        dict(text="Stato degli eventi e scadenze", tool="Lunedì 9:00", at=c("Ogni lunedì")), dict(text="Risposte agli inviti, lista ospiti", tool="Ogni giorno", at=c("Ogni giorno,")),
        dict(text="Promemoria ai fornitori, in bozza", tool="-14 / -7 / -1", at=c("A quattordici")), dict(text="Ringraziamenti e raccolta foto", tool="Giorno dopo", at=c("Il giorno dopo")),
        dict(text="Report: presenze, costi, risultati", tool="+7 giorni", at=c("Una settimana dopo"))]))
    t = c.scene("Il prompt di avvio")
    txt = "Sei l'assistente dell'ufficio eventi del marketing. Leggi il Leggimi e il file fornitori e location. Per un nuovo evento crea la sua cartella con brief, budget e cronoprogramma. Tieni aggiornata la lista ospiti da mail e moduli. Prepara inviti, comunicazioni e promemoria solo in bozza: niente invii senza il mio ok. Ogni lunedì mandami lo stato degli eventi."
    S.append(dict(type="quote", t0=t, kicker="Da incollare nel progetto", title="Il prompt di avvio.", label="Istruzioni del progetto", segs=sentences_segs(c, txt)))
    t = c.scene("Il setup si fa")
    S.append(dict(type="steps", t0=t, kicker="Il setup · Otto passi", side=True, steps=[
        dict(h="La cartella", short="Cartella", at=c("create la cartella")), dict(h="Fornitori e template", short="Fornitori e template", at=c("riempite il file")),
        dict(h="Progetto collegato", short="Progetto", at=c("create il progetto")), dict(h="Le istruzioni", short="Istruzioni", at=c("scrivete le istruzioni")),
        dict(h="Le skill", short="Skill", at=c("create le skill")), dict(h="Connettori con l'IT", short="Connettori", at=c("collegate mail")),
        dict(h="Pianificate in Manuale", short="Pianificate", at=c("create le attività")), dict(h="Un evento piccolo", p="Mezza giornata più due settimane di rodaggio.", short="Prova", at=c("e provate tutto"))]))
    t = c.scene("Cosa resta fuori")
    S.append(dict(type="cards", t0=t, kicker="Cosa resta fuori", title="Claude organizza. Il resto, strumenti dedicati.", cards=[
        dict(ck="Claude", nm="Organizza", job="Scrive, controlla, ricorda", pts=["Legge i dati via connettore"], dark=True, at=c("Claude organizza")),
        dict(ck="Strumenti dedicati", nm="Il resto", job="Registrazione e biglietteria", pts=["Check-in con QR", "Pagamenti, app partecipanti"], at=c("Ma per la registrazione"))],
        foot="Non serve un'altra AI: <b>serve un ufficio ben impostato.</b>", footAt=c("Il messaggio di questo")))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 10", title="Un ufficio eventi.", next="Prossimo capitolo: Leonardo AI."))
    return S

@chapter("11a")
def ch11a(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 11", lines=["Leonardo AI,", "lo studio visivo."], sub="Immagini e video nel dettaglio.")]
    t = c.scene("Come funziona")
    S.append(dict(type="steps", t0=t, kicker="Come funziona", steps=[
        dict(h="Descrivete", p="l'immagine a parole", at=c("Descrivete")), dict(h="Scegliete", p="un modello e un formato", at=c("scegliete un modello")),
        dict(h="Generate", p="alcune varianti", at=c("e Leonardo genera")), dict(h="Rifinite", p="ritocchi, ingrandimenti, animazione", at=c("Poi potete"))]))
    t = c.scene("Tre cose da sapere")
    S.append(dict(type="list", t0=t, kicker="Da sapere", title="Tre cose.", items=[
        dict(text="È un aggregatore", sub="tanti modelli diversi", at=c("è un aggregatore")), dict(text="Ogni generazione costa token", at=c("ogni generazione")),
        dict(text="Sui piani a pagamento, immagini private", at=c("e sui piani"))]))
    t = c.scene("L'area di lavoro ha sei")
    S.append(dict(type="list", t0=t, kicker="L'area di lavoro", title="Sei strumenti.", compact=True, items=[
        dict(text="Image", tool="prompt e modello", at=c("Image,")), dict(text="Flow State", tool="decine di varianti", at=c("Flow State")),
        dict(text="Editor", tool="modifiche a parole", at=c("L'editor")), dict(text="Upscaler", tool="risoluzione", at=c("L'upscaler")),
        dict(text="Video", tool="anima un'immagine", at=c("Video, per")), dict(text="Blueprints", tool="flussi pronti", at=c("E Blueprints"))]))
    t = c.scene("I modelli per le immagini")
    S.append(dict(type="list", t0=t, kicker="Immagini", title="Un modello per ogni specialità.", compact=True, items=[
        dict(text="Lucid Origin", tool="Tuttofare", at=c("Lucid Origin")), dict(text="Lucid Realism", tool="Fotorealismo", at=c("Lucid Realism")),
        dict(text="Nano Banana", tool="Modifiche a parole", at=c("Nano Banana")), dict(text="Seedream 4.0", tool="4K nativo", at=c("Seedream")),
        dict(text="Ideogram 3.0", tool="Testo leggibile", at=c("Ideogram")), dict(text="GPT Image", tool="Editing e mockup", at=c("GPT Image")),
        dict(text="Flux 2 Pro", tool="Colori fedeli", at=c("Flux 2")), dict(text="Phoenix", tool="Stile vettoriale", at=c("E Phoenix"))]))
    t = c.scene("Anche per i video")
    S.append(dict(type="list", t0=t, kicker="Video", title="Una scelta ampia.", sub="Il video parte da un'immagine: diventa il primo fotogramma.", compact=True, items=[
        dict(text="Veo 3.1", tool="Pubblicità", at=c("Veo")), dict(text="Kling 3.0", tool="Camera cinematografica", at=c("Kling 3.0")),
        dict(text="Kling Omni", tool="Modifica video", at=c("Kling Omni")), dict(text="Seedance", tool="Più scene coerenti", at=c("Seedance")),
        dict(text="MiniMax", tool="Audio nativo", at=c("MiniMax")), dict(text="LTX-2", tool="4K", at=c("LTX-2")), dict(text="Motion 2.0", tool="Teaser social", at=c("E Motion"))]))
    t = c.scene("Come si sceglie, nella pratica")
    S.append(dict(type="list", t0=t, kicker="In pratica", title="Come si sceglie.", compact=True, items=[
        dict(text="Concept e moodboard", tool="Lucid Origin", at=c("Per concept")), dict(text="Ambientazione fotorealistica", tool="Realism o Flux", at=c("Per un'ambientazione")),
        dict(text="Correggere un dettaglio", tool="Nano Banana", at=c("Per correggere")), dict(text="Locandina con testo", tool="Ideogram", at=c("Per una locandina")),
        dict(text="Stampa e pubblicità", tool="Seedream 4K", at=c("Per visual")), dict(text="Teaser social", tool="Motion", at=c("Per un teaser")),
        dict(text="Video con il prodotto", tool="Veo o Kling", at=c("Per un video"))]))
    t = c.scene("Il prompt di un'immagine")
    S.append(dict(type="quote", t0=t, kicker="Il prompt", title="Sei blocchi.", sub="Soggetto, ambiente, luce, inquadratura, stile, formato. In inglese rende meglio: fatelo tradurre a Claude.", label="Prompt", segs=[
        c.seg("un soggiorno", "tessuto bouclé,", "Un soggiorno moderno con un divano basso in tessuto bouclé, "),
        c.seg("davanti a", "in rovere,", "davanti a una grande finestra sul lago, pavimento in rovere, "),
        c.seg("luce morbida", "toni caldi,", "luce morbida del mattino, toni caldi, "),
        c.seg("inquadratura grandangolare", "altezza occhi,", "inquadratura grandangolare ad altezza occhi, "),
        c.seg("fotografia d'interni", "minimal, fotorealistica,", "fotografia d'interni editoriale, minimal, fotorealistica, "),
        c.seg("formato sedici", "sedici noni.", "formato 16:9.")]))
    t = c.scene("Il testo da solo")
    S.append(dict(type="list", t0=t, kicker="Per la coerenza", title="Immagini di riferimento.", items=[
        dict(text="Di stile", sub="fallo come questa foto", at=c("di stile")), dict(text="Di contenuto", sub="forma e composizione", at=c("di contenuto")),
        dict(text="Di personaggio", sub="lo stesso soggetto in più immagini", at=c("e di personaggio")), dict(text="Ritocchi", sub="modifiche, upscale, espansione del formato", at=c("Poi ci sono"))]))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 11", title="Leonardo AI.", next="Seconda parte: costi, pipeline e attenzioni."))
    return S

@chapter("11b")
def ch11b(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Capitolo 11", lines=["Leonardo AI,", "seconda parte."], sub="Costi, pipeline, attenzioni.")]
    t = c.scene("Sui costi")
    S.append(dict(type="list", t0=t, kicker="Token e piani", title="Per non sprecarli.", sub="Gratis 150 token al giorno. A pagamento da circa 12 a 60 dollari al mese.", mark="check", items=[
        dict(text="Una o due immagini alla volta", at=c("generate una")), dict(text="Esplorate in bassa risoluzione", at=c("esplorate")),
        dict(text="Upscale solo delle migliori", at=c("fate l'upscale")), dict(text="Animate solo le immagini scelte", at=c("e animate"))]))
    t = c.scene("L'ultima pipeline")
    S.append(dict(type="pipeline", t0=t, kicker="Pipeline", title="Dall'idea al video.", steps=[
        dict(tool="Claude", text="Concept e prompt delle scene", at=c("Claude trasforma")), dict(tool="Leonardo", text="Immagini, poche alla volta", at=c("Leonardo genera")),
        dict(tool="Leonardo", text="Ritocchi e upscale", at=c("Poi le ritocca")), dict(tool="Kling o Veo", text="L'animazione", at=c("Le anima")),
        dict(tool="Claude", text="Montaggio, musica, brand con HyperFrames", at=c("E infine"))], foot="Prima le immagini giuste, poi il movimento.", footAt=c("Prima le immagini")))
    t = c.scene("E qualche attenzione")
    S.append(dict(type="list", t0=t, kicker="Attenzioni", title="Cinque cose.", items=[
        dict(text="Prodotti reali: riferimento o compositing", at=c("I prodotti reali")), dict(text="Il testo si aggiunge dopo", sub="Claude Design, InDesign o ChatGPT", at=c("Il testo nelle")),
        dict(text="Uso commerciale: verificate il piano", at=c("Verificate")), dict(text="Palette, luce e materiali del brand", at=c("Guidate")),
        dict(text="Dichiarate l'uso dell'AI", sub="quando serve", at=c("E quando serve"))]))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="Capitolo 11", title="Leonardo AI.", next="Ultimo capitolo: la chiusura."))
    return S

@chapter("12")
def ch12(c):
    S = [dict(type="title", t0=0, kicker="L'AI al lavoro · Chiusura", lines=["Cinque messaggi", "da portare a casa."])]
    t = c.scene("Uno: ogni AI")
    S.append(dict(type="steps", t0=t, kicker="Cinque messaggi", side=True, steps=[
        dict(h="Ogni AI ha il suo mestiere", p="Perplexity cerca, Claude lavora, Gemini vive in Google, ChatGPT corre, Leonardo crea.", short="Il mestiere di ogni AI", at=c("Uno:")),
        dict(h="Il prompt è tutto", p="Ruolo, contesto, compito, formato.", short="Il prompt", at=c("Due:")),
        dict(h="Modello, chat, cartella", p="Meno token e più qualità.", short="Meno token", at=c("Tre:")),
        dict(h="Claude riscrive i file", p="Chiedete a lui o lavorate su una copia.", short="La copia", at=c("Quattro:")),
        dict(h="Cinque mosse", p="Prima chiedete, poi delegate.", short="Le cinque mosse", at=c("Cinque:"))]))
    t = c.scene("E poi il primo passo")
    S.append(dict(type="list", t0=t, kicker="Entro domani", title="Il primo passo.", sub="Cosa manca? Aggiungetelo alle istruzioni.", items=[
        dict(text="Cartella e progetto collegato", at=c("create la cartella")), dict(text="Tono di voce e due testi nel Leggimi", at=c("mettete nel")),
        dict(text="La variante di un contenuto reale", at=c("chiedete a Claude")), dict(text="Giudicate il risultato", at=c("e giudicate"))]))
    t = c.scene("Perché alla fine")
    S.append(dict(type="statement", t0=t, lines=[dict(text="Non sostituisce il vostro giudizio.", at=c("l'AI non sostituisce")), dict(text="Lo moltiplica.", soft=True, at=c("Li moltiplica"))], small="Grazie per l'ascolto.", smallAt=c("Grazie per")))
    S.append(dict(type="outro", t0=c.dur + .3, kicker="L'AI al lavoro", title="Grazie.", next="Formazione AI per il Marketing · Colombini Group"))
    return S

TITLES = {"01": "Introduzione e panorama", "02": "Il prompt", "03": "Tre a confronto", "04a": "Dentro Claude", "04b": "Dentro Claude, seconda parte", "05": "Lavorare bene", "06a": "Skill e agenti", "06b": "Skill e agenti, seconda parte", "08": "Automazioni", "09": "Fiducia", "10": "Un ufficio eventi", "11a": "Leonardo AI", "11b": "Leonardo AI, seconda parte", "12": "Chiusura"}

def build(k):
    c = Cues(k)
    S = CH[k](c)
    total = round(c.dur + 3.4, 2)
    for i, s in enumerate(S):
        s["t1"] = S[i + 1]["t0"] if i + 1 < len(S) else total
        s.setdefault("paper", s["type"] in ("cards", "pipeline", "compare"))
    # alterna fondo carta su alcune scene di lista per ritmo visivo
    num = k[:2]
    spec = {"id": k, "total": total, "dur": c.dur, "chromeL": f"L'AI al lavoro · Capitolo {num}" if k != "12" else "L'AI al lavoro · Chiusura", "chromeR": TITLES[k], "scenes": S}
    html = open("engine.html", encoding="utf-8").read().replace("/*SPEC*/null", json.dumps(spec, ensure_ascii=False))
    os.makedirs("out", exist_ok=True)
    open(f"out/{k}.html", "w", encoding="utf-8").write(html)
    json.dump(spec, open(f"out/{k}.json", "w"), ensure_ascii=False, indent=1)
    return spec

if __name__ == "__main__":
    for k in (sys.argv[1:] or list(CH)):
        sp = build(k); print(k, sp["total"], len(sp["scenes"]))
