import html,os,glob
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); E=html.escape
def patch(k,items,W=1289,H=472):
    src=glob.glob(f'{D}/../pics/{k}_*')[0]; im=Image.open(src).convert('RGB'); sx=im.size[0]/W
    b=''
    for it in items:
        x,y,w,h,txt,st=it[:6]; o=it[6] if len(it)>6 else {}
        sp=o.get('sp',(x+1,y+1)); c=o.get('bg') or '#%02x%02x%02x'%im.getpixel((int(sp[0]*sx),int(sp[1]*sx)))
        al=o.get('al','left'); pad=o.get('pad',4)
        jc={'left':'flex-start','center':'center'}[al]
        b+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{c};display:flex;align-items:{o.get("ai","center")};justify-content:{jc};padding-left:{pad if al=="left" else 0}px;text-align:{al};{st}"><div>{txt if o.get("raw") else E(txt)}</div></div>'
    h=f'<html><head><meta charset=utf-8><link rel=stylesheet href=base.css><style>body{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:url("{src}") 0 0/{W}px {H}px}}</style></head><body>{b}</body></html>'
    open(f'{D}/p_{k}.html','w').write(h); return [f'{D}/p_{k}.html',W,H,f'{D}/out/{k}.png']
