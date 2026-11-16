# Regra 02: Versionamento Semântico Documental e Releases

1. **Fonte única de versão:** `doc/shared/version.tex` define `\newcommand{\docversion}{v3.0.0}` e `\newcommand{\docdate}{...}`. Nenhum documento declara versão manualmente.
2. **SemVer para documentos:**
   - `MAJOR`: Mudança estrutural de capítulos, divisão de documentos ou mudança da escala de cores.
   - `MINOR`: Novo apêndice, seção completa, gráfico ou página web.
   - `PATCH`: Correção de *typos*, ajustes de tradução ou diagramação.
3. **Congelamento:** Toda entrega fechada exige atualização de `CHANGELOG.md`, commit limpo e tag Git anotada (`git tag -a vX.Y.Z -m "..."`).
