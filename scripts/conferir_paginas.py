"""Confere as duas páginas do manita-site, que o app Google da Manita usa na tela de consentimento.

O que reprova (cada item é exigência do Google para app com escopos de Gmail/Drive, ou do próprio site):
- HTML com tag de bloco aberta e não fechada (html, head, body, h1, h2, p, ul, li, a);
- index.html sem link para privacidade.html, ou sem contato (mailto:);
- privacidade.html sem: contato (mailto:), a data "Última atualização", o link de revogação
  (myaccount.google.com/permissions), a Política de Dados do Usuário das APIs do Google e o "Uso Limitado".
Uso:  python scripts/conferir_paginas.py [raiz]      (só biblioteca padrão)
      python scripts/conferir_paginas.py --controle   (prova que o conferidor reprova uma página quebrada)
"""
from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path

BLOCOS = {"html", "head", "body", "h1", "h2", "p", "ul", "li", "a", "title", "style"}


class Tags(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.pilha: list[str] = []
        self.erros: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.links += [v for k, v in attrs if k == "href" and v]
        if tag in BLOCOS:
            self.pilha.append(tag)

    def handle_endtag(self, tag):
        if tag not in BLOCOS:
            return
        if not self.pilha or self.pilha[-1] != tag:
            self.erros.append(f"</{tag}> sem par (aberto: {self.pilha[-1] if self.pilha else 'nada'})")
            if tag in self.pilha:
                while self.pilha and self.pilha.pop() != tag:
                    pass
            return
        self.pilha.pop()


def conferir(nome: str, texto: str) -> list[str]:
    t = Tags()
    t.feed(texto)
    falhas = [f"{nome}: {e}" for e in t.erros]
    if t.pilha:
        falhas.append(f"{nome}: tags abertas sem fechar: {t.pilha}")
    if not any(h.startswith("mailto:") for h in t.links):
        falhas.append(f"{nome}: sem contato (mailto:)")
    if nome == "index.html" and "privacidade.html" not in t.links:
        falhas.append("index.html: sem link para privacidade.html")
    if nome == "privacidade.html":
        exigidos = {
            "Última atualização": "a data da última atualização",
            "myaccount.google.com/permissions": "o link de revogação do acesso",
            "api-services-user-data-policy": "a Política de Dados do Usuário das APIs do Google",
            "Limited Use": "o requisito de Uso Limitado",
        }
        for trecho, oque in exigidos.items():
            if trecho not in texto:
                falhas.append(f"privacidade.html: falta {oque} ({trecho!r})")
    return falhas


def main(argv: list[str]) -> int:
    if argv[:1] == ["--controle"]:
        quebrada = "<html><body><h1>Política</h1><p>sem contato<p></body></html>"
        falhas = conferir("privacidade.html", quebrada)
        print("controle: " + ("REPROVOU, como devia" if falhas else "NÃO REPROVOU (o conferidor está cego)"))
        return 0 if falhas else 1
    raiz = Path(argv[0] if argv else ".")
    falhas = []
    for nome in ("index.html", "privacidade.html"):
        caminho = raiz / nome
        if not caminho.is_file():
            falhas.append(f"{nome}: ausente")
            continue
        falhas += conferir(nome, caminho.read_text(encoding="utf-8"))
    for f in falhas:
        print("FALHA  " + f)
    print("páginas: " + ("ok" if not falhas else f"{len(falhas)} falha(s)"))
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
