# Revisão em Sistemas de Graduação em Escalada

**Goal:** Produzir revisão técnica bibliográfica sobre sistemas de graduação em escalada indoor, guia operacional de cores/CUD para o muro da UFRN (`Branco-Vazado` + 8 faixas) e proposta técnica `UFRN na CBE`.
**Scope & Non-Goals:** Mantém fontes modulares LaTeX (`doc/revisao_graduacao/`, `doc/guia_ufrn/`, `doc/ufrn_na_cbe/`), quadros de referência validados (`references/charts/`) e portal estático (`site/`).
**Definition of Done (DoD):** Todos os 3 PDFs compilam sem erros (`make`), scripts de quadros de referência validam integridade e aspect-ratio (`fetch_reference_charts.py`), e `uow.py check` passa em `main`.
**Next Steps:** Concluir revisão final do Guia UFRN (`doc/guia_ufrn/`) e integrar o portal estático (`site/`) para publicação.

Projeto de pesquisa bibliográfica, normatização técnica e aplicação prática para o muro de escalada da UFRN.

## Estrutura de Entregáveis
- `doc/revisao_graduacao/`: **Documento 1** (`revisao-graduacao-escalada.pdf`) — Revisão pública sobre normas, métodos de redução de subjetividade, benchmarking e apêndices (história, IRCRA/RIC, glossário).
- `doc/guia_ufrn/`: **Documento 2A** (`guia_ufrn.pdf`) — Guia operacional do muro da UFRN (9 faixas cromáticas com `Branco-Vazado` + CUD, calibração local e protocolo para *setters*).
- `doc/ufrn_na_cbe/`: **Documento 2B** (`ufrn_na_cbe.pdf`) — Proposta objetiva de equipe da UFRN na CBE.
- `site/`: Portal estático minimalista para hospedagem em página não listada (`lufreitas0000.github.io`).
