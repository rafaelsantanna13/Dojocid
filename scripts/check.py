"""Static checks and HTTP resource validation; no third-party dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from urllib.request import urlopen
import json,xml.etree.ElementTree as ET
class Page(HTMLParser):
 def __init__(self):super().__init__();self.tags=[]
 def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
root=Path('site'); checked=set();report=[]
for file in sorted(root.glob('*.html')):
 p=Page();p.feed(file.read_text(encoding='utf8')); tags=p.tags
 assert sum(t=='h1' for t,a in tags)==1,file
 assert any(t=='main' and a.get('id')=='conteudo' for t,a in tags),file
 assert any(t=='html' and a.get('lang')=='pt-BR' for t,a in tags),file
 assert any(t=='link' and a.get('rel')=='canonical' for t,a in tags),file
 assert any(t=='meta' and a.get('name')=='description' and a.get('content') for t,a in tags),file
 assert sum(a.get('aria-current')=='page' for t,a in tags)==1,file
 sources=[]
 for t,a in tags:
  if t=='img':assert all(x in a for x in ('alt','width','height','loading')),a
  for candidate in [a.get('href',''),a.get('src','')]+[part.strip().split(' ')[0] for part in a.get('srcset','').split(',') if part.strip()]:
   url=candidate;u=urlsplit(url)
   if u.scheme or not u.path:continue
   target=root/unquote(u.path.lstrip('/'))
   if u.path=='/':target=root/'index.html'
   elif not target.suffix:target=target.with_suffix('.html')
   assert target.is_file(),(file,url)
   if u.path not in checked:
    with urlopen('http://127.0.0.1:4173'+u.path) as response:assert response.status==200
    checked.add(u.path)
  if t=='img':sources.append(a['src'])
 assert len(sources)==len(set(sources)),('unnecessary repeated image',file)
 report.append({'page':file.name,'images':len(sources),'bytes':file.stat().st_size})
assert not (root/'_redirects').exists()
ET.parse(root/'sitemap.xml')
for image in (root/'images').glob('*.webp'):assert image.stat().st_size<400000,image
result=dict(pages=report,checked_http_resources=len(checked),published_bytes=sum(f.stat().st_size for f in root.rglob('*') if f.is_file()),redirect_rules=False)
Path('docs/static-tests.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
