import json,patch
P=patch.patch;J=[]
K='font:600 9.5px Karla;letter-spacing:2px;'
TT='font:700 37px Butler;white-space:nowrap;'
BD='font:400 17px/24.5px Karla;'
J.append(P('s051',[
 (50,44,150,18,'OPTION A',K+'color:#b9b3aa'),(50,62,520,46,'Ask Claude',TT+'color:#fff'),
 (50,120,560,90,'Type in the chat what to change: “in slide 4 shorten the title, in slide 7 add the price”. Claude regenerates the file with the changes, without losing anything.',BD+'color:#d9d4cc',{'ai':'flex-start'}),
 (679,44,150,18,'OPTION B',K+'color:#75655c'),(679,62,520,46,'Duplicate and rename',TT+'color:#161d33'),
 (679,120,560,90,'Want to touch it up by hand? First duplicate the file and rename it (e.g. report_v2_Mario.docx). Work on the copy: Claude will not touch it.',BD+'color:#161d33',{'ai':'flex-start'}),
 (60,414,1170,26,'<b>Why?</b>&nbsp; When Claude edits a file it rewrites it from scratch: changes made by hand on the original are lost.','font:500 15px Karla;color:#fff',{'al':'center','raw':1})]))
AG='font:600 8.5px Karla;letter-spacing:1.8px;color:#75655c;'
AT='font:700 27px Butler;color:#161d33;white-space:nowrap;'
AS='font:400 15px Karla;color:#8a8d95;'
PL=lambda ps:''.join(f'<span style="background:#161d33;color:#fff;border-radius:12px;padding:3px 9px;margin-right:6px;font:600 11.5px Karla">{p}</span>' for p in ps)
items=[(462,24,365,58,'Claude (the main conversation)<br><span style="font:400 12.5px Karla;color:#b9b3aa">“Analyse the September fair”</span>','font:600 15px/22px Karla;color:#fff',{'al':'center','raw':1})]
for x,t,s,ps in [(97,'Photo Agent','analyses the stands',['skill: visual reading']),(499,'Press Agent','reads articles and social',['skill: press review']),(901,'Strategy Agent','draws the conclusions',['skill: tone of voice','skill: report pptx'])]:
    items+=[(x,163,90,16,'AGENT',AG),(x,180,290,34,t,AT),(x,224,290,22,s,AS),(x,253,290,25,PL(ps),'',{'raw':1})]
items.append((80,407,1130,26,'Agents work in parallel, each at its own desk. Skills give each one the method.','font:500 15px Karla;color:#fff',{'al':'center'}))
J.append(P('s062',items))
BT='font:700 27px Butler;color:#161d33;white-space:nowrap;'
BL='font:400 17px Karla;color:#161d33;white-space:nowrap;'
it=[]
for x,y,t,bs in [(45,34,'Skills',['Event brief','Run of show','Invitations','Report']),(45,268,'Agents',['Locations and suppliers','Communication','Logistics','Analysis']),
                 (973,34,'Connectors',['Mail','Calendar','Drive or SharePoint','Excel']),(973,268,'Scheduled',['Monday status','Guest list','Reminders','Final report'])]:
    it.append((x,y,250,34,t,BT))
    for j,s in enumerate(bs): it.append((x+19,y+47+j*29.3,230,27,s,BL))
it+=[(490,182,300,16,'PROJECT + FOLDER',AG+'color:#b9b3aa'),(490,200,320,46,'Events Office','font:700 37px Butler;color:#fff;white-space:nowrap'),
     (490,251,320,22,'instructions, suppliers, templates, events','font:400 13.5px Karla;color:#b9b3aa'),
     (470,321,350,24,'Output: Docs, Slides, Design, Excel files','font:500 14px Karla;color:#fff',{'al':'center'})]
J.append(P('s092',it))
LB='font:600 17px Karla;color:#fff;'
J.append(P('s107',[(45,y,150,30,t,LB) for y,t in zip([40,108,176,244,312,380],['Subject','Setting','Light','Framing','Style','Format'])]))
json.dump(J,open('j.json','w'))
