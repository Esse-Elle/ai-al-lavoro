import subprocess,sys,os
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); FPS=30; N=int(30*FPS)
ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-c:v','png','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18',f'{D}/intro_en_v.mp4'],stdin=subprocess.PIPE)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://'+D+'/r.html'); pg.wait_for_timeout(800)
    pg.evaluate("document.fonts.ready")
    for i in range(N):
        t=i/FPS
        pg.evaluate("""t=>{document.querySelectorAll('.clip[data-start]').forEach(e=>{const s=+e.dataset.start,d=+e.dataset.duration;e.style.visibility=(t>=s&&t<s+d)?'visible':'hidden'});window.__timelines.main.seek(t,false)}""",t)
        ff.stdin.write(pg.screenshot(type='png'))
        if i in (60,240,420,600,780,890): pg.screenshot(path=f'{D}/f{i}.png')
    b.close()
ff.stdin.close(); ff.wait()
