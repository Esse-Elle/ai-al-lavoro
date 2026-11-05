import asyncio, subprocess, sys
from playwright.async_api import async_playwright
FPS=30; TOTAL=122.0
async def main():
    ff=subprocess.Popen(["ffmpeg","-v","error","-y","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-","-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","video_noaudio.mp4"],stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1920,"height":1080})
        await pg.goto("file:///home/claude/v07/index.html"); await pg.evaluate("document.fonts.ready")
        n=int(TOTAL*FPS)
        for i in range(n):
            await pg.evaluate(f"window.__seek({i/FPS})")
            ff.stdin.write(await pg.screenshot(type="jpeg",quality=92))
            if i%300==0: print(i,n,flush=True)
        await b.close()
    ff.stdin.close(); ff.wait(); print("done")
asyncio.run(main())
