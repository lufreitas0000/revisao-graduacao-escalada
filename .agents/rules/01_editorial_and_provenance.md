# Regra 01: Rigor Editorial, Proveniência e Mitigação de Alucinações

1. **Rastreabilidade no código-fonte LaTeX:**
   - Toda `\section` numerada deve ser precedida por `% EDITORIAL QUESTION: <pergunta>` e respondê-la ao final da seção.
   - Todo parágrafo com afirmação factual, normativa ou histórica deve conter tag de fonte imediatamente acima:
     - `% SOURCE [VERIFIED_PRIMARY]: <autor/órgão, título exato, ano, p. XX / seção, URL/DOI>`
     - `% SOURCE [VERIFIED_SECONDARY]: <autor, obra, ano, p. XX, URL> (via <primária>)`
     - `% SOURCE [INTERPRETATION]: <síntese derivada de [fontes]>`
     - `% SOURCE [UNVERIFIED]: <motivo>` -> Proibido em releases públicos.
2. **Proibição de extrapolação:**
   - Nunca citar página, número ou regra com base apenas em *snippet* de busca ou memória paramétrica. Se o texto completo não foi lido, marcar `[UNVERIFIED]` ou omitir.
   - Nunca usar marcadores numéricos `[1]` ou `[cite:1]`. Usar `\cite{chave}` ligado ao `.bib` verificado ou link explícito.
3. **Vocabulário padronizado:**
   - Usar **setter** para ginásios; reservar **conquistadores** e **abertura de via** para rocha.
   - Padronizar todas as siglas de associações na primeira ocorrência e usar apenas a sigla depois (ex.: `AERN`, `CBME`, `UIAA`, `IFSC`, `IRCRA`).
