"""Parser de argumentos CLI para conversão de arquivos."""

from __future__ import annotations

import argparse
from pathlib import Path

from sa.file import FileFormat

DEFAULT_INPUT_FORMAT = FileFormat.CSV
DEFAULT_OUTPUT_FORMAT = FileFormat.XLSX


class ConverterParser(argparse.ArgumentParser):
    """Parser para conversão de arquivos"""


class ConverterParserNamespace(argparse.Namespace):
    """Tipagem explícita dos atributos retornados pelo parser."""

    input_format: FileFormat
    output_format: FileFormat
    input_path: Path
    output_path: Path


def create_conveter_parser() -> ConverterParser:
    """Cria e configura o parser de argumentos para conversão de arquivos."""

    parser = ConverterParser(
        prog="sa-converter",
        description="Converte arquivos entre formatos suportados pela SA.",
    )

    parser.add_argument(
        "-i",
        "--input-path",
        type=Path,
        required=True,
        help="Caminho do arquivo de entrada a ser convertido.",
    )

    parser.add_argument(
        "-o",
        "--output-path",
        type=Path,
        required=True,
        help="Caminho do arquivo de saída após a conversão.",
    )

    parser.add_argument(
        "-if",
        "--input-format",
        type=FileFormat,
        choices=[fmt for fmt in FileFormat],
        required=True,
        help=f"Formato do arquivo de entrada.",
    )

    parser.add_argument(
        "-of",
        "--output-format",
        type=FileFormat,
        choices=[fmt for fmt in FileFormat],
        required=True,
        help=f"Formato do arquivo de saída.",
    )

    return parser


def parse_converter_args(argv: list[str] | None = None) -> ConverterParserNamespace:
    """Parseia os argumentos da linha de comando e retorna um namespace tipado."""

    parser = create_conveter_parser()

    return parser.parse_args(argv, namespace=ConverterParserNamespace())
