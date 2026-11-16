# Regra 04: Padrões de LaTeX Modular e Site Estático

1. **LaTeX:**
   - Compilação exclusiva via `latexmk -pdf -interaction=nonstopmode -halt-on-error` com saída em `build/`.
   - Destaques visuais ("grau trabalhado" e conceitos-chave) usam macro dedicada em `doc/shared/macros.tex` com cores pastel dessaturadas semitransparentes.
   - Cada arquivo em `sections/` e `appendices/` tem responsabilidade única.
2. **Site (`site/`):**
   - HTML/CSS/JS estático puro, zero dependências pesadas de build, acessível para usuários não técnicos e de todas as idades.
   - Páginas estritamente isoladas: `index.html`, `identidade.html`, `graduacao.html`, `cbe.html`, `calculadora.html`, `referencias.html`.
