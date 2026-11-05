import asyncio,sys,json,os,subprocess
from playwright.async_api import async_playwright
async def m(k):
  sp=json.load(open(f"out_en/{k}.json")); ts=[round(s["t1"]-0.6,2) for s in sp["scenes"]]
  open(f"en{k}.html","w").write(open(f"out_en/{k}.html").read())
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1920,"height":1080})
    await pg.goto("file://"+os.getcwd()+f"/en{k}.html"); await pg.evaluate("document.fonts.ready")
    fs=[]
    for i,t in enumerate(ts):
      await pg.evaluate(f"window.__seek({t})"); f=f"sn_{k}_{i}.jpg"; await pg.screenshot(path=f,type="jpeg",quality=60); fs.append(f)
    await b.close()
  n=len(fs); cols=3; rows=(n+cols-1)//cols
  while len(fs)<rows*cols: fs.append(fs[-1])
  inp=sum([["-i",f] for f in fs],[]); fl="".join(f"[{i}]scale=640:-1[s{i}];" for i in range(len(fs)))
  fl+="".join("".join(f"[s{r*cols+c}]" for c in range(cols))+f"hstack={cols}[r{r}];" for r in range(rows))
  fl+="".join(f"[r{r}]" for r in range(rows))+(f"vstack={rows}" if rows>1 else "null")
  subprocess.run(["ffmpeg","-v","error","-y"]+inp+["-filter_complex",fl,f"sheet_{k}.jpg"],check=True)
for k in sys.argv[1:]: asyncio.run(m(k)); print(k)
