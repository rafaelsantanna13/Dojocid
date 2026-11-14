# Auditoria e reconstrução — 14/11/2026

**Estado atual: prévia para teste, com limpeza autorizada pelo usuário em 14/11/2026.** Os 221 arquivos de imagem e quatro arquivos legados foram removidos de site/ após nova conferência dos hashes com o ZIP preservado. O conjunto publicado tem aproximadamente 3 MB. A integração à main aguarda a revisão do usuário.

## Estado inicial e referências

Repositório inicial: `84bf82e`. Quatro páginas HTML, CSS escuro/dourado sem o brasão, galerias com todas as variantes desktop/mobile exibidas simultaneamente, textos de professores agrupados sem identificação individual, 221 imagens (24.972.795 bytes), CSS residual do construtor e ZIP de recuperação.

As quatro páginas originais foram acessadas no navegador: https://dojocid.com.br/, /judo-e-jiu-jitsu, /boxe e /professores. O primeiro acesso à página de professores pela ferramenta de pesquisa retornou 502, mas o navegador posteriormente carregou o conteúdo e confirmou nomes, imagens, modalidades, biografias e idiomas. A versão antiga em https://dojocid.pages.dev/ também foi inspecionada no navegador.

O original usa navegação branca, Roboto/sans-serif, seções escuras, o brasão Cid Nascimento, fotografias reais e CTA de aula experimental. Sua renderização no navegador deste ambiente apresentou blocos muito altos, rolagem horizontal e imagens genéricas de ondas/arquitetura. A reconstrução preserva brasão, paleta neutra, navegação, conteúdo e fotografias, com reorganização responsiva; não é réplica pixel a pixel desses defeitos. Capturas de referência estão em `screenshots/original-*.png`.

## Conteúdo e associações

- Cid Nascimento: Judô e Jiu-Jitsu; foto `img-20251110-wa0021`.
- Juan Dias: Jiu-Jitsu; foto `img-20260812-wa0012`.
- Ana: Judô e Jiu-Jitsu conforme título do original; foto `img-20260811-wa0045`.
- Juan Joseph: Boxe; foto `img_20251110_165040`.
- Matheus Reis: Judô e Jiu-Jitsu; foto `1787178846137`.
- Lucas: Judô e Jiu-Jitsu; foto `1787003137178`.

Associações confirmadas pela seção correspondente no original, não inferidas apenas por aparência. Biografias preservadas do material recuperado e comparadas ao original; os títulos esportivos são declarações do próprio site, sem pesquisa independente sobre sua atualidade. Os idiomas de Cid, Juan Dias e Ana foram confirmados no original. Nenhum preço, horário ou nova credencial foi criado. Karatê, Capoeira e Funcional constam da página inicial original e permanecem como consultas via contato, sem páginas ou professores inventados. Instagram corrigido para @dojocid (o cabeçalho original tinha um link genérico para instagram.com).

## Fotografias

SHA-256: 221 arquivos, 180 hashes únicos, portanto 41 cópias exatas excedentes. Agrupamento pelo nome de origem: 26 grupos. Seleção pela maior área útil recuperada, sem ampliação; todas as 221 cópias estão preservadas e foram comparadas byte a byte ao ZIP antes de retirar a árvore legada da publicação.

dHash de 64 bits e revisão visual da folha de contato: dois pares entre nomes diferentes ficaram abaixo do limiar de 12 bits. O par Ana / ana-variante (distância 0) é a mesma fotografia e apenas a melhor versão foi mantida em WebP. O par Lucas / Matheus (distância 1) mostra pessoas diferentes diante do mesmo cenário e foi preservado. Semelhança perceptual não foi usada como autorização automática de exclusão.

Resultado: 25 imagens de origem em duas larguras WebP (50 arquivos), inclusive fotografias relevantes preservadas para uso futuro. As páginas exibem seleções contextuais, não um mural de todas as variantes. Retratos e logotipos usam `object-fit: contain`; fotos de ambiente usam enquadramento adequado. `srcset`, dimensões explícitas, lazy loading fora da abertura e carregamento prioritário da imagem principal.

Os fundos genéricos de Unsplash e placeholders do construtor foram dispensados. Não há fotografias externas ou imagens artificiais. A transparência do logotipo Checkmat foi preservada; a inspeção final está em screenshots/checkmat-final.png. Nenhuma dependência de Hostinger, fontes remotas, rastreamento ou scripts de terceiros permanece.

## Implementação

HTML/CSS/JS estáticos, geração opcional em Python para compartilhar cabeçalho e rodapé, sem framework e sem build obrigatório no Pages. Quatro páginas com navegação consistente, menu progressivo com teclado/Escape, foco visível, link de pulo, semântica, um H1 por página, metadados próprios, canonical, Open Graph, sitemap e robots. As URLs sem extensão seguem a normalização nativa do Cloudflare; não existe `_redirects`.

## Testes e limites

- Verificação estática e HTTP em `scripts/check.py`: quatro páginas, 36 recursos referenciados, caminhos e variantes srcset existentes, alt/dimensões, H1, main, idioma, canonical, descriptions, item atual de navegação, ausência de imagens repetidas no mesmo contexto e sitemap XML válido. Zero falhas na execução final.
- Navegador: quatro páginas a 390×844 e 1440×1000, sem overflow horizontal, um H1, um item de menu atual e sem alt ausente. Todas as imagens carregaram após percorrer cada página, em ambos os tamanhos. Console sem avisos/erros durante a verificação local.
- Menu mobile abre/fecha, atualiza aria-expanded, fecha com Escape e permite navegação para Boxe.
- Capturas integrais desktop/mobile revisadas; capturas depois de percorrer a página incluem as imagens carregadas sob demanda.
- `node --check site/site.js`, `node --check scripts/serve.cjs` e `git diff --check`.
- Site publicado tem aproximadamente 2,98 MB no total (contra 25 MB apenas das imagens antigas). Sem nota Lighthouse/axe: essas auditorias não foram executadas. Não se afirma certificação de acessibilidade.
- Links de WhatsApp, telefone e Instagram conferidos contra o original; nenhuma mensagem foi enviada e nenhum agendamento real foi feito.
- O servidor local testa resolução das rotas sem redirecionamento, mas não simula toda a plataforma Pages. URLs HTML e ausência de loops precisam também ser confirmadas após deploy.

As credenciais e a infraestrutura não foram alteradas. O ZIP não foi excluído. O status de PR, integração e deploy é informado no relatório final da conversa, após a execução dessas etapas.
