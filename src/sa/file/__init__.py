"""
Módulo de manipulação de dados e arquivos.

Fornece as implementações concretas das interfaces comuns para ler, salvar
e converter dados. Encapsula o uso de bibliotecas (como `pandas`) para
manipulação de dados e operações de I/O em formatos tabulares
(CSV, XLSX, etc.).
"""

from .conveter import ConverterFactory, FileFormat
from .csv import CSVPostSaver
from .xlsx import XLSXColumnReader, XLSXPostSaver

__all__ = [
    "ConverterFactory",
    "CSVPostSaver",
    "XLSXColumnReader",
    "XLSXPostSaver",
    "FileFormat",
]
