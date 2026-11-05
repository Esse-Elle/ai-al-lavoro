import json,table,others as O
T=table.table;J=[]
J.append(T('s030',[(None,None,20,210),('Chat','t',210,515),('Cowork','n',522,928),('Code','t',934,1264)],[
 ['What it does','Answers, reasons, writes','Executes: files, folders, connectors, browser, even in the background','Writes and runs code on a project'],
 ['How you get there','You write in the conversation','Same conversation: Claude moves to the work on its own','Code tab, separate'],
 ['Example','“Give me 5 headlines for the newsletter”','“Read the brief in the folder and prepare the plan”','“Rename the 500 photos from the shoot”'],
 ['Permissions','None','Manual (asks) or Auto','You approve the steps']],W=1289,H=472,bottom=445,fs=17,hfs=25,x1=1268))
J.append(T('s039',[(None,None,19,197),('Haiku','t',197,440),('Sonnet','n',447,715),('Opus','t',721,988),('Fable','t',994,1263)],[
 ['Character','Fast and light','Balanced','Deep reasoning','Long projects on its own'],
 ['Usage','Low','Medium','High','Very high'],
 ['Use it for','Summaries, extractions, short answers','Everyday writing and analysis','Strategy, complex documents','Big, critical jobs'],
 ['Marketing','Summarise this email','Write 3 posts from the press release','Analyse the report and propose the plan','Build the entire launch kit']],
 W=1289,H=472,bottom=440,fs=17,hfs=25,x1=1268,nfs=10,ntop=452,note="The more powerful the model and the higher the effort, the more tokens each answer uses"))
J.append(O.s015([('Finding trends, data, competitor moves','Perplexity','','Cites sources: you can check'),
 ('Writing copy, press releases, product sheets','Claude','n','Consistent tone, polished texts'),
 ('Working inside Gmail, Drive, Docs','Gemini','','Already in the Google ecosystem'),
 ('Quick brainstorming, an image on the fly','ChatGPT','','Fast, images in chat'),
 ('Moodboards, settings, social visuals','Leonardo AI','','Control over visual style'),
 ('Automating a repetitive job','Claude','n','Folders, connectors, scheduled tasks')],['IF I NEED TO...','USE','WHY']))
J.append(O.s009([('TEXT AND IDEAS','ChatGPT','by OpenAI','The generalist',['Quick drafts','Images in chat','Lots of connected apps'],0),
 ('TEXT AND WORK','Claude','by Anthropic','The collaborator who reasons',['Polished texts','Works on files and tools','Docs, Slides, Design'],1),
 ('GOOGLE ECOSYSTEM','Gemini','by Google','The assistant in Gmail and Drive',['Already in your account','Mail, Drive, Docs','NotebookLM'],0),
 ('RESEARCH','Perplexity','by Perplexity AI','Research with sources',['Trends and competitors','Clickable sources','Comet browser'],0),
 ('IMAGES AND VIDEO','Leonardo AI','by Canva','The visual studio',['Moodboards and concepts','Images and video','Many models'],0)]))
J.append(O.s027([('Chat','You talk and reason it through'),('Projects',"The collaborator's memory"),('Artifacts','The finished document'),('Scheduled tasks','Works on its own, on a schedule'),
 ('Personalization','Knows you and how you write'),('Connectors & MCP','The sockets to your tools'),('Claude Design','The in-house graphic designer'),('Claude Code','The tool builder')]))
J.append(O.s038('WITH EVERY MESSAGE CLAUDE REREADS THE WHOLE CONVERSATION','new message','the whole history reread (attachments included)'))
json.dump(J,open('j.json','w'))
