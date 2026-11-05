import asyncio,sys
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1920,"height":1080})
    await pg.goto("file://"+__import__('os').getcwd()+"/"+sys.argv[1]); await pg.evaluate("document.fonts.ready")
    for t in sys.argv[2:]:
      await pg.evaluate(f"window.__seek({t})"); await pg.screenshot(path=f"snap_{t}.jpg",type="jpeg",quality=70)
    await b.close()
asyncio.run(m())
