# Reddit Sentiment Analysis

Coleta e análise de sentimentos em posts do Reddit.

## Instalação

```bash
pip install -e .
```

Para incluir as ferramentas de desenvolvimento:

```bash
pip install -e ".[dev]"
```

## Uso

```bash
cp .env.example .env   # preencha com suas credenciais da API do Reddit
python APIReddit.py
```

## Estrutura

```text
src/sa/
├── analysis/    # pré-processamento de texto e empacotamento de posts
├── collector/   # coleta de dados via API do Reddit
└── storage/     # exportação para Excel e CSV
```
