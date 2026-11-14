"""Regenerate the four buildless HTML pages from shared components and recovered prose."""
from pathlib import Path
import json,html
ROOT=Path(__file__).resolve().parents[1]; SITE=ROOT/'site'
people=json.loads((ROOT/'content/people.json').read_text(encoding='utf8'))
images=json.loads((ROOT/'content/images.json').read_text(encoding='utf8'))
e=html.escape
WA='https://wa.me/5521992816485?text=Oi%2C%20estou%20vindo%20do%20site%20e%20quero%20agendar%20uma%20aula%20experimental'
routes=[('/', 'Início'),('/judo-e-jiu-jitsu','Judô e Jiu-Jitsu'),('/boxe','Boxe'),('/professores','Professores')]
def img(i,alt,cls='',eager=False):
 r=images[str(i)];slug=r['slug']; w=min(r['width'],1200);h=round(r['height']*w/r['width'])
 return f'<img class="{cls}" src="/images/{slug}-1200.webp" srcset="/images/{slug}-480.webp 480w, /images/{slug}-1200.webp {w}w" sizes="(max-width: 700px) 100vw, 50vw" width="{w}" height="{h}" alt="{e(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'>'
def button(label='Agendar aula experimental'): return f'<a class="button" href="{WA}">{label}<span aria-hidden="true"> ↗</span></a>'
def bio(p):return ''.join(f'<p>{e(t)}</p>' for t in p['paragraphs'])
def cta():return f'<section class="contact-band"><div class="wrap contact-inner"><div><p class="eyebrow">Dojocid · Copacabana</p><h2>Quer nos conhecer de verdade?</h2><p>Rua Barata Ribeiro, 489 (CIB), Copacabana.</p></div>{button()}</div></section>'
def gallery(items,title='No Dojocid'):
 return '<section class="section wrap"><div class="section-heading"><p class="eyebrow">Nosso espaço, nossa equipe</p><h2>'+title+'</h2></div><div class="gallery">'+''.join('<figure>'+img(i,alt)+'<figcaption>'+e(alt)+'</figcaption></figure>' for i,alt in items)+'</div></section>'
def render(path,title,desc,body):
 links=''.join(f'<a href="{url}"'+(' aria-current="page"' if path==url else '')+f'>{name}</a>' for url,name in routes)
 canonical='https://dojocid.pages.dev'+path
 doc=f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://dojocid.pages.dev/images/brasao-1200.webp">
<meta name="theme-color" content="#17191a"><link rel="icon" type="image/webp" href="/images/brasao-480.webp"><link rel="stylesheet" href="/site.css"><script src="/site.js" defer></script></head>
<body><a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header><div class="wrap header-inner"><a class="brand" href="/" aria-label="Dojocid — início"><img src="/images/brasao-480.webp" width="52" height="52" alt="" loading="eager"><span>DOJOCID<small>ARTES MARCIAIS</small></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu" hidden>Menu <span aria-hidden="true">☰</span></button><nav id="menu" aria-label="Navegação principal">{links}<a class="nav-contact" href="{WA}">WhatsApp ↗</a></nav></div></header>
<main id="conteudo">{body}{cta()}</main>
<footer><div class="wrap footer-inner"><div><a class="footer-brand" href="/">DOJOCID</a><p>Artes marciais em Copacabana</p></div><address>Rua Barata Ribeiro, 489 (CIB)<br>Copacabana · Rio de Janeiro<br><a href="tel:+5521992816485">21 99281-6485</a></address><div><a href="https://www.instagram.com/dojocid/">Instagram @dojocid ↗</a><br><a href="{WA}">Fale com a academia ↗</a><p>© 2026 Dojocid</p></div></div></footer></body></html>'''
 (SITE/('index.html' if path=='/' else path[1:]+'.html')).write_text(doc,encoding='utf8')
intro=f'''<section class="home-hero"><div class="wrap hero-grid"><div><p class="eyebrow">Rio de Janeiro · Copacabana</p><h1>Dojocid</h1><p class="hero-subtitle">Artes marciais<br>em Copacabana.</p><p class="hero-description">Judô, Jiu-Jitsu, Karatê, Boxe, Capoeira e Funcional.</p>{button()}<a class="text-link" href="/professores">Conheça os professores <span aria-hidden="true">→</span></a></div><div class="hero-emblem">{img(0,'Brasão Cid Nascimento Brazilian Jiu-Jitsu',eager=True)}</div></div><div class="hero-foot wrap"><span>Rua Barata Ribeiro, 489 (CIB)</span><a href="#modalidades">Conheça o Dojocid ↓</a></div></section>
<section class="section wrap" id="modalidades"><div class="section-heading"><p class="eyebrow">No tatame e além dele</p><h2>Modalidades</h2></div><div class="modalities">'''
for n,(url,label) in enumerate([('/judo-e-jiu-jitsu','Judô'),('/judo-e-jiu-jitsu','Jiu-Jitsu'),('/boxe','Boxe'),(None,'Karatê'),(None,'Capoeira'),(None,'Funcional')],1):
 intro+=f'<article class="modality"><span class="number">0{n}</span><h3>{label}</h3>'+ (f'<a href="{url}">Conheça {label} <span aria-hidden="true">↗</span></a>' if url else f'<a href="{WA}">Consulte as aulas <span aria-hidden="true">↗</span></a>')+'</article>'
intro+='</div></section>'
intro+=f'<section class="space-section"><div class="wrap split">{img(20,"Entrada do Dojocid, com brasão da academia", "space-photo")}<div><p class="eyebrow">A academia</p><h2>O Dojocid<br>em Copacabana.</h2><p>O Dojocid fica na Rua Barata Ribeiro, 489 (CIB), em Copacabana, no Rio de Janeiro.</p><p>Conheça a equipe, as modalidades e o espaço da academia.</p><a class="text-link" href="/professores">Conheça quem ensina →</a></div></div></section>'
intro+=gallery([(19,'Equipe reunida no tatame do Dojocid'),(21,'Aula infantil no tatame'),(6,'Treino de boxe com luvas')],'Um pouco da nossa rotina')
render('/','Dojocid — Artes marciais em Copacabana','Conheça o Dojocid: Judô, Jiu-Jitsu e Boxe em Copacabana. Professores, academia e contato para agendar uma aula experimental.',intro)
for route,title,index,related in [('/judo-e-jiu-jitsu','Judô e Jiu-Jitsu',0,[(3,'Escola de Judô Cid Nascimento'),(1,'Checkmat')]),('/boxe','Boxe',3,[(12,'Registro de treino de boxe no Dojocid'),(2,'Boxe Para Todos — Juan Joseph')])]:
 p=people[index]
 body=f'<section class="page-intro wrap"><p class="eyebrow">Modalidades · Dojocid</p><h1>{title}</h1><p>Artes marciais em Copacabana</p></section><section class="section wrap split profile-feature">{img(p["image"],p["name"],"portrait",True)}<div><p class="eyebrow">Professor</p><h2>{p["name"]}</h2>{bio(p)}<a class="text-link" href="/professores">Conheça toda a equipe →</a></div></section>'
 body+=gallery(related,'Na modalidade')
 render(route,title+' | Dojocid',f'{title} no Dojocid, em Copacabana. Conheça o professor {p["name"]} e entre em contato para uma aula experimental.',body)
body='<section class="page-intro wrap"><p class="eyebrow">Quem está com você no tatame</p><h1>Professores</h1><p>Conheça a equipe do Dojocid.</p><nav class="people-nav" aria-label="Escolha um professor">'+''.join(f'<a href="#professor-{i}">{p["name"]}</a>' for i,p in enumerate(people))+'</nav></section>'
for i,p in enumerate(people):
 body+=f'<section id="professor-{i}" class="teacher section wrap split">{img(p["image"],p["name"],"portrait",i==0)}<div><p class="eyebrow">{p["modality"]}</p><h2>{p["name"]}</h2>{bio(p)}</div></section>'
render('/professores','Professores | Dojocid','Conheça Cid Nascimento, Juan Dias, Ana, Juan Joseph, Matheus Reis e Lucas, professores do Dojocid em Copacabana.',body)
(SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://dojocid.pages.dev'+p+'</loc></url>' for p,_ in routes)+'</urlset>\n')
(SITE/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://dojocid.pages.dev/sitemap.xml\n')
print('Generated four pages and sitemap.')
