import asyncio,sys,os
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch()
    for f,w,h in [("p17",1333,356),("p19",1289,472)]:
      pg=await b.new_page(viewport={"width":w,"height":h},device_scale_factor=2)
      await pg.goto("file://"+os.getcwd()+"/"+f+".html"); await pg.evaluate("document.fonts.ready"); await pg.screenshot(path=f+"_en.png")
    await b.close()
asyncio.run(m())
