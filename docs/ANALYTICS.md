# Google Analytics original — 15/11/2026

## Propriedade e instalação
O usuário confirmou o ID original **G-MV0EZNNB3Q**. A Google tag reutiliza esse fluxo GA4 existente; não foi criada propriedade nem fluxo. O histórico permanece na propriedade original. A instalação não recupera eventos que não tenham sido coletados durante a migração.

O cabeçalho compartilhado em scripts/build.py gera o carregamento assíncrono de gtag.js, a fila dataLayer, a inicialização e uma única chamada gtag('config', 'G-MV0EZNNB3Q') nas quatro páginas: Início, Judô e Jiu-Jitsu, Boxe e Professores. O config padrão gera page_view automaticamente; não há evento page_view manual, GTM ou segunda instalação no site.js. Não foram criados listeners de navegação ou de âncora.

A tag funciona em dojocid.com.br, www.dojocid.com.br e dojocid.pages.dev, sem restrição por hostname. As prévias também enviam dados à propriedade original; usar a dimensão hostname para distinguir testes e produção. Configurações de filtros, consentimento, medição otimizada e destinos da Google tag na conta existente não foram alteradas nem inspecionadas. Bloqueadores e configurações da propriedade podem impedir que uma visita apareça.

## Validação executável
- python scripts/build.py: gera as quatro páginas.
- node scripts/check-analytics.cjs: exige um loader assíncrono no head e uma inicialização por página, verifica o ID, executa a fila em sandbox para três hostnames e rejeita disparos page_view manuais/instalações concorrentes.
- python scripts/check.py: confere recursos, páginas, imagens e links HTTP.
- O workflow Verificar site executa o teste de Analytics em cada push/PR.

Os testes em sandbox verificam o código emitido, não a recepção dos dados pelo Google. Confirmar coleta em produção com Tag Assistant e no relatório autenticado. Sem acesso à propriedade não é possível certificar a chegada dos eventos.

## Como validar no GA4
1. Abra https://analytics.google.com/ e selecione a propriedade original. Em Administração > Fluxos de dados > fluxo Web, confirme G-MV0EZNNB3Q. Não crie outro fluxo.
2. Abra Relatórios > Tempo real.
3. Em outro navegador ou celular, sem bloqueador e com o consentimento aplicável, visite https://dojocid.com.br/ e navegue por /judo-e-jiu-jitsu, /boxe e /professores. Repita em https://dojocid.pages.dev para testar esse ambiente.
4. Confira usuários recentes, eventos page_view e visualizações por título. A coleta pode levar até 30 minutos para começar. Filtros de tráfego interno também podem ocultar seu teste.
5. Em https://tagassistant.google.com/, conecte o domínio e confirme o destino G-MV0EZNNB3Q. Para cada carregamento completo, verifique um page_view; eventos session_start e user_engagement são distintos e esperados. Mudanças apenas de âncora não recebem disparos manuais do site.
6. Alternativamente, DevTools > Network: filtre por collect e verifique o ID em tid e page_view em en. Considere requisições em lote ao contar eventos. O relatório em tempo real sozinho não comprova ausência de duplicação.

## Auditoria anterior e escopo
O ID não estava no ZIP recuperado nem nos primeiros commits; sua origem foi confirmada pelo usuário. As quatro páginas anteriores na main não tinham tag. O gerador e as páginas mantêm canonical, Open Graph, sitemap, robots e URLs de produção. Não há alteração de DNS ou domínio.

Fontes oficiais:
- https://support.google.com/analytics/answer/14183469
- https://support.google.com/analytics/answer/9271392
- https://support.google.com/analytics/answer/9311124


## Conversão de WhatsApp: CliqueZapEvento
O proprietário confirmou por capturas que CliqueZapEvento é o nome exato e já está marcado como evento principal. Foi criada uma regra derivada de click com link_url contendo wa.me/5521992816485, mas o teste do proprietário não exibiu o evento principal. A causa dessa falha não foi comprovada. Para adotar um único caminho explícito, o proprietário confirmou a remoção SOMENTE dessa regra; a marcação como evento principal foi mantida.

site/whatsapp.js envia diretamente gtag('event', 'CliqueZapEvento', ...) para G-MV0EZNNB3Q. O script é incluído uma vez no cabeçalho compartilhado das quatro páginas. Um listener delegado atende todos os 25 links (incluindo um botão fixo mobile por página), com suporte a clique em texto/ícone, teclado e botão central. Há proteção contra instalação repetida do script. Não há bloqueio da navegação, redirecionamento programado ou timeout; o transporte beacon é solicitado para enviar o evento durante a saída. Se a tag estiver bloqueada ou indisponível, o link continua funcionando, mas a coleta não pode ser garantida.

O evento mede intenção de abrir contato, NÃO envio de mensagem. Só são aceitos links HTTPS para wa.me/5521992816485. O parâmetro link_url do evento personalizado contém apenas origem e caminho, sem o texto da mensagem. O URL real do link e sua mensagem preenchida permanecem inalterados. Nenhum page_view é disparado manualmente.

O click automático de medição otimizada pode coexistir como evento distinto. Não recriar a regra que transforma click em CliqueZapEvento, nem adicionar um disparo igual em GTM, pois isso duplicaria a conversão. A estrela do evento principal existente deve permanecer, e o click genérico não deve ser tratado como conversão específica de WhatsApp.

### Testes executados e limites
node scripts/check-whatsapp.cjs executa o script em sandbox para dojocid.com.br, www.dojocid.com.br e dojocid.pages.dev, exercitando todos os 25 links (75 combinações). Verifica um evento por clique, proteção contra dupla instalação, cliques em elementos filhos, botão central, repetição legítima de cliques, exclusão de outros links/destinos e ausência de preventDefault/stopPropagation, inclusive quando Analytics está bloqueado. O teste integra o workflow de CI. O inventário está em docs/whatsapp-link-audit.json.

A validação GA4 já existente continua verificando uma tag/config e nenhum page_view manual. O verificador HTTP confere recursos e links. Nenhuma alteração em canonical, sitemap, robots, DNS ou domínio.

O navegador de automação deste ambiente está indisponível por falha de inicialização, e não há conexão autenticada com a propriedade GA4. Os testes de sandbox não comprovam que o Google recebeu o evento nem substituem teste real no aplicativo. Não foi enviada mensagem pelo WhatsApp.

### Validação real após publicação
1. Abrir a propriedade original G-MV0EZNNB3Q em Relatórios > Tempo real e confirmar que CliqueZapEvento continua marcado como principal.
2. No celular ou navegador sem bloqueador e com o consentimento aplicável, abrir https://dojocid.com.br e clicar UMA vez no WhatsApp. Confirmar o número e a mensagem no aplicativo, sem enviar.
3. Procurar CliqueZapEvento na contagem por nome e nos eventos principais. click pode aparecer como evento genérico separado. Não esperar que os dois eventos tenham o mesmo nome ou confundir user_engagement com duplicação.
4. Para testar duplicidade com precisão, conectar https://tagassistant.google.com/ ao site, conferir o destino G-MV0EZNNB3Q e acompanhar DebugView do dispositivo. Cada clique deve gerar UMA ocorrência de CliqueZapEvento. Repetir em cabeçalho, conteúdo, rodapé e botão fixo mobile, e no ambiente https://dojocid.pages.dev.
5. Em DevTools > Network, filtrar collect e verificar tid=G-MV0EZNNB3Q e en=CliqueZapEvento, considerando requisições em lote. Filtros internos, bloqueadores e configurações de consentimento podem ocultar testes; não alterar esses controles sem avaliar a conta.

Fontes:
- https://support.google.com/analytics/answer/9216061
- https://support.google.com/analytics/answer/7201382
