import json,table
T=table.table
J=[]
J.append(T('s023',[(None,None,20,202),('ChatGPT','t',203,411),('Claude','n',417,626),('Gemini','t',630,837)],[
 ['Character','Versatile and fast','Thoughtful and precise','Integrated with Google'],
 ['Models today','GPT-6 Astra, Sol, Luna','Opus 5.5, Sonnet 5.5','Gemini 3.x Flash and Pro'],
 ['Long texts','Good','Key strength','Good'],
 ['Images','Generates them in chat','No photos: creates graphics and layouts','Generates them (Nano Banana)'],
 ['Working on files','Agent and connected apps','Folders, connectors, Chrome','Gmail, Drive, Docs'],
 ['Finished outputs','Canvas, files','Docs, Slides, Design','Google Docs and Sheets'],
 ['Automations','Automations and agents','Scheduled tasks','Google actions and agents'],
 ['Base plan','Plus, about $20','Pro, $20','AI Pro, about $20']],
 note="Data as of October 2026, monthly prices excluding VAT: check before the session"))
J.append(T('s029',[(None,None,20,351),('Desktop app','n',351,575),('Browser and mobile','t',580,837)],[
 ['Conversations, projects, artifacts','Yes','Yes'],['Docs, Slides, Design','Yes','Yes'],
 ['Folders on your computer','Yes','Only with the desktop app open'],
 ['Built-in browser and computer use','Yes','Only with the desktop app open'],
 ['Scheduled tasks','Yes, in the cloud too','Yes, in the cloud'],['Code tab','Yes','Separate web version'],
 ['Shortcuts and quick dictation','Yes','Limited'],['From any PC, no install','No','Yes']],bottom=603,fs=13))
J.append(T('s049',[(None,None,20,220),('Artifact','n',220,525),('File','t',532,837)],[
 ['What it is','A result that lives inside Claude','A real document: .docx, .pptx, .xlsx, .pdf'],
 ['Where you find it','Artifacts section, shareable link','In the working folder on your PC'],
 ['How you edit it','In the Claude editor or by asking Claude','With Office, or by asking Claude'],
 ['Best for','Docs, Slides, Design, live pages, mini apps','Deliverables, attachments, archive'],
 ['Switching','Exports to Word, PowerPoint, PDF','Can be published as an artifact']],bottom=605,fs=13))
J.append(T('s061',[(None,None,20,203),('Skill','n',203,492),('Agent','t',499,837)],[
 ['Metaphor','The manual on the shelf','The colleague with their own desk'],
 ['What it brings','Knowledge, method, format','A role you hand a whole task to'],
 ['Where it works','Inside the conversation','In a separate context, then reports back'],
 ['It kicks in','On its own, when the request matches','When Claude delegates the work to it'],
 ['How to create it','“Create a skill that...”','Role file, inside a plugin or in Code'],
 ['To get started','Yes: the most useful investment','Later, for big or parallel jobs']],bottom=605,fs=14))
J.append(T('s104',[('Model','t',23,296),('Best for','t',302,837)],[
 ['Lucid Origin','The all-rounder: concepts, social visuals, good aesthetics'],
 ['Lucid Realism','Photorealism: settings, still life, portraits'],
 ['Nano Banana, Pro, 2','Editing an image with words, infographics'],
 ['Seedream 4.0','Native 4K: ads and print'],['Ideogram 3.0','Readable text in the image: posters'],
 ['GPT Image 1.5','Precise editing, mockups'],['Flux 2 Pro / Kontext','Realism and faithful colours / editing from instructions'],
 ['Phoenix 1.0','Illustrations and vector-style graphics']],x0=20,bottom=593,fs=13,
 note="Model list from Leonardo.ai, October 2026"))
J.append(T('s105',[('Model','t',23,297),('Best for','t',302,837)],[
 ['Veo 3.1','Ads with a consistent product throughout the shot'],
 ['Kling 3.0 / Turbo','Cinematic camera moves, up to 15 s'],
 ['Kling Omni','Editing existing videos while keeping the subjects'],
 ['Seedance 2.x','Camera control, several consistent scenes, up to 4K'],
 ['MiniMax H3','Video with native audio: voice, ambience, music'],
 ['LTX-2','Native 4K, opening shots'],['Motion 2.0','Quick social teasers from a still image']],bottom=590,fs=13,
 note="Videos use far more tokens than images"))
json.dump(J,open('j.json','w'))
