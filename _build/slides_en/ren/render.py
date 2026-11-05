import asyncio,sys,os,json
from playwright.async_api import async_playwright
# usage: render.py job.json  -> job: [[html_file, w, h, out_png],...]
async def m(jobs):
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for f,w,h,out in jobs:
      pg=await b.new_page(viewport={"width":w,"height":h},device_scale_factor=2)
      await pg.goto("file://"+os.path.abspath(f)); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(100)
      await pg.screenshot(path=out); await pg.close()
    await b.close()
asyncio.run(m(json.load(open(sys.argv[1]))))
