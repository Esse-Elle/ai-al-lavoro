import json,sys,os,html
D=os.path.dirname(os.path.abspath(__file__))
def cover(k,kicker,title,sub,by=None,dark=True):
    bg,kc,tc,sc,rc=('#161d33','#cbc6bb','#ffffff','#f4f2ee','#cbc6bb') if dark else ('#f4f2ee','#75655c','#161d33','#161d33','#75655c')
    byh=f'<div class="by">{html.escape(by)}</div>' if by else ''
    h=f'''<html><head><meta charset=utf-8><link rel=stylesheet href=base.css><style>
body{{width:655px;height:618px;background:{bg};position:relative;overflow:hidden}}
.k{{position:absolute;left:45px;top:55px;font:600 12.2px Karla;letter-spacing:.17em;text-transform:uppercase;color:{kc}}}
.w{{position:absolute;left:44px;top:{231 if by else 233}px;right:30px}}
.t{{font:700 60.5px/1.05 Butler;color:{tc};letter-spacing:-.005em}}
.by{{font:400 15px Karla;color:{kc};margin-top:{12}px;letter-spacing:.02em}}
.r{{width:120px;height:2px;background:{rc};margin-top:{18 if by else 22}px}}
.s{{font:400 25.8px/1.32 Butler;color:{sc};margin-top:{14 if by else 12}px;max-width:{520}px}}
</style></head><body><div class=k>{html.escape(kicker)}</div><div class=w><div class=t>{html.escape(title)}</div>{byh}<div class=r></div><div class=s>{html.escape(sub)}</div></div></body></html>'''
    open(f'{D}/c_{k}.html','w').write(h); return [f'{D}/c_{k}.html',655,618,f'{D}/out/{k}.png']
