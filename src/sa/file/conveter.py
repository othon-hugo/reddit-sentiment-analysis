from enum import Enum

import pandas as pd

from sa.common import FileConverterABC


class FileFormat(Enum):
    """
    Enumeração que define os formatos de arquivo tabulares suportados para conversão.

    Attributes:
        CSV: Formato Comma-Separated Values ("csv").
        XLSX: Formato Microsoft Excel Open XML Spreadsheet ("xlsx").
    """

    CSV = "csv"
    XLSX = "xlsx"


class _CSV_XLSXConverter(FileConverterABC):
    """
    Estratégia concreta de conversão de CSV para XLSX.

    Carrega via `pandas` o conteúdo do arquivo CSV de origem em memória e
    o escreve no formato Excel no caminho de destino, mantendo a estrutura tabular.

    Observações:
        - O índice do DataFrame é ignorado (``index=False``) durante a escrita
          para evitar colunas duplicadas ou indesejadas na saída.
        - Não deve ser instanciada diretamente fora da `ConverterFactory`.
    """

    def convert(self, input_path: str, output_path: str) -> None:
        """
        Lê um CSV de entrada através do pandas e exporta como Excel com índice oculto.

        Args:
            input_path (str): Caminho para o arquivo CSV de origem.
            output_path (str): Caminho para o arquivo Excel destino.
        """

        df = pd.read_csv(input_path)
        df.to_excel(output_path, index=False)


class _XLSX_CSVConverter(FileConverterABC):
    """
    Estratégia concreta de conversão de XLSX para CSV.

    Carrega via `pandas` a aba principal do arquivo Excel em memória e
    o exporta no formato CSV no caminho de destino.

    Observações:
        - Apenas a primeira aba (default do `pandas`) é lida.
        - O índice do DataFrame é ignorado (``index=False``) durante a escrita.
        - Não deve ser instanciada diretamente fora da `ConverterFactory`.
    """

    def convert(self, input_path: str, output_path: str) -> None:
        """
        Lê um arquivo Excel de entrada através do pandas e exporta como CSV com índice oculto.

        Args:
            input_path (str): Caminho para o arquivo Excel de origem.
            output_path (str): Caminho para o arquivo CSV destino.
        """

        df = pd.read_excel(input_path)
        df.to_csv(output_path, index=False)


class ConverterFactory:
    """
    Fábrica responsável por instanciar conversores de arquivo mediante demanda.

    Atua como um ponto central (singleton em nível de classe) para criação
    de conversores, ocultando as classes concretas de conversão (que possuem
    escopo privado neste módulo) do resto do sistema.

    Observações:
        - Padrão utilizado: Factory Method (variante parametrizada).
        - Os conversores estão registrados no dicionário interno `_converters`
          mapeados por uma tupla ``(formato_origem, formato_destino)``.
    """

    _converters: dict[tuple[FileFormat, FileFormat], type[FileConverterABC]] = {
        (FileFormat.CSV, FileFormat.XLSX): _CSV_XLSXConverter,
        (FileFormat.XLSX, FileFormat.CSV): _XLSX_CSVConverter,
    }

    @classmethod
    def get_converter(cls, in_fmt: FileFormat, out_fmt: FileFormat) -> FileConverterABC:
        """
        Fabricante do objeto de conversão correspondente aos formatos especificados.

        Fornece uma instância concreta de `FileConverterABC` capaz de ler
        arquivos em `in_fmt` e salvar em `out_fmt`. Valida previamente se a conversão
        faz sentido lógico e se está suportada pelo registro interno.

        Args:
            in_fmt (FileFormat): Formato originário a ser convertido.
            out_fmt (FileFormat): Formato desejado como saída.

        Returns:
            FileConverterABC: Instância configurada para efetuar a conversão desejada.

        Raises:
            ValueError: Quando os formatos de entrada e saída são os mesmos, logo uma
                cópia pura deveria ser feita em outro nível de abstração.
            ValueError: Se não houver classe mapeada para processar os formatos solicitados.
        """

        if in_fmt == out_fmt:
            raise ValueError("Formato de entrada e saída são iguais. Nenhuma conversão necessária.")

        Converter = cls._converters.get((in_fmt, out_fmt))

        if not Converter:
            raise ValueError(f"Conversão de {in_fmt} para {out_fmt} não suportada.")

        return Converter()
