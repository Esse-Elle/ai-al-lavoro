import json,subprocess,sys
k=sys.argv[1]; voice=sys.argv[2]; out=sys.argv[3]
sp=json.load(open(f"out_en/{k}.json")); T=sp["total"]; D=sp["dur"]; A="assets/"
ev=[]
for i,s in enumerate(sp["scenes"]):
    if i>0 and s["type"]!="outro": ev.append(("whoosh",s["t0"],.4))
    if s["type"]=="outro": ev.append(("sparkle",s["t0"],.45))
    for it in s.get("items",[])+s.get("steps",[]):
        if "at" in it: ev.append(("pop",it["at"],.3))
    for b in s.get("blocks",[]):
        if "type" in b:
            a,e=b["type"]; t=a
            while t<e-0.3: ev.append(("typing",t,.16)); t+=1.5
        elif "at" in b: ev.append(("pop",b["at"],.3))
inputs=["-i",voice,"-stream_loop","6","-i",A+"music_a.wav"]
filt=["[0:a]aresample=48000,volume=1.7[v]",
 f"[1:a]aresample=48000,atrim=0:{T},volume='if(lt(t,{D}),0.11,0.55)':eval=frame,afade=t=in:d=0.4,afade=t=out:st={T-1.8}:d=1.8[m]"]
L=["[v]","[m]"]
for i,(n,t,vol) in enumerate(ev):
    inputs+=["-i",A+n+".mp3"]; ms=int(t*1000)
    filt.append(f"[{i+2}:a]aresample=48000,volume={vol},adelay={ms}|{ms}[e{i}]"); L.append(f"[e{i}]")
filt.append("".join(L)+f"amix=inputs={len(L)}:normalize=0:duration=longest,atrim=0:{T},alimiter=limit=0.95[out]")
subprocess.run(["ffmpeg","-v","error","-y"]+inputs+["-filter_complex",";".join(filt),"-map","[out]","-c:a","aac","-b:a","192k","-t",str(T),out],check=True)
print("mix ok",len(ev))
