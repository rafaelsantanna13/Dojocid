# Dojocid

Prévia da reconstrução: limpeza do acervo legado autorizada e aplicada. Todos os originais permanecem no ZIP preservado. A integração à main aguarda a revisão do usuário.

Site institucional estático, independente do Hostinger. Produção: https://dojocid.pages.dev/.

## Publicação

Cloudflare Pages continua conectado à branch `main`, com diretório de saída `site` e build vazio. Os HTML gerados estão versionados; não é necessário Python ou Node no servidor. Nenhum DNS ou domínio foi alterado. Não adicionar regras de redirecionamento para as mesmas URLs normalizadas pelo Pages.

## Manutenção

- `content/people.json`: biografias recuperadas; atualizar somente com informações confirmadas.
- `content/images.json`: associação das fotografias com os arquivos de origem.
- `scripts/build.py`: componentes compartilhados e geração das quatro páginas, sitemap e robots.
- `site/site.css` e `site/site.js`: apresentação e menu responsivo.
- `site/images`: WebP locais em dois tamanhos, sem serviço externo.

Com Python 3: `python scripts/build.py`. Para visualizar, `node scripts/serve.cjs` e abrir http://127.0.0.1:4173/. Com o servidor ativo, executar `python scripts/check.py`. O verificador usa apenas a biblioteca padrão. `node --check site/site.js` valida a sintaxe do JavaScript.

Para repetir a auditoria e otimização das imagens: instalar Pillow e numpy e executar `python scripts/audit_images.py` e `python scripts/optimize_images.py`. Esses scripts leem o ZIP preservado; a ordem semântica do inventário é registrada em `docs/image-audit.json`.

O ZIP de recuperação permanece intacto e contém todas as 221 imagens antigas, verificadas byte a byte antes da limpeza. O workflow manual antigo **Extrair site recuperado** é apenas para recuperação histórica: executá-lo sobre `main` pode restaurar a versão antiga. Não é parte da publicação normal.

## Verificação

Consulte `docs/AUDITORIA.md`, os relatórios JSON de testes e `docs/screenshots/`. O domínio canônico de produção é `dojocid.com.br`; sitemap, robots e metadados já estão preparados em `scripts/build.py`. A conexão do domínio deve ser concluída no Cloudflare Pages após a publicação na main.
