from pathlib import Path
from PIL import Image,ImageOps
import json,zipfile,io
r=json.loads(Path('docs/image-audit.json').read_text()); out=Path('site/images'); out.mkdir(exist_ok=True)
names=['brasao','checkmat','boxe-para-todos','escola-judo','professor-tatame','treino-boxe','boxe-luvas','juan-dias','cordas','treino-solo','graduacao','ana','boxe-turma','lucas','matheus-reis','competicao','ana-variante','turma-jiu-jitsu','turma-judo','equipe','entrada','aula-infantil','tatame','juan-joseph','encontro','cid-nascimento']
manifest={}
for i,row in enumerate(r['selected']):
 if i == 16: continue  # Same photograph as Ana (11); original retained in ZIP.
 with zipfile.ZipFile('dojocid-corrigido.zip') as archive:
  key=next(k for k in archive.namelist() if k.replace('\\','/').endswith(row['path'][5:]))
  im=ImageOps.exif_transpose(Image.open(io.BytesIO(archive.read(key)))).convert('RGB')
 for width in (480,1200):
  copy=im.copy();copy.thumbnail((width,width*2));copy.save(out/f'{names[i]}-{width}.webp','WEBP',quality=85,method=6)
 manifest[str(i)]={'slug':names[i],'width':im.width,'height':im.height,'source':row['path']}
Path('content/images.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Optimized bytes:',sum(x.stat().st_size for x in out.iterdir()))
