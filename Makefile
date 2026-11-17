LATEXMK = latexmk -pdf -silent -interaction=nonstopmode -halt-on-error -outdir=../../build

.PHONY: all doc1 guia cbe charts clean

all: doc1 guia cbe

doc1:
	@echo "[build] Compilando revisao-graduacao-escalada.pdf..."
	@cd doc/revisao_graduacao && $(LATEXMK) -jobname=revisao-graduacao-escalada main.tex
	@echo "[ok] build/revisao-graduacao-escalada.pdf"

guia:
	@echo "[build] Compilando guia_ufrn.pdf..."
	@cd doc/guia_ufrn && $(LATEXMK) -jobname=guia_ufrn main.tex

cbe:
	@echo "[build] Compilando ufrn_na_cbe.pdf..."
	@cd doc/ufrn_na_cbe && $(LATEXMK) -jobname=ufrn_na_cbe main.tex

charts:
	@python3 scripts/fetch_reference_charts.py

clean:
	@rm -rf build/*
	@echo "[clean] build/ limpo."
