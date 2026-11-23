---
status: aceito
date: 2026-10-20
decision-makers: dono
---

# Publicar a página inicial e a política da Manita como site estático no GitHub Pages, com endereço fixo

## Contexto e problema

O app Google da Manita (Gmail, Drive, Planilhas, Agenda e Contatos) precisa, na tela de consentimento, de uma página
inicial e de uma política de privacidade públicas, num endereço estável.

## Opções consideradas

- Servir as páginas pelo próprio servidor da Manita.
- Site estático num repositório público, no GitHub Pages.

## Decisão

Escolhido o GitHub Pages (`main`, raiz), com duas páginas HTML sem script nem recurso de terceiros. O endereço não
muda e os arquivos não se renomeiam: o app Google publicado aponta para eles. Os arquivos do kit de agentes ficam fora
do site pelo `_config.yml`.

### Consequências

- Bom: não depende do servidor da Manita estar no ar; custo zero; histórico público de cada mudança na política.
- Ruim: apagar o repositório, desligar o Pages ou renomear uma página quebra a tela de consentimento do app.

## Mais informações

Commit `56685f5` (2026-10-20).
