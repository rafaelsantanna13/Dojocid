# Dojocid — migração para Cloudflare Pages

Este repositório receberá a cópia recuperada do site Dojocid.

## Importar o site

1. Na raiz do repositório, use **Add file → Upload files** para enviar `dojocid-corrigido.zip`.
2. Na aba **Actions**, execute o workflow **Extrair site recuperado**. Ele extrai o ZIP na pasta `site/` e faz commit na branch `main`.
3. Na Cloudflare, crie um projeto **Pages** integrado a este repositório. Use **Build command** vazio e **Build output directory** `site`.
4. Teste o endereço `pages.dev` antes de alterar o DNS de `dojocid.com.br`.

A versão recuperada é uma reconstrução simplificada, não uma cópia visual exata. Confira fotografias, conteúdo e links antes de cancelar a hospedagem antiga. Não inclua segredos no repositório público.
