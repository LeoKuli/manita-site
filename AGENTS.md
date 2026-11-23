# AGENTS.md — manita-site

> Fonte única de instruções para qualquer agente, de qualquer modelo (Claude, GPT/Codex, Gemini, Cursor, Copilot,
> modelo local). `CLAUDE.md`, `GEMINI.md` e `.github/copilot-instructions.md` só apontam para cá.

## Antes de tudo: retomar o trabalho

1. Leia este arquivo, depois [`docs/ESTADO.md`](docs/ESTADO.md).
2. Leia os ADRs aceitos em [`docs/decisoes/`](docs/decisoes/) e o [`docs/GLOSSARIO.md`](docs/GLOSSARIO.md).
3. `git log --oneline -20`, PRs e Issues abertos.
4. `bash scripts/verificar` antes de mudar qualquer coisa.

**Conflito com ADR aceito: pare e pergunte ao dono.** **No fim de toda sessão, atualize `docs/ESTADO.md`.**

## Objetivo do projeto

Site estático, no GitHub Pages (`main`, raiz), com a **página inicial** e a **política de privacidade** da Manita, a
assistente administrativa privada do dono (código no repositório privado `LeoKuli/assistente`). O app Google da
Manita aponta para estas páginas na tela de consentimento: **o site não pode sair do ar nem mudar de endereço**. NÃO é
o produto, não tem código de servidor nem formulário. O repositório é **público**.

## Como rodar e o comando único de "pronto"

```bash
bash scripts/verificar        # confere as duas páginas (e o controle que prova que o conferidor reprova); o mesmo no CI
```

Pré-requisitos: Python 3 e bash (no Windows, o Git Bash). Segundos. Para ver a página: abrir `index.html` no navegador.

## Mapa de pastas

- `index.html` — página inicial (o que é a Manita, link para a política, contato).
- `privacidade.html` — política de privacidade (dados acessados, uso, compartilhamento, guarda, limites de segurança,
  revogação, Uso Limitado das APIs do Google, LGPD).
- `scripts/conferir_paginas.py` — o conferidor das páginas, com o controle positivo (`--controle`).
- `_config.yml` — deixa os arquivos do kit (AGENTS.md, docs/...) fora do site publicado pelo Pages.
- `docs/` — estado, decisões, glossário (não publicados no site).

## Regras inegociáveis

- As regras do dono valem aqui: <https://github.com/LeoKuli/agentes-padroes/blob/main/docs/REGRAS-DO-DONO.md>.
- **Repositório e site públicos**: nada de segredo, dado de paciente ou de cliente, nem dado pessoal além do contato
  que a política já publica.
- **A política tem de dizer a verdade sobre a Manita.** Qualquer mudança no que a Manita acessa, guarda, compartilha
  ou nos limites dela (no repositório `assistente`) obriga a revisar `privacidade.html` e a data "Última atualização"
  no mesmo dia (ADR 0002). Mudar a política sem mudar a Manita, ou o contrário, deixa o app Google com declaração falsa.
- Não renomear nem mover `index.html` e `privacidade.html`; não desligar o Pages (ADR 0001).
- O conferidor só cresce: requisito novo do Google entra com a checagem e o controle.
- pt-BR; UTF-8 sem BOM, LF; Conventional Commits; nunca `push --force`.

## O que o agente NUNCA faz

- Mudar o texto da política sem o sim do dono (é declaração pública dele ao Google e aos titulares).
- Acrescentar script, rastreador, formulário ou recurso de terceiros às páginas.
- Mexer nas configurações do Pages ou do app Google.

## Como é um PR aceitável

- Um assunto por PR; `bash scripts/verificar` verde; `docs/ESTADO.md` atualizado.
- Merge: CI (`conformidade`, `segredos`, `verificar`) verde, depois `gh pr merge --squash --match-head-commit <sha>`. O
  merge publica o site na hora: depois dele, abrir <https://leokuli.github.io/manita-site/> e
  <https://leokuli.github.io/manita-site/privacidade.html> e conferir que as duas respondem.

## Onde está o conhecimento

| O quê | Onde |
|---|---|
| Estado e próximo passo | [`docs/ESTADO.md`](docs/ESTADO.md) |
| Decisões | [`docs/decisoes/`](docs/decisoes/) |
| Termos | [`docs/GLOSSARIO.md`](docs/GLOSSARIO.md) |
| O que a Manita faz de fato (fonte da verdade da política) | repositório privado `LeoKuli/assistente` (AGENTS.md, ADRs) |
| Regras do dono e skills de método | <https://github.com/LeoKuli/agentes-padroes> |
