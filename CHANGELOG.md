# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo. Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/) e SemVer.

## [Unreleased]

### [2026-11-18] [W2-U2] [Actor: Antigravity] — Commit updated reference charts and align Four-Record + HORIZON + UoW CHANGELOG on main
#### Ideas & Contracts Evolved
- Preserved existing Portuguese CHANGELOG entries alongside dual-section UoW feed and custom color_scale locks in PROJECT_STATE.yaml.

#### Code & Artifacts Changed
- Committed references/charts/ & scripts/fetch_reference_charts.py updates; extended PROJECT_STATE.yaml; added CURRENT_SPRINT.md, HORIZON.md, BACKLOG.md; updated README.md, CHANGELOG.md, .agents/.

### Added
- Arquitetura v3.0.0 com governança adaptada, separação em 3 documentos e diretório `site/`.
- Estrutura modular do Documento 1 (`doc/revisao_graduacao/`) em 3 capítulos, conclusão e 3 apêndices (História, IRCRA/RIC, Glossário), com macros de destaque pastel e tags `% SOURCE`.
- Script `scripts/fetch_reference_charts.py` e convenção padrão de slugs em `references/charts/`.

### Changed
- `Makefile` atualizado com flag `-silent` e alvo `make charts`.
- Tabela 3.1 atualizada para 9 faixas (`Branco-Vazado` em VB/V0 e `Branco` em V0/V1).

### Fixed
- Correção do typo `extbf` na Seção 2.2 e ajuste de largura de coluna na Tabela 3.1.
