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
 layout='gallery logos' if all(i in (1,2,3) for i,_ in items) else 'gallery'
 return '<section class="section wrap"><div class="section-heading"><p class="eyebrow">Nosso espaço, nossa equipe</p><h2>'+title+'</h2></div><div class="'+layout+'">'+''.join('<figure>'+img(i,alt)+'<figcaption>'+e(alt)+'</figcaption></figure>' for i,alt in items)+'</div></section>'
def render(path,title,desc,body):
 links=''.join(f'<a href="{url}"'+(' aria-current="page"' if path==url else '')+f'>{name}</a>' for url,name in routes)
 canonical='https://dojocid.pages.dev'+path
 doc=f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://dojocid.pages.dev/images/brasao-1200.webp">
<meta name="theme-color" content="#101213"><meta name="color-scheme" content="dark"><link rel="icon" type="image/webp" href="/images/brasao-480.webp"><link rel="stylesheet" href="/site.css"><script src="/site.js" defer></script></head>
<body><a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header><div class="wrap header-inner"><a class="brand" href="/" aria-label="Dojocid — início"><img src="/images/brasao-480.webp" width="52" height="52" alt="" loading="eager"><span>DOJOCID<small>ARTES MARCIAIS</small></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu" hidden>Menu <span aria-hidden="true">☰</span></button><nav id="menu" aria-label="Navegação principal">{links}<a class="nav-contact" href="{WA}">Agendar aula ↗</a></nav></div></header>
<main id="conteudo">{body}{cta()}</main>
<div class="mobile-contact">{button('Agendar aula experimental')}</div><footer><div class="wrap footer-inner"><div><a class="footer-brand" href="/">DOJOCID</a><p>Artes marciais em Copacabana</p><nav class="footer-nav" aria-label="Navegação do rodapé"><a href="/judo-e-jiu-jitsu">Judô e Jiu-Jitsu</a><a href="/boxe">Boxe</a><a href="/professores">Professores</a></nav></div><address>Rua Barata Ribeiro, 489 (CIB)<br>Copacabana · Rio de Janeiro<br><a href="tel:+5521992816485">21 99281-6485</a></address><div><a href="https://www.instagram.com/dojocid/">Instagram @dojocid ↗</a><br><a href="{WA}">Fale com a academia ↗</a><p>© 2026 Dojocid</p></div></div></footer></body></html>'''
 (SITE/('index.html' if path=='/' else path[1:]+'.html')).write_text(doc,encoding='utf8')
intro=f'''<section class="home-hero"><div class="wrap hero-grid"><div class="hero-copy"><p class="eyebrow"><span class="status-dot" aria-hidden="true"></span>Dojocid · Rio de Janeiro</p><h1>Artes marciais<br><span>em Copacabana.</span></h1><p class="hero-description">Judô, Jiu-Jitsu, Karatê, Boxe, Capoeira e Funcional.</p><div class="hero-actions">{button()}<a class="secondary-button" href="#modalidades">Conheça as modalidades ↓</a></div><p class="hero-address">Rua Barata Ribeiro, 489 (CIB)</p></div><figure class="hero-photo">{img(19,'Equipe reunida no tatame do Dojocid',eager=True)}<figcaption><span>Dojocid</span><span>No nosso tatame · Copacabana</span></figcaption></figure></div><nav class="hero-foot wrap" aria-label="Explore o Dojocid"><a href="#modalidades"><span>01</span> Modalidades ↗</a><a href="/professores"><span>02</span> Professores ↗</a><a href="#visite"><span>03</span> A academia ↗</a></nav></section>
<section class="section wrap" id="modalidades"><div class="section-heading section-heading-row"><div><p class="eyebrow">Escolha sua modalidade</p><h2>Seu próximo<br>encontro com o tatame.</h2></div><p>Conheça as modalidades e converse com a equipe para agendar sua aula experimental.</p></div><div class="modality-features">'''
for url,label,person,photo in [('/judo-e-jiu-jitsu','Judô e Jiu-Jitsu','Cid Nascimento',25),('/boxe','Boxe','Juan Joseph',12)]:
 intro+=f'<a class="modality-card" href="{url}"><div class="modality-photo">{img(photo,person)}</div><div class="modality-content"><div><p class="eyebrow">Professor {person}</p><h3>{label}</h3></div><span class="round-arrow" aria-hidden="true">↗</span></div><span class="card-link">Conhecer a modalidade</span></a>'
intro+=f'<div class="other-modalities"><p class="eyebrow">Também no Dojocid</p><div><a href="{WA}">Karatê ↗</a><a href="{WA}">Capoeira ↗</a><a href="{WA}">Funcional ↗</a></div><p>Consulte as aulas pelo WhatsApp.</p></div></div></section>'
intro+=f'<section class="team-section"><div class="wrap team-intro"><div><p class="eyebrow">Quem ensina</p><h2>Conheça quem está<br>com você no tatame.</h2></div><div><p class="team-names">Cid Nascimento · Juan Dias · Ana · Juan Joseph · Matheus Reis · Lucas</p><a class="secondary-button" href="/professores">Conheça os professores ↗</a></div></div></section>'
intro+=gallery([(17,'Turma reunida no Dojocid'),(21,'Aula infantil no tatame'),(6,'Treino de boxe com luvas')],'A academia em movimento')
intro+=f'<section class="space-section" id="visite"><div class="wrap split">{img(20,"Entrada do Dojocid, com brasão da academia", "space-photo")}<div><p class="eyebrow">Venha conhecer</p><h2>Copacabana.<br>Rio de Janeiro.</h2><address class="location-address">Rua Barata Ribeiro, 489 (CIB)<br>Copacabana · Rio de Janeiro</address><p>Fale com a equipe para consultar as aulas e agendar sua visita.</p><div class="location-links"><a class="secondary-button" href="https://www.google.com/maps/search/?api=1&amp;query=Rua+Barata+Ribeiro+489+Copacabana+Rio+de+Janeiro">Ver localização no mapa ↗</a><a class="text-link" href="tel:+5521992816485">21 99281-6485</a></div></div></div></section>'
render('/','Dojocid — Artes marciais em Copacabana','Conheça o Dojocid: Judô, Jiu-Jitsu e Boxe em Copacabana. Professores, academia e contato para agendar uma aula experimental.',intro)
for route,title,index,related in [('/judo-e-jiu-jitsu','Judô e Jiu-Jitsu',0,[(3,'Escola de Judô Cid Nascimento'),(1,'Checkmat')]),('/boxe','Boxe',3,[(12,'Registro de treino de boxe no Dojocid'),(2,'Boxe Para Todos — Juan Joseph')])]:
 p=people[index]
 body=f'<section class="page-intro wrap"><a class="back-link" href="/#modalidades">← Todas as modalidades</a><p class="eyebrow">Modalidades · Dojocid</p><h1>{title}</h1><p>Artes marciais em Copacabana</p>{button()}</section><section class="section wrap split profile-feature">{img(p["image"],p["name"],"portrait",True)}<div><p class="eyebrow">Professor</p><h2>{p["name"]}</h2>{bio(p)}<a class="text-link" href="/professores">Conheça toda a equipe →</a></div></section>'
 body+=gallery(related,'Na modalidade')
 render(route,title+' | Dojocid',f'{title} no Dojocid, em Copacabana. Conheça o professor {p["name"]} e entre em contato para uma aula experimental.',body)
body='<section class="page-intro wrap"><a class="back-link" href="/">← Voltar ao início</a><p class="eyebrow">A equipe Dojocid</p><h1>Quem está com você<br>no tatame.</h1><p>Conheça nossos professores, suas modalidades e trajetórias.</p><nav class="people-nav" aria-label="Escolha um professor">'+''.join(f'<a href="#professor-{i}">{p["name"]}</a>' for i,p in enumerate(people))+'</nav></section><section class="section wrap teacher-grid" aria-label="Professores">'
for i,p in enumerate(people):
 excerpt=p['paragraphs'][0].split('. ')[0].rstrip('.')+'.'
 body+=f'<article id="professor-{i}" class="teacher-card">{img(p["image"],p["name"],"portrait",i==0)}<div class="teacher-content"><p class="eyebrow">{p["modality"]}</p><h2>{p["name"]}</h2><p class="teacher-excerpt">{e(excerpt)}</p><details><summary>Trajetória e formação <span aria-hidden="true">+</span></summary><div class="teacher-bio">{bio(p)}</div></details></div></article>'
body+='</section>'
render('/professores','Professores | Dojocid','Conheça Cid Nascimento, Juan Dias, Ana, Juan Joseph, Matheus Reis e Lucas, professores do Dojocid em Copacabana.',body)
(SITE/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://dojocid.pages.dev'+p+'</loc></url>' for p,_ in routes)+'</urlset>\n')
(SITE/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://dojocid.pages.dev/sitemap.xml\n')
print('Generated four pages and sitemap.')
