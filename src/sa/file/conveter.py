from enum import Enum

import pandas as pd

from sa.common import FileConverterABC


class FileFormat(Enum):
    CSV = "csv"
    XLSX = "xlsx"


class _CSV_XLSXConverter(FileConverterABC):
    def convert(self, input_path: str, output_path: str) -> None:
        df = pd.read_csv(input_path)
        df.to_excel(output_path, index=False)


class _XLSX_CSVConverter(FileConverterABC):
    def convert(self, input_path: str, output_path: str) -> None:
        df = pd.read_excel(input_path)
        df.to_csv(output_path, index=False)


class ConverterFactory:
    _converters: dict[tuple[FileFormat, FileFormat], type[FileConverterABC]] = {
        (FileFormat.CSV, FileFormat.XLSX): _CSV_XLSXConverter,
        (FileFormat.XLSX, FileFormat.CSV): _XLSX_CSVConverter,
    }

    @classmethod
    def get_converter(cls, in_fmt: FileFormat, out_fmt: FileFormat) -> FileConverterABC:
        if in_fmt == out_fmt:
            raise ValueError("Formato de entrada e saída são iguais. Nenhuma conversão necessária.")

        Converter = cls._converters.get((in_fmt, out_fmt))

        if not Converter:
            raise ValueError(f"Conversão de {in_fmt} para {out_fmt} não suportada.")

        return Converter()
