import html,os
D=os.path.dirname(os.path.abspath(__file__))
E=html.escape
def cards(k,items,foot=None,W=1289,H=472,top=20,bottom=378,ftop=392,fh=60,pad=25,arrow=True,ffs=16,numsz=40,ttl=28,sub=None,body=19,bodycol='#6b6e76',extra_css='',bg='#f4f2ee'):
    n=len(items); g=24; cw=(W-2*pad-(n-1)*g)/n; gap=cw+g
    cs=[]
    for i,it in enumerate(items):
        x=pad+i*gap
        parts=[]
        if it.get('num') is not None: parts.append(f'<div class=num>{E(str(it["num"]))}</div>')
        if it.get('n'): parts.append(f'<div class=nn>{E(it["n"])}</div>')
        if it.get('pill'): parts.append(f'<div class="pill {it.get("pc","")}">{E(it["pill"])}</div>')
        if it.get('h'): parts.append(f'<div class=h>{E(it["h"])}</div>')
        if it.get('q'): parts.append(f'<div class=q>{E(it["q"])}</div>')
        if it.get('p'): parts.append(f'<div class=p>{E(it["p"])}</div>')
        if it.get('r'): parts.append(f'<div class=r><b>{E(it.get("rl","RESULT"))}</b><span>{E(it["r"])}</span></div>')
        cs.append(f'<div class="c {it.get("cls","")}" style="left:{x:.1f}px;width:{cw:.1f}px">{"".join(parts)}</div>')
        if arrow and i<n-1: cs.append(f'<div class=a style="left:{x+cw:.1f}px;width:24px">➞</div>')
    f=f'<div class=f>{E(foot)}</div>' if foot else ''
    h=f'''<html><head><meta charset=utf-8><link rel=stylesheet href=base.css><style>
body{{width:{W}px;height:{H}px;background:{bg};position:relative;overflow:hidden}}
.c{{position:absolute;top:{top}px;height:{bottom-top}px;background:#fff;border-radius:8px;padding:12px 15px}}
.c.dark{{background:#161d33}} .c.dark .h,.c.dark .p,.c.dark .nn{{color:#fff}}
.num{{width:{numsz}px;height:{numsz}px;border-radius:50%;background:#161d33;color:#fff;font:400 {numsz*.55:.0f}px/{numsz}px Butler;text-align:center;margin-top:4px}}
.nn{{font:400 21px Butler;color:#75655c}}
.pill{{display:inline-block;margin-top:8px;font:600 14.5px Karla;color:#fff;background:#75655c;border-radius:20px;padding:5px 11px;letter-spacing:.3px}}
.pill.y{{background:#9a8b7f}}.pill.d{{background:#161d33}}
.h{{font:700 {ttl}px/1.15 Butler;color:#161d33;margin-top:12px}}
.q{{font:600 15px Karla;color:#75655c;margin-top:12px;letter-spacing:.2px}}
.p{{font:400 {body}px/1.38 Karla;color:{bodycol};margin-top:10px;letter-spacing:.7px}}
.r{{position:absolute;left:15px;right:15px;bottom:14px;border-top:1px solid #c6c0b8;padding-top:10px}}
.r b{{display:block;font:600 8.5px Karla;letter-spacing:2px;color:#75655c}}.r span{{display:block;font:500 18px Karla;color:#161d33;margin-top:7px;letter-spacing:.3px}}
.a{{position:absolute;top:{top+(bottom-top)*.48:.0f}px;color:#75655c;font:600 16px Karla;text-align:center}}
.f{{position:absolute;left:{pad}px;right:{pad}px;top:{ftop}px;height:{fh}px;background:#161d33;border-radius:8px;color:#f4f2ee;font:400 {ffs}px Karla;display:flex;align-items:center;justify-content:center;letter-spacing:.3px;text-align:center;padding:0 20px}}
{extra_css}
</style></head><body>{"".join(cs)}{f}</body></html>'''
    open(f'{D}/k_{k}.html','w').write(h); return [f'{D}/k_{k}.html',W,H,f'{D}/out/{k}.png']
