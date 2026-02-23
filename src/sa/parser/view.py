"""Parser de argumentos CLI para geração de nuvens de palavras."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_SHEETS = ["positivo", "negativo", "neutro"]
DEFAULT_TOP_N = 20


class WordCloudParser(argparse.ArgumentParser):
    """Parser de argumentos para geração de nuvens de palavras."""


class WordCloudParserNamespace(argparse.Namespace):
    """Tipagem explícita dos atributos retornados pelo parser."""

    input_path: Path
    output_dir: Path
    sheets: list[str]
    top_n: int
    extras: Path | None


def create_wordcloud_parser() -> WordCloudParser:
    """Cria e configura o parser de argumentos para geração de nuvens de palavras."""

    parser = WordCloudParser(
        prog="sa-wordcloud",
        description="Gera nuvens de palavras e gráficos de frequência a partir de arquivos de posts.",
    )

    parser.add_argument(
        "-i",
        "--input-path",
        type=Path,
        required=True,
        help="Caminho do arquivo de entrada (Excel ou CSV).",
    )

    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        required=True,
        help="Diretório de saída para as imagens geradas.",
    )

    parser.add_argument(
        "-s",
        "--sheets",
        type=str,
        nargs="+",
        default=DEFAULT_SHEETS,
        help=f"Nomes das abas do Excel a processar (default: {' '.join(DEFAULT_SHEETS)}).",
    )

    parser.add_argument(
        "-n",
        "--top-n",
        type=int,
        default=DEFAULT_TOP_N,
        help=f"Número de palavras mais frequentes para o gráfico de barras (default: {DEFAULT_TOP_N}).",
    )

    parser.add_argument(
        "-e",
        "--extras",
        type=Path,
        default=None,
        help="Caminho para CSV de stopwords extras (coluna 'palavra').",
    )

    return parser


def parse_wordcloud_args(argv: list[str] | None = None) -> WordCloudParserNamespace:
    """Parseia os argumentos da linha de comando e retorna um namespace tipado."""

    parser = create_wordcloud_parser()

    return parser.parse_args(argv, namespace=WordCloudParserNamespace())
