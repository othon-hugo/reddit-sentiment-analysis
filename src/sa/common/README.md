# Contratos Transversais (`common/`)

> O ecossistema que rege a padronização no qual o polimorfismo do nosso processador baseia a interoperabilidade da I/O (entada e saída dos fluxos via interfaces estritas).

O módulo atua somente definindo as classes abstratas necessárias para garantir um contrato entre as implementações. Ele não executa o código, mas define os seus comportamentos base, orientando que as implementações apenas assinem dependência via generic types.
