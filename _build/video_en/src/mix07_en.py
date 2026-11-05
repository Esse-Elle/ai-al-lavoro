import json,subprocess
W=json.load(open('warp07.json'))
def inv(t):
    for i in range(1,len(W)):
        if t<=W[i][1]:
            a,b=W[i-1],W[i]; return a[0]+(b[0]-a[0])*(t-a[1])/max(1e-6,b[1]-a[1])
    return W[-1][0]
src=open('mix.py').read()
ns={}
exec(src.split('inputs=')[0],ns)
ev=[(n,round(inv(t),3),v) for n,t,v in ns['ev']]
T=120.07; D=117.24; A="assets/"
inputs=["-i","../en/audio/07.wav","-stream_loop","4","-i",A+"music_a.wav"]
filt=["[0:a]aresample=48000,volume=1.7[v]",f"[1:a]aresample=48000,atrim=0:{T},volume='if(lt(t,{inv(3.6)}),0.55,if(lt(t,{inv(118.8)}),0.11,0.55))':eval=frame,afade=t=in:d=0.4,afade=t=out:st={T-1.8}:d=1.8[m]"]
L=["[v]","[m]"]
for i,(n,t,vol) in enumerate(ev):
    inputs+=["-i",A+n+".mp3"]; ms=int(t*1000); filt.append(f"[{i+2}:a]aresample=48000,volume={vol},adelay={ms}|{ms}[e{i}]"); L.append(f"[e{i}]")
filt.append("".join(L)+f"amix=inputs={len(L)}:normalize=0:duration=longest,atrim=0:{T},alimiter=limit=0.95[out]")
subprocess.run(["ffmpeg","-v","error","-y"]+inputs+["-filter_complex",";".join(filt),"-map","[out]","-c:a","aac","-b:a","192k","-t",str(T),"en07_mix.m4a"],check=True); print("ok",len(ev))
