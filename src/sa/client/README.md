# Camada de Comunicação Externa (`client/`)

> Este subpacote é responsável por abstrair a comunicação entre o sistema e serviços externos, encapsulando detalhes de protocolo e integração.

O módulo atua como uma camada de tradução entre as regras técnicas exigidas por APIs externas e o restante da aplicação.

Nenhuma parte subsequente do pipeline — como coletores ou processadores textuais — precisa conhecer detalhes como autenticação (ex: OAuth), configuração de headers, controle de sessão ou requisitos específicos de comunicação HTTP.

O cliente encapsula essa complexidade, realizando os handshakes necessários com as APIs externas e fornecendo uma instância de sessão configurada, autenticada e pronta para uso.

Seu papel é exclusivamente garantir conectividade e conformidade com os requisitos técnicos dos serviços integrados, sem incorporar regras de negócio ou lógica de processamento de dados.
