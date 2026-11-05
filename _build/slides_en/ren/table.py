import html,os
D=os.path.dirname(os.path.abspath(__file__)); E=html.escape
def table(k,cols,rows,note=None,W=861,H=618,top=15,hh=43,body_top=65,bottom=None,fs=14,hfs=20,lab_first=True,x0=20,x1=None,gap=5,nfs=10.5,ntop=None):
    """cols: list of (header_text_or_None, color('n'|'t'|None), x_start, x_end)"""
    x1=x1 or W-24
    bottom=bottom or (590 if note else 605)
    n=len(rows); rh=(bottom-body_top)/n
    out=[]
    for i,(h,c,xa,xb) in enumerate(cols):
        if h: out.append(f'<div class="hd {c}" style="left:{xa}px;width:{xb-xa}px">{E(h)}</div>')
    for r,row in enumerate(rows):
        y=body_top+r*rh
        if r%2==0: out.append(f'<div class=zb style="top:{y:.1f}px;height:{rh:.1f}px;left:{x0}px;width:{x1-x0}px"></div>')
        for i,(h,c,xa,xb) in enumerate(cols):
            cls='lab' if (i==0 and lab_first) else 'cell'
            out.append(f'<div class={cls} style="top:{y:.1f}px;height:{rh:.1f}px;left:{xa}px;width:{xb-xa-6}px">{E(row[i])}</div>')
    if note: out.append(f'<div class=note>{E(note)}</div>')
    h=f'''<html><head><meta charset=utf-8><link rel=stylesheet href=base.css><style>
body{{width:{W}px;height:{H}px;background:#f4f2ee;position:relative;overflow:hidden}}
.hd{{position:absolute;top:{top}px;height:{hh}px;border-radius:5px;color:#fff;font:700 {hfs}px/{hh}px Butler;padding-left:11px;background:#75655c;white-space:nowrap}}
.hd.n{{background:#161d33}}
.zb{{position:absolute;background:#fff}}
.lab,.cell{{position:absolute;display:flex;align-items:center;padding-left:11px;font:400 {fs}px/1.35 Karla;color:#161d33;letter-spacing:.2px}}
.lab{{font-weight:600;color:#75655c;padding-left:14px}}
.note{{position:absolute;left:{x0}px;top:{ntop or bottom+6}px;font:400 {nfs}px Karla;color:#8a8d95}}
</style></head><body>{"".join(out)}</body></html>'''
    open(f'{D}/t_{k}.html','w').write(h); return [f'{D}/t_{k}.html',W,H,f'{D}/out/{k}.png']
