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

Para o gerador de nuvens de palavras, baixe o modelo spaCy:

```bash
python3 -m spacy download pt_core_news_lg
```

## Uso

### Coletar posts do Reddit

```bash
cp .env.example .env   # preencha com suas credenciais da API do Reddit
python3 script/reddit.py -s conversas desabafos -l pt -t 1000 -o dados.xlsx -f xlsx
```

| Flag                  | Descrição                          | Default       |
| --------------------- | ---------------------------------- | ------------- |
| `-s` / `--subreddits` | Subreddit(s) alvo                  | `conversas`   |
| `-l` / `--language`   | Idioma dos posts (`pt`, `en`)      | `pt`          |
| `-t` / `--total`      | Total de posts por palavra         | `50000`       |
| `-o` / `--output`     | Caminho de saída do arquivo        | _obrigatório_ |
| `-f` / `--format`     | Formato do arquivo (`csv`, `xlsx`) | `xlsx`        |

### Converter arquivos

```bash
python3 script/convert.py -i dados.xlsx -o dados.csv -if xlsx -of csv
```

| Flag                      | Descrição                          |
| ------------------------- | ---------------------------------- |
| `-i` / `--input-path`     | Caminho do arquivo de entrada      |
| `-o` / `--output-path`    | Caminho do arquivo de saída        |
| `-if` / `--input-format`  | Formato de entrada (`csv`, `xlsx`) |
| `-of` / `--output-format` | Formato de saída (`csv`, `xlsx`)   |

### Gerar nuvens de palavras

```bash
python3 script/wc.py -i posts.xlsx -o resultados/ -s positivo negativo neutro -n 20
```

| Flag                  | Descrição                           | Default                    |
| --------------------- | ----------------------------------- | -------------------------- |
| `-i` / `--input-path` | Arquivo de entrada (Excel)          | _obrigatório_              |
| `-o` / `--output-dir` | Diretório de saída para imagens     | _obrigatório_              |
| `-s` / `--sheets`     | Abas do Excel a processar           | `positivo negativo neutro` |
| `-n` / `--top-n`      | Top N palavras no gráfico de barras | `20`                       |
| `-e` / `--extras`     | CSV de stopwords extras             | —                          |

## Estrutura

```text
src/sa/
├── analysis/       # pré-processamento de texto e empacotamento de posts
├── client/         # cliente da API do Reddit
├── collector/      # coleta de dados via API do Reddit
├── common/         # interfaces e abstrações compartilhadas
├── file/           # exportação e conversão entre formatos (CSV, XLSX)
├── logger/         # configuração de logging
├── nlp/            # stopwords e limpeza de texto (spaCy/NLTK)
├── parser/         # parsers de argumentos CLI
└── visualization/  # nuvens de palavras e gráficos de frequência

script/
├── reddit.py       # script de coleta de posts
├── convert.py      # script de conversão de arquivos
└── wc.py           # script de geração de nuvens de palavras
```
