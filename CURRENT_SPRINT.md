# Current sprint — revisao-graduacao-escalada / W2

Owning milestone: W2 (see [HORIZON.md](HORIZON.md))
Machine state: [PROJECT_STATE.yaml](PROJECT_STATE.yaml) (authoritative for task statuses)

## Scientific / engineering objective
Registrar quadros de referência atualizados (`references/charts/`) e padronizar governança PG-10, `HORIZON.md`, `CURRENT_SPRINT.md`, `BACKLOG.md` e UoW `CHANGELOG.md`.

## Implementation strategy
Preservar convenções modulares, slugs padronizados, paleta CUD de 9 faixas e histórico de decisões em `PROJECT_STATE.yaml`.

## Scope and non-goals
Mantém fontes modulares LaTeX (`doc/revisao_graduacao/`, `doc/guia_ufrn/`, `doc/ufrn_na_cbe/`), quadros de referência validados (`references/charts/`) e portal estático (`site/`).

## Current bounded tasks
- `T1` in `PROJECT_STATE.yaml`: Commitar quadros references/charts + fetch_reference_charts.py e alinhar governança UoW

## Independent acceptance and reproduction
- `python3 /home/lucas/Projects/scripts/uow.py check --repo revisao-graduacao-escalada`

## Blockers and owner choices
- None blocking governance alignment; see repo-owned verification commands above.

## Exact Next Step
- Concluir revisão final do Guia UFRN (`doc/guia_ufrn/`) e integrar o portal estático (`site/`) para publicação.
