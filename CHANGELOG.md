# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo. Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/) e SemVer.

## [Unreleased]

### Added
- Arquitetura v3.0.0 com governança adaptada, separação em 3 documentos e diretório `site/`.
- Estrutura modular do Documento 1 (`doc/revisao_graduacao/`) em 3 capítulos, conclusão e 3 apêndices (História, IRCRA/RIC, Glossário), com macros de destaque pastel e tags `% SOURCE`.
- Script `scripts/fetch_reference_charts.py` e convenção padrão de slugs em `references/charts/`.

### Changed
- `Makefile` atualizado com flag `-silent` e alvo `make charts`.
- Tabela 3.1 atualizada para 9 faixas (`Branco-Vazado` em VB/V0 e `Branco` em V0/V1).

### Fixed
- Correção do typo `extbf` na Seção 2.2 e ajuste de largura de coluna na Tabela 3.1.
