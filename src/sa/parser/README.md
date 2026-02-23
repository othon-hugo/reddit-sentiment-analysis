# Analisadores CLI Estritos (`parser/`)

> Módulo unicamente acoplado à injeção segura de parametros lógicos baseando sua avaliação na interceptação dos arrays passados pelo terminal antes do runtime acontecer na infraestrutura pesada.

Ele isola totalmente as responsabilidades das `scripts/`. Tem por vocação comportamental barrar anomalias vindas dos digitamentos no shell do usuário do sistema operacional subjacente. Ao invés da lógica interagir com Strings não verificadas propícias a vazarem erros no meio da operação baseada em Memória, esse avaliador transforma e força "Namespace" engessado instanciando na injeção Enumerações e Paths limpos que a modelagem confia inteiramente ao ser instanciado e disparado nas chamadas posteriores.
