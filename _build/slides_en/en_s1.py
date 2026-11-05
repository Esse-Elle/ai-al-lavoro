from pptx import Presentation
from PIL import Image
import io
I='/tmp/claude-0/-home-claude/9246d2b0-a976-528c-81cc-8b69e6ccc473/scratchpad/intro/'
p=Presentation('en_full.pptx');s=p.slides[0]
for r in s.part.rels.values():
    if r.is_external: continue
    t=r.target_part
    if t.partname.endswith('.mp4'): t._blob=open(I+'intro_en.mp4','rb').read()
    if r.reltype.endswith('/image'):
        b=io.BytesIO(); im=Image.open(I+'intro_en-poster.jpg'); ow,oh=Image.open(io.BytesIO(t.blob)).size; im.resize((ow,oh)).save(b,'PNG'); t._blob=b.getvalue()
p.save('en_full.pptx'); print('ok')
