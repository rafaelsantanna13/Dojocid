# Revisão visual com fundos escuros — 14/11/2026

Pedido do usuário: melhoria geral antes de conectar o domínio, com preferência por fundos escuros e pesquisa de referências Gracie Barra e Alliance.

## Referências consultadas

- https://graciebarra.com/brasil/ — abertura com fotografia, hierarquia de títulos e aula introdutória em destaque.
- https://www.allianceofficial.com/ — navegação visual por grandes áreas, fotografia e contraste entre imagem, texto e fundo escuro.

As referências orientaram composição e navegação. Nenhuma fotografia, logotipo, texto, estatística, metodologia, certificação ou alegação de vínculo dessas academias foi incorporada ao Dojocid.

## Mudanças

- Preto e grafite no cabeçalho, corpo, cartões e rodapé das quatro páginas; textos claros e foco visível.
- Abertura com fotografia original da equipe, título legível e chamada para aula experimental; brasão preservado na marca.
- Acesso direto a modalidades, professores e academia; cartões com fotos e professores confirmados para Judô/Jiu-Jitsu e Boxe.
- Karatê, Capoeira e Funcional continuam como consultas pelo WhatsApp, sem informações inventadas.
- Página de professores com seis cartões e biografias completas em elementos nativos details/summary, operáveis pelo teclado e sem novo JavaScript.
- Localização com endereço confirmado e link de busca no Google Maps, sem mapa incorporado ou rastreamento.
- Contato acessível na parte inferior do celular, com espaço reservado para não cobrir o rodapé.
- Galerias com imagens reais, sem repetição da foto de abertura na mesma página. Retratos, logotipos e fotografia principal preservam os enquadramentos completos.

## Validação

- Quatro páginas em 320, 390, 768 e 1440 pixels: 16 verificações, sem overflow horizontal, sem imagem carregada quebrada, um H1 por página.
- Todas as fotos carregadas após percorrer as quatro páginas no celular; rodapé permanece acima do botão fixo.
- As seis biografias abrem e fecham com Enter; menu mobile abre e fecha com Escape.
- Console local sem erros ou avisos.
- Verificação estática e HTTP de 37 recursos; JavaScript e diff verificados.
- Capturas viewport da nova abertura em desktop/mobile e dos professores em docs/screenshots/dark-*.png. As capturas anteriores são histórico da primeira prévia. A captura integral via API apresentou falhas nesta revisão; a inspeção visual foi feita pelas capturas de viewport e navegação real.
- Nenhuma nota Lighthouse/axe foi produzida. Não houve alteração de DNS nem integração à main.

Os relatórios desta rodada estão em docs/dark-*-tests.json. A publicação de teste segue na branch codex/reconstrucao-dojocid e no PR #1.
