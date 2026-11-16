# Diretrizes de Operação — revisao-graduacao-escalada

Este repositório segue a arquitetura de governança adaptada de `project-governance` para produção documental em LaTeX, pesquisa bibliográfica verificada e publicação web estática.

## Hierarquia de Autoridade
1. Fontes primárias verificadas em `references/` prevalecem sobre resumos ou memória de LLM.
2. `PROJECT_STATE.yaml` registra o estado real validado (não intenções).
3. Rascunhos, extratos não auditados e experimentos ficam isolados em `doc/rnd/`.

## Regras Ativas (`.agents/rules/`)
- `01_editorial_and_provenance.md`: Rastreabilidade estrita (`% SOURCE [...]`), proibição de alucinações e corte de dados não verificados.
- `02_versioning_and_releases.md`: SemVer documental (`vX.Y.Z`), `doc/shared/version.tex` como fonte única e `CHANGELOG.md`.
- `03_llm_delegation_and_verification.md`: Papéis `W1–W4`, níveis de risco `R0–R3` e auditoria independente de citações.
- `04_latex_and_site_standards.md`: Padrões modulares de LaTeX (`latexmk`) e simplicidade passiva do site estático.
