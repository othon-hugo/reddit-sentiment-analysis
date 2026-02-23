# Executáveis CLI (`script/`)

> Este diretório comporta os pontos de entrada (entrypoints) projetados para inicializar o sistema através do terminal ou console interativo.

O propósito arquitetural absoluto desta camada é orquestrar a junção entre a interface com o usuário (CLI) e a infraestrutura subjacente do Core (`src/sa`).
Espera-se que nenhum script aqui retenha regras lógicas, processamento matemático de linguagem ou regras rígidas sobre formatação tabular.

A responsabilidade das execuções repousa puramente na:

- Capitação das diretrizes pelo usuário ("flags" como _--total_, _--idioma_).
- Inicialização dos conectores autênticos do fluxo (carregar `.env`, APIs, NLP).
- Tratamentos superficiais dos encerramentos ou interrupções.
- Delegação do processamento ao respectivo construtor interno.
