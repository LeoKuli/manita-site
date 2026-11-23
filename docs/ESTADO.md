# Estado do projeto — manita-site

Atualizado em: 2026-11-23
Por: Claude Opus 5.5 no Claude Code (app desktop)
Situação: em produção (GitHub Pages, <https://leokuli.github.io/manita-site/>)

## Onde parou

- Único commit de conteúdo: 2026-10-20, página inicial e política de privacidade ("Última atualização: 20 de outubro
  de 2026"). Pages ativo na `main`, raiz, estado `built` (lido pela API do GitHub em 2026-11-23).
- O kit de agentes (o PR que traz esta atualização): AGENTS.md, este arquivo, ADRs, glossário, o conferidor das
  páginas com controle positivo, o CI e o `_config.yml` que deixa o kit fora do site.

## Em curso

Nada aberto.

## Próximo passo

- Nenhum pedido aberto. Quando a Manita mudar o que acessa, guarda ou compartilha (no `assistente`), revisar a
  política e a data no mesmo dia (ADR 0002). Desde 20/10 a Manita ganhou, entre outras coisas, Pix e cobranças pelo
  Sicoob e canais de WhatsApp e Telegram; a política fala só das contas Google. **Conferir com o dono se a política
  precisa cobrir isso** (a tela de consentimento do Google é sobre os dados do Google, mas a seção 5 fala do servidor).

## Bloqueios

- A revisão da política acima depende do dono (é declaração pública dele).

## Últimas decisões

- [ADR 0001](decisoes/0001-site-estatico-no-pages-para-o-app-google.md): site estático no GitHub Pages, endereço fixo.
- [ADR 0002](decisoes/0002-politica-acompanha-a-manita.md): a política acompanha o que a Manita faz, no mesmo dia.

## Como retomar em 5 minutos

1. `bash scripts/verificar`
2. Ler `privacidade.html` inteira.
