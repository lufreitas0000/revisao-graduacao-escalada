LATEXMK = latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../../build

.PHONY: all doc1 guia cbe clean

all: doc1 guia cbe

doc1:
	cd doc/revisao_graduacao && $(LATEXMK) -jobname=revisao-graduacao-escalada main.tex

guia:
	cd doc/guia_ufrn && $(LATEXMK) -jobname=guia_ufrn main.tex

cbe:
	cd doc/ufrn_na_cbe && $(LATEXMK) -jobname=ufrn_na_cbe main.tex

clean:
	rm -rf build/*
