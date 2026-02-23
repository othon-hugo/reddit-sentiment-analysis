"""Script de conversão de arquivos entre formatos suportados."""

from __future__ import annotations

from sys import argv, exit
from typing import NoReturn

from sa.file import ConverterFactory
from sa.logger import create_logger
from sa.parser import parse_converter_args

logger = create_logger(__name__)


def main() -> None:
    """Ponto de entrada principal do script de conversão."""

    args = parse_converter_args(argv[1:])

    input_path = args.input_path.resolve()
    output_path = args.output_path.resolve()

    if not input_path.exists():
        fatal(f"O arquivo de entrada {str(input_path)!r} não existe.")

    if output_path.exists():
        fatal(f"O arquivo de saída {str(output_path)!r} já existe. Por favor, escolha um caminho diferente ou remova o arquivo existente.")

    logger.info("Convertendo %s (%s) para %s (%s)...", input_path, args.input_format.value, output_path, args.output_format.value)

    converter = ConverterFactory.get_converter(args.input_format, args.output_format)
    converter.convert(str(input_path), str(output_path))

    logger.info("Conversão concluída com sucesso: %s", output_path)


def fatal(message: str) -> NoReturn:
    logger.fatal(message)
    exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nConversão interrompida pelo usuário.")
