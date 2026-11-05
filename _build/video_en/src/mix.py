import subprocess
A="assets/"
ev=[("whoosh",3.6,.45),("whoosh",64.6,.4),("whoosh",70.3,.4),("whoosh",84.6,.35),("whoosh",92.5,.5),("sparkle",119.3,.45)]
for t in [4.0,8.55,13.8,17.95,22.2,25.8,30.0,35.4,39.6,41.9]: ev.append(("pop",t,.35))
for t in [27.04,28.0,28.8,85.3,87.8]: ev.append(("pop",t,.25))
for t in [96.38,100.34,104.3,106.9,110.5,113.78,116.78]: ev.append(("pop",t,.3))
for s,e in [(48.72,52.6),(53.2,55.6),(56.08,58.3),(58.8,61.1),(61.6,64.4)]:
    t=s
    while t<e-0.3: ev.append(("typing",t,.16)); t+=1.5
inputs=["-i",A+"voice.mp3","-stream_loop","4","-i",A+"music_a.wav"]
filt=["[0:a]aresample=48000,volume=1.7[v]",
      "[1:a]aresample=48000,atrim=0:122,volume='if(lt(t,3.6),0.55,if(lt(t,118.8),0.11,0.55))':eval=frame,afade=t=in:d=0.4,afade=t=out:st=120.2:d=1.8[m]"]
labels=["[v]","[m]"]
for i,(n,t,vol) in enumerate(ev):
    inputs+=["-i",A+n+".mp3"]
    k=i+2; ms=int(t*1000)
    filt.append(f"[{k}:a]aresample=48000,volume={vol},adelay={ms}|{ms}[e{i}]"); labels.append(f"[e{i}]")
filt.append("".join(labels)+f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=0:122,alimiter=limit=0.95[out]")
# durata: usa la musica (122s) come riferimento
filt[-1]=filt[-1].replace("duration=first","duration=longest")
cmd=["ffmpeg","-v","error","-y"]+inputs+["-filter_complex",";".join(filt),"-map","[out]","-c:a","aac","-b:a","192k","-t","122","audio_mix.m4a"]
subprocess.run(cmd,check=True); print("ok")
