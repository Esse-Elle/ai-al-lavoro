import asyncio, sys, json
from playwright.async_api import async_playwright
from PIL import Image
async def main(k):
    sp=json.load(open(f"out/{k}.json"))
    ts=[]
    for s in sp["scenes"]:
        ts.append(min(s["t1"]-0.6, s["t0"]+ (s["t1"]-s["t0"])*0.85))
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1920,"height":1080})
        errs=[]; pg.on("pageerror",lambda e: errs.append(str(e)))
        await pg.goto(f"file:///home/claude/vgen/out/{k}.html"); await pg.evaluate("document.fonts.ready")
        ims=[]
        for i,t in enumerate(ts):
            await pg.evaluate(f"window.__seek({t})"); fn=f"/tmp/s_{k}_{i}.jpg"; await pg.screenshot(path=fn,type="jpeg",quality=60); ims.append(fn)
        if errs: print("ERR",errs)
        await b.close()
    w,h=640,360; cols=3; rows=(len(ims)+2)//3
    S=Image.new("RGB",(w*cols,h*rows),"white")
    for i,f in enumerate(ims): S.paste(Image.open(f).resize((w,h)),((i%3)*w,(i//3)*h))
    S.save(f"sheet_{k}.jpg",quality=75)
asyncio.run(main(sys.argv[1]))
