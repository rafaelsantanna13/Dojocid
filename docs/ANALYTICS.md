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
