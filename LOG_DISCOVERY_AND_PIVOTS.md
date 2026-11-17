# Log de Descobertas e Pivôs

| Data | Frente | Decisão / Descoberta | Motivo / Evidência | Impacto |
| :--- | :--- | :--- | :--- | :--- |
| 2026-11-16 | Arquitetura | Divisão do Doc 2 em `guia_ufrn` e `ufrn_na_cbe` | Single Responsibility Principle; isolar proposta institucional da operação do muro | Dois PDFs curtos e aba isolada no site |
| 2026-11-16 | Cores | Divisão da faixa Branca em `Branco-Vazado` (VB/V0) e `Branco` (V0/V1) | "Transparente" não tem contraste na parede escura nem em fundo claro | Tabela passa a 9 faixas mantendo CUD |
| 2026-11-16 | Doc 1 | Mover História para Apêndice e retornar a 3 capítulos | Fluidez de leitura e status público com apêndices autocontidos | Reestruturação na Onda 2 |
| 2026-11-16 | Infra / Mídia | Padronização de slugs `chart_NN_<nome>` + `fetch_reference_charts.py` | Evitar hashes opacos de upload e validar integridade via magic bytes/dimensões/SHA-256 | `references/charts/manifest.json` |
| 2026-11-16 | Build | `latexmk -silent` no `Makefile` | Reduzir ruído no terminal durante iterações da Onda 2 | Compilação limpa |
