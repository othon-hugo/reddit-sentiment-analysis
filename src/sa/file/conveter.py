from sa.common import FileConverterABC

from enum import Enum
import pandas as pd


class FileFormat(Enum):
    CSV = "csv"
    XLSX = "xlsx"


class CSV_XLSXConverter(FileConverterABC):
    def convert(self, input_path: str, output_path: str) -> None:
        df = pd.read_csv(input_path)
        df.to_excel(output_path, index=False)


class XLSX_CSVConverter(FileConverterABC):
    def convert(self, input_path: str, output_path: str) -> None:
        df = pd.read_excel(input_path)
        df.to_csv(output_path, index=False)


class ConverterFactory:
    _converters: dict[tuple[FileFormat, FileFormat], type[FileConverterABC]] = {
        (FileFormat.CSV, FileFormat.XLSX): CSV_XLSXConverter,
        (FileFormat.XLSX, FileFormat.CSV): XLSX_CSVConverter,
    }

    @classmethod
    def get_converter(cls, in_fmt: FileFormat, out_fmt: FileFormat) -> FileConverterABC:
        if in_fmt == out_fmt:
            raise ValueError("Formato de entrada e saída são iguais. Nenhuma conversão necessária.")

        Converter = cls._converters.get((in_fmt, out_fmt))

        if not Converter:
            raise ValueError(f"Conversão de {in_fmt} para {out_fmt} não suportada.")

        return Converter()
