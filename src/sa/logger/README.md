# Módulo Clínico Observável (`logger/`)

> A interface abstrata nativa customizada estipulada para padronizar todos pontos das requisições geradas pelo terminal e da engine, unificadamente.

Este módulo não deve poluir o workflow ou exigir carga analítica de ram do núcleo NLP para gerar exibições. Agrega construtores configurados especificamente sob severidades passadas via injeção dos scripts da aplicação pai. O comportamento de negócio base consiste de dar ao pacote inteiro de coleta ou formatação Lexo "sinais de fumaça" padronizados em caso crítico ou visualizações úteis aos observadores que interagem com o sistema de longe.
