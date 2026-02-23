# Projeto de Iniciação Científica: Análise de Sentimentos em Redes Sociais

Este projeto consiste em um pipeline de extração, processamento e análise de textos provenientes da rede social Reddit, focado em categorizar e gerar métricas e recursos visuais sobre opiniões de usuários a respeito de tópicos pré-determinados.

A arquitetura foi pensada para ser modular, desacoplada e estrita, fornecendo forte tipagem, organização de dependências e previsibilidade desde a chamada na interface de terminal (CLI) até o momento da geração visual dos gráficos analisados.

## Executáveis CLI (Terminal/Console)

Este projeto possui scripts de entrada estruturados na pasta `script/` que operam como o ponto inicial de contato para os analistas operacionais usarem as diversas vertentes criadas sob a infraestrutura. Consultar suas instruções individuais provê uma visão ampla dos comportamentos e restrições:

- [Conversor de Extensões (`script/convert.py`)](script/convert.md)
- [Crawler de Coleta NLP (`script/reddit.py`)](script/reddit.md)
- [Renderizador Gráfico de Sentimentos (`script/view.py`)](script/view.md)
