"""Script de geração de nuvens de palavras e gráficos de frequência."""

from __future__ import annotations

from collections import Counter
from sys import argv, exit
from typing import NoReturn

import spacy

from sa.file import XLSXColumnReader
from sa.logger import create_logger
from sa.nlp import build_stopwords, preprocess_text
from sa.parser import parse_wordcloud_args
from sa.visualization import generate_frequency_chart, generate_wordcloud

COLORMAPS: dict[str, str] = {
    "positivo": "viridis",
    "negativo": "plasma",
    "neutro": "magma",
}

BAR_COLORS: dict[str, str] = {
    "positivo": "seagreen",
    "negativo": "indianred",
    "neutro": "mediumpurple",
}

logger = create_logger(__name__)


def main() -> None:
    """Ponto de entrada principal do script de geração de nuvens de palavras."""

    args = parse_wordcloud_args(argv[1:])

    input_path = args.input_path.resolve()
    output_dir = args.output_dir.resolve()

    if not input_path.exists():
        fatal(f"O arquivo de entrada {str(input_path)!r} não existe.")

    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Carregando modelo spaCy...")

    nlp = spacy.load("pt_core_news_lg")

    logger.info("Construindo stopwords...")

    stopwords = build_stopwords(lang="portuguese", extras_path=args.extras)

    visual_pos = {"NOUN", "ADJ"}

    for sheet in args.sheets:
        logger.info("Processando aba '%s'...", sheet)

        reader = XLSXColumnReader(input_path, sheet_name=sheet, column="texto")

        try:
            texts = reader.read()
        except KeyError:
            logger.warning("Aba '%s' não possui coluna 'texto'. Pulando.", sheet)
            continue

        cleaned_texts = [preprocess_text(t, stopwords, nlp, allowed_pos=visual_pos) for t in texts]
        combined = " ".join(" ".join(t) for t in cleaned_texts)

        if not combined.strip():
            logger.warning("Nenhum texto restante após limpeza na aba '%s'. Pulando.", sheet)

            continue

        word_counts = Counter(combined.split()).most_common(args.top_n)

        colormap = COLORMAPS.get(sheet, "viridis")
        bar_color = BAR_COLORS.get(sheet, "steelblue")

        wc_path = output_dir / f"nuvem_{sheet}.png"

        generate_wordcloud(combined, wc_path, colormap=colormap)

        logger.info("Nuvem de palavras salva em %s", wc_path)

        chart_path = output_dir / f"frequencia_{sheet}.png"

        generate_frequency_chart(word_counts, chart_path, color=bar_color)

        logger.info("Gráfico de frequência salvo em %s", chart_path)
        logger.info("Top %d palavras para '%s':", args.top_n, sheet)

        for word, freq in word_counts:
            logger.info("  %-15s | %d", word, freq)

    logger.info("Processo finalizado com sucesso.")


def fatal(message: str) -> NoReturn:
    logger.fatal(message)
    exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário.")
