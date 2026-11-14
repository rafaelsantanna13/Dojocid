"""Audit original recovered images directly from the preserved ZIP (Pillow + numpy)."""
from pathlib import Path
from PIL import Image,ImageDraw
import hashlib,json,numpy as np,zipfile,io
rows=[];groups={}
with zipfile.ZipFile('dojocid-corrigido.zip') as z:
 for key in sorted(z.namelist()):
  if Path(key).suffix.lower() not in ('.jpg','.jpeg','.png'):continue
  data=z.read(key);im=Image.open(io.BytesIO(data)).convert('RGB'); small=np.asarray(im.resize((9,8)).convert('L'))
  bits=''.join('1' if x else '0' for x in (small[:,1:]>small[:,:-1]).flatten())
  clean=key.replace('\\','/');clean=clean if clean.startswith('site/') else 'site/'+clean
  row=dict(path=clean,name=Path(key).name,width=im.width,height=im.height,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),dhash=hex(int(bits,2)))
  rows.append(row);groups.setdefault(row['name'],[]).append(row)
 selected=[max(g,key=lambda r:r['width']*r['height']) for g in groups.values()]
 # Stable semantic order is recorded in content/images.json, independent of ZIP traversal.
 existing=json.loads(Path('docs/image-audit.json').read_text())
 selected=sorted(selected,key=lambda r:[x['name'] for x in existing['selected']].index(r['name']))
 pairs=[]
 for i,a in enumerate(selected):
  for j,b in enumerate(selected[:i]):
   distance=(int(a['dhash'],16)^int(b['dhash'],16)).bit_count()
   if distance<=12:pairs.append(dict(a=i,b=j,distance=distance))
Path('docs/image-audit.json').write_text(json.dumps(dict(images=rows,selected=selected,perceptual_candidates=pairs),ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'images;',len(groups),'names;',len(set(r['sha256'] for r in rows)),'exact unique;',len(pairs),'cross-name perceptual candidates')
