import json,patch,html
P=patch.patch;E=html.escape;J=[]
NM=lambda n,s,d=None:f'<span style="font:700 {s}px Butler;color:#161d33">{E(n)}</span>'
DS='font:400 14px Karla;color:#6e6a66;white-space:nowrap'
it=[]
for x,y,n,d,s in [(88,46,'Marketing-Claude','the project folder',24),(144,113,'00_ReadMe','instructions, tone of voice, rules',23),(144,181,'01_Brand','brand book, logo, palette, fonts',23),(144,248,'02_Products','catalogues, sheets, price lists',23),
 (144,316,'03_Approved-examples','texts and posts to imitate',23),(144,384,'04_Input','briefs, data exports, new materials',23),(144,451,'05_Output','where Claude saves the work',23),(144,518,'_Archive','old versions',23)]:
    it.append((x-4,y-18,470,38,NM(n,s)+f'<span style="margin-left:14px;{DS}">{E(d)}</span>','white-space:nowrap',{'raw':1,'pad':4}))
J.append(P('s046',it,861,618))
it=[]
for x,y,n,d,s in [(87,46,'Events-Office','the project folder',23),(137,113,'00_ReadMe','rules, tone, typical budget',23),(137,181,'01_Suppliers-Locations','list with contacts and prices',23),(137,248,'02_Templates','briefs, budgets, run of show, invitations',23),
 (137,316,'03_Events','one folder per event',23),(187,384,'2026-11_Showroom','brief, guests, photos, report',23),(187,451,'2027-04_Salone','brief, guests, photos, report',23),(137,518,'_Archive','past events',23)]:
    it+=[(x-4,y-17,330,33,NM(n,s),'white-space:nowrap',{'raw':1}),(x-4,y+18,300,21,d,'font:400 13.5px Karla;color:#6e6a66;white-space:nowrap')]
J.append(P('s093',it,861,618))
code='''---
name: brand-tone-of-voice
description: Use this skill when you write
  copy, posts, press releases or newsletters
  for the brand. Applies tone and rules.
---

# Tone of voice
Elegant, warm, never shouted.
Short sentences. No empty superlatives.

## Words yes / words no
Yes: material, light, project, made to measure
No: incredible, top, unmissable

## Approved examples
See examples/approved_posts.md'''
J.append(P('s055',[(48,46,520,480,f'<pre style="margin:0;font:400 15.6px/28px \'DejaVu Sans Mono\',monospace;color:#f1ede6">{E(code)}</pre>','',{'raw':1,'ai':'flex-start','pad':7}),
 (588,94,215,20,'when it kicks in','font:600 12.5px Karla;color:#fff'),(588,289,215,20,'the method','font:600 12.5px Karla;color:#fff'),(588,484,215,20,'attached materials','font:600 12.5px Karla;color:#fff')],861,618))
K='font:600 9.5px Karla;letter-spacing:2px;';M='font:400 17.5px Karla;white-space:nowrap;'
J.append(P('s078',[(60,34,300,16,'EVERY HOUR',K+'color:#c9c3ba'),(60,53,600,24,'The scheduled task starts',M+'color:#fff'),
 (60,113,300,16,'READS',K+'color:#75655c'),(60,131,700,24,'New emails with PDFs: is it an invoice?',M+'color:#161d33'),
 (60,191,300,16,'EXTRACTS',K+'color:#75655c'),(60,209,700,24,'Supplier, number, amount, reference',M+'color:#161d33'),
 (60,269,300,16,'DECIDES',K+'color:#75655c'),(60,287,700,24,'Looks up the supplier in the “who gets what” table',M+'color:#161d33'),
 (60,400,300,16,'FOUND',K+'color:#161d33'),(60,422,340,46,"Forwards it to the right contact and saves the PDF in the supplier's folder",'font:400 15px/20px Karla;color:#161d33',{'ai':'flex-start'}),
 (465,400,300,16,'UNSURE OR NOT FOUND',K+'color:#75655c'),(465,422,340,46,"It doesn't guess: it sets it aside and flags it to you",'font:400 15px/20px Karla;color:#161d33',{'ai':'flex-start'}),
 (90,544,690,26,'Excel log updated + end-of-day summary','font:500 17px Karla;color:#fff',{'al':'center'})],861,618))
S='font:500 17px Karla;color:#161d33;white-space:nowrap'
it=[(71,67,190,26,'+ New conversation',S)]+[(71,y-13,180,26,t,S) for y,t in [(125,'Recents'),(170,'Projects'),(215,'Artifacts'),(260,'Scheduled')]]
it+=[(632,78,330,24,'Prepare the campaign report','font:400 15px Karla;color:#161d33'),(305,228,365,24,'Can I send the draft?  [Allow] [Deny]','font:400 14px Karla;color:#161d33'),
 (307,364,300,24,'Type what you need...','font:400 15px Karla;color:#8a8d95'),(386,408,68,20,'Manual','font:500 14px Karla;color:#161d33',{'al':'center'}),
 (782,408,172,20,'Sonnet 5.5 · Medium effort','font:500 13px Karla;color:#161d33;white-space:nowrap',{'al':'center'}),
 (1029,59,130,16,'PROGRESS','font:600 10px Karla;letter-spacing:2px;color:#75655c',{'pad':0}),(1029,199,130,16,'CONTEXT','font:600 10px Karla;letter-spacing:2px;color:#75655c',{'pad':0})]
it+=[(1018,y-12,200,25,t,'font:400 16px Karla;color:#161d33') for y,t in [(235,'• Folders'),(265,'• Connectors'),(295,'• Skills')]]
L=['Sidebar: Recents, Projects, Artifacts, Scheduled','Conversation: requests and answers','Approvals: Allow or Deny','Input: + attach or Research, / for skills',
   'Model, effort, Manual or Auto permissions','Progress: the steps under way','Context: folders, connectors, skills','Output: the files created, ready to open']
for i,t in enumerate(L): it.append(((66 if i<4 else 712),[517,556,595,634][i%4]-14,540,29,t,'font:400 19px Karla;color:#161d33;white-space:nowrap'))
J.append(P('s033',it,1333,750))
json.dump(J,open('j.json','w'))
