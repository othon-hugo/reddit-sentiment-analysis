# Estruturas Tipadas e de Domínio (`model/`)

> Espaço que dita a estrita rigidez sobre como se moldam todas entidades da nossa inteligência.

Este módudo não interage de modo logico na avaliação de sentimento direta nem abre diretórios externos. O que é cobrado dessa estrutura, se baseia fielmente em prover estabilidade baseada em restrições imutáveis ("Enums, TypedDicts"). Age prevenindo que as matrizes injetadas do Scrapping ou processadas pela NLPs trafeguem dados impuros formatáveis e sem identificações únicas que geram gargalo. Eles se solidificam, fornecendo uma espinha dorsal de atributos amarrada na infra que qualquer biblioteca de parser a frente deva obedecer sem duvidar os tipos internos que são processados O(1) pelas views.
