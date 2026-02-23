from abc import ABC, abstractmethod
from typing import Generic, Iterable, TypeVar

T = TypeVar("T")


class FileSaverABC(ABC, Generic[T]):
    """
    Interface abstrata para persistência de coleções de dados em arquivo.

    Define o contrato para classes responsáveis por salvar um conjunto (iterável)
    de registros em um destino de armazenamento (ex.: arquivo CSV, JSON, banco de dados).
    Segue o padrão Template Method, delegando a implementação da lógica de
    persistência às subclasses concretas.

    Attributes:
        T: Tipo genérico dos elementos da coleção a ser persistida.

    Observações:
        - Padrão utilizado: Template Method + Strategy (via ABC genérica).
        - Implementações concretas devem definir o formato e o destino de escrita.
    """

    @abstractmethod
    def save(self, values: Iterable[T]) -> None:
        """
        Persiste uma coleção de valores no destino de armazenamento.

        Args:
            values (Iterable[T]): Coleção iterável de registros a serem salvos.
                O tipo concreto de cada elemento é definido pelo parâmetro
                genérico `T` da subclasse.

        Observações:
            - A implementação concreta é responsável por definir o formato
              de serialização e o destino de escrita (arquivo, banco, etc.).
        """


class FileReaderABC(ABC, Generic[T]):
    """
    Interface abstrata para leitura de dados a partir de uma fonte de armazenamento.

    Define o contrato para classes responsáveis por carregar dados de uma fonte
    (ex.: arquivo CSV, JSON) e retorná-los em um formato tipado. Segue o padrão
    Template Method, delegando a lógica de leitura e desserialização às subclasses.

    Attributes:
        T: Tipo genérico do dado retornado pela operação de leitura.

    Observações:
        - Padrão utilizado: Template Method + Strategy (via ABC genérica).
        - Implementações concretas devem definir a fonte e o formato de leitura.
    """

    @abstractmethod
    def read(self) -> T:
        """
        Lê e retorna os dados da fonte de armazenamento.

        Returns:
            T: Dados lidos e desserializados da fonte, no tipo definido pelo
                parâmetro genérico `T` da subclasse.

        Observações:
            - A implementação concreta é responsável por abrir a fonte,
              desserializar o conteúdo e retorná-lo no formato esperado.
        """


class FileWriterABC(ABC, Generic[T]):
    """
    Interface abstrata para escrita de um único valor em um destino de armazenamento.

    Define o contrato para classes responsáveis por serializar e gravar um único
    objeto tipado em um destino (ex.: arquivo de texto, JSON). Difere de
    `FileSaverABC` por operar sobre um valor singular em vez de uma coleção.

    Attributes:
        T: Tipo genérico do valor a ser escrito.

    Observações:
        - Padrão utilizado: Template Method + Strategy (via ABC genérica).
        - Implementações concretas devem definir o formato de serialização
          e o destino de escrita.
    """

    @abstractmethod
    def write(self, value: T) -> None:
        """
        Serializa e grava um único valor no destino de armazenamento.

        Args:
            value (T): Objeto a ser serializado e gravado, cujo tipo é
                definido pelo parâmetro genérico `T` da subclasse.

        Observações:
            - A implementação concreta é responsável por abrir o destino,
              serializar o valor e garantir o fechamento adequado do recurso.
        """


class FileConverterABC(ABC):
    """
    Interface abstrata para conversão de arquivos entre formatos distintos.

    Define o contrato para classes responsáveis por transformar um arquivo
    de um formato de entrada em um formato de saída (ex.: CSV para JSON,
    TSV para CSV). Não utiliza genéricos, pois opera sobre caminhos de arquivo
    em vez de objetos tipados em memória.

    Observações:
        - Padrão utilizado: Template Method + Strategy (via ABC).
        - Implementações concretas devem definir os formatos de entrada e saída
          suportados e a lógica de transformação.
    """

    @abstractmethod
    def convert(self, input_path: str, output_path: str) -> None:
        """
        Converte um arquivo do formato de entrada para o formato de saída.

        Args:
            input_path (str): Caminho absoluto ou relativo para o arquivo de entrada
                a ser lido e convertido.
            output_path (str): Caminho absoluto ou relativo para o arquivo de saída
                onde o resultado da conversão será gravado.

        Observações:
            - A implementação concreta é responsável por gerenciar a abertura
              e o fechamento dos arquivos de entrada e saída.
            - Caso o arquivo de saída já exista, o comportamento (sobrescrita
              ou erro) deve ser definido pela implementação concreta.
        """
