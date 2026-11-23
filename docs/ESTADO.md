# Estado do projeto — manita-site

Atualizado em: 2026-11-23
Por: Claude Opus 5.5 no Claude Code (app desktop)
Situação: em produção (GitHub Pages, <https://leokuli.github.io/manita-site/>)

## Onde parou

- 2026-10-20: página inicial e política de privacidade (1ª versão, só as contas Google).
- 2026-11-23, #1: kit de agentes (AGENTS.md, este arquivo, ADRs, glossário, conferidor das páginas, CI, `_config.yml`).
- 2026-11-23, **o PR que traz esta atualização**: política revista para o que a Manita faz hoje. Entram WhatsApp e
  Telegram, banco (Sicoob, Pix e boletos), certificados A1, documentos, portais que o titular autorizou, os provedores
  de IA (OpenAI e Anthropic) pelo nome e com os termos de API, e a guarda sem prazo até a pessoa pedir a exclusão
  (decisão do dono de 23/11, opção (a)), com as cópias de segurança por até 12 meses (30 diárias e 12 mensais; timer do
  backup conferido ativo na VPS em 23/11). **Só entra no ar com o sim final do dono.**

## Em curso

- O PR da política, aberto e verde, esperando o sim do dono para mesclar (o merge publica na hora).

## Próximo passo

1. Com o sim do dono: mesclar, conferir <https://leokuli.github.io/manita-site/privacidade.html> no ar (a data
   "23 de novembro de 2026"; se publicar em outro dia, trocar a data antes) e rodar `bash scripts/verificar`.
2. Daí em diante, ADR 0002: toda mudança no `assistente` que altere acesso, uso, compartilhamento, guarda ou limites
   revisa esta política no mesmo dia. Pontos a vigiar: a ordem dos provedores de IA (`IA_ORDEM` no compose), portal
   novo, e qualquer mudança de guarda (hoje sem prazo; specs 001, 002 e 018 do `assistente`).

## Bloqueios

- Publicar depende do sim do dono (declaração pública dele).

## Últimas decisões

- [ADR 0001](decisoes/0001-site-estatico-no-pages-para-o-app-google.md): site estático no GitHub Pages, endereço fixo.
- [ADR 0002](decisoes/0002-politica-acompanha-a-manita.md): a política acompanha o que a Manita faz, no mesmo dia.
- 2026-11-23 (dono): guarda sem prazo, apagar a pedido (ESQUECER); não 90 dias, que o sistema não faz e contrariaria
  as specs 001, 002 e 018 do `assistente`.

## Como retomar em 5 minutos

1. `bash scripts/verificar`
2. Ler `privacidade.html` inteira.
