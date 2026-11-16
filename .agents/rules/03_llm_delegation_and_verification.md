# Regra 03: Estratégia Multi-Agente e Auditoria Independente

1. **Separação de papéis (`W1–W4`):**
   - `W1` (Especificação): Define estrutura, perguntas editoriais e critérios de corte (supervisor humano + planejador).
   - `W2` (Execução): Redige seções LaTeX e código HTML/JS estritamente sob o contrato do `W1`.
   - `W3` (Mecânico): Compilação `latexmk`, conversão de imagens, formatação.
   - `W4` (Árbitro/Auditor): Verifica se cada `% SOURCE` existe, se o título/ano/página batem e se há saltos lógicos ou *typos*.
2. **Níveis de risco (`R0–R3`):**
   - `R0`: Diagramação, CSS, espaçamento.
   - `R1`: Síntese de parágrafos já ancorados em fontes verificadas.
   - `R2`: Equivalência de escalas, regras da calculadora IRCRA/RIC, gráficos comparativos.
   - `R3`: Auditoria factual de normas (UIAA, World Climbing, CBME, AERN) e afirmações estatísticas/científicas. Exige revisão `W4` obrigatória antes de `main`.
