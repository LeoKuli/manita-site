---
status: aceito
date: 2026-10-20
decision-makers: dono
---

# A política de privacidade acompanha o que a Manita faz, no mesmo dia

## Contexto e problema

A política declara ao Google e aos titulares o que a Manita acessa, para que usa, com quem compartilha, onde guarda,
os limites de segurança (lixeira em vez de apagar; não compartilhar arquivo sem confirmação) e o Uso Limitado das APIs
do Google. Se a Manita muda e a política não, a declaração fica falsa.

## Decisão

Toda mudança no `assistente` que altere acesso, uso, compartilhamento, guarda ou limites revisa `privacidade.html` e a
data "Última atualização" no mesmo dia, com o sim do dono para o texto. O conferidor (`scripts/conferir_paginas.py`)
exige os itens que o Google pede (contato, data, revogação, Política de Dados do Usuário e Uso Limitado).

### Consequências

- Bom: a declaração pública não envelhece em silêncio.
- Ruim: uma mudança de produto passa a ter um passo de documentação pública que depende do dono.

## Mais informações

`privacidade.html`, seções 1 a 9.
