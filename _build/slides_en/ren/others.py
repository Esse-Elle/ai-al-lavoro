import html,os,glob
D=os.path.dirname(os.path.abspath(__file__)); E=html.escape
HEAD='<html><head><meta charset=utf-8><link rel=stylesheet href=base.css><style>body{width:%dpx;height:%dpx;background:#f4f2ee;position:relative;overflow:hidden}%s</style></head><body>%s</body></html>'
def save(k,W,H,css,body):
    open(f'{D}/o_{k}.html','w').write(HEAD%(W,H,css,body)); return [f'{D}/o_{k}.html',W,H,f'{D}/out/{k}.png']
def s015(rows,hdr):
    css='''.h{position:absolute;top:22px;font:600 10px Karla;letter-spacing:2px;color:#75655c}
.r{position:absolute;left:24px;width:1229px;height:63px;background:#fff;border-radius:6px}
.t{position:absolute;left:45px;font:400 19px Karla;color:#161d33;height:63px;display:flex;align-items:center}
.p{position:absolute;left:589px;height:31px;border-radius:16px;padding:0 16px;font:700 15px/31px Karla;color:#fff;background:#75655c}.p.n{background:#161d33}
.w{position:absolute;left:844px;font:400 17px Karla;color:#8a8d95;height:63px;display:flex;align-items:center}'''
    b=f'<div class=h style="left:36px">{E(hdr[0])}</div><div class=h style="left:589px">{E(hdr[1])}</div><div class=h style="left:844px">{E(hdr[2])}</div>'
    for i,(t,p,c,w) in enumerate(rows):
        y=48.6+i*68.3
        b+=f'<div class=r style="top:{y}px"></div><div class=t style="top:{y}px">{E(t)}</div><div class="p {c}" style="top:{y+16}px">{E(p)}</div><div class=w style="top:{y}px">{E(w)}</div>'
    return save('s015',1289,472,css,b)
def s009(cards):
    css='''.c{position:absolute;top:25px;width:236px;height:421px;background:#fff;border-radius:7px;padding:0 18px}.c.n{background:#161d33}
.k{position:absolute;top:19px;font:600 9px Karla;letter-spacing:1.3px;color:#75655c}
.ti{position:absolute;top:33px;font:700 34px Butler;color:#161d33;white-space:nowrap}
.by{position:absolute;top:85px;font:400 12px Karla;color:#8a8d95}
.ln{position:absolute;top:110px;left:18px;right:18px;height:1px;background:#d9d4cc}
.su{position:absolute;top:121px;left:18px;right:18px;font:400 19px/1.3 Butler;color:#161d33}
.bl{position:absolute;left:18px;font:400 15px Karla;color:#161d33}.bl:before{content:"";display:inline-block;width:5px;height:5px;border-radius:3px;background:currentColor;margin:0 8px 3px 2px}
.n .ti,.n .su,.n .bl{color:#fff}.n .k,.n .by{color:#b9b3aa}.n .ln{background:#3a4055}'''
    xs=[23,274,525,777,1028];b=''
    for x,(k,t,by,su,bl,n) in zip(xs,cards):
        b+=f'<div class="c {"n" if n else ""}" style="left:{x}px"><div class=k>{E(k)}</div><div class=ti>{E(t)}</div><div class=by>{E(by)}</div><div class=ln></div><div class=su>{E(su)}</div>'
        b+=''.join(f'<div class=bl style="top:{201+j*31.5}px">{E(s)}</div>' for j,s in enumerate(bl))+'</div>'
    return save('s009',1289,472,css,b)
def s027(items):
    css='''.c{position:absolute;width:294px;height:202px;background:#fff;border-radius:7px}.c.n{background:#161d33}
.nu{position:absolute;left:19px;top:14px;font:400 23px Butler;color:#75655c}
.ti{position:absolute;left:19px;top:68px;font:700 28px Butler;color:#161d33;white-space:nowrap}
.su{position:absolute;left:19px;top:115px;font:400 17px Karla;color:#8a8d95;white-space:nowrap}
.n .ti{color:#fff}.n .su{color:#d9d4cc}.n .nu{color:#b9b3aa}'''
    xs=[30,341,653,964];ys=[24,243];b=''
    for i,(t,s) in enumerate(items):
        b+=f'<div class="c {"n" if i in (1,3,5) else ""}" style="left:{xs[i%4]}px;top:{ys[i//4]}px"><div class=nu>{i+1:02d}</div><div class=ti>{E(t)}</div><div class=su>{E(s)}</div></div>'
    return save('s027',1289,472,css,b)
def s038(title,l1,l2):
    src=glob.glob(f'{D}/../pics/s038_*')[0]
    css=f'''body{{background:url("{src}") 0 0/1289px 472px}}.m{{position:absolute;background:#f4f2ee}}
.t{{position:absolute;left:34px;top:19px;font:600 11px Karla;letter-spacing:2px;color:#75655c}}
.l{{position:absolute;top:436px;font:400 14px Karla;color:#161d33}}'''
    b=f'<div class=m style="left:28px;top:14px;width:900px;height:22px"></div><div class=t>{E(title)}</div>'
    b+=f'<div class=m style="left:82px;top:434px;width:150px;height:22px"></div><div class=m style="left:262px;top:434px;width:600px;height:22px"></div>'
    b+=f'<div class=l style="left:86px">{E(l1)}</div><div class=l style="left:265px">{E(l2)}</div>'
    return save('s038',1289,472,css,b)
