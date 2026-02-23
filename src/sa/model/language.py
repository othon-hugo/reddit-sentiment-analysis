from enum import Enum


class Language(str, Enum):
    """
    Enumeração que define os idiomas suportados pelo sistema de NLP.

    Esta classe garante contratos rígidos na definição do idioma esperado
    na fase de coleta e pós-processamento, evitando strings soltas no código.
    Herdar paralelamente de `str` permite que seus enumeradores possam interagir
    diretamente com APIs que esperam nativamente strings convencionais, como
    modelos pré-treinados em NLP.

    Attributes:
        PT: Representa a língua Portuguesa (código ISO 639-1: "pt").
        EN: Representa a língua Inglesa (código ISO 639-1: "en").
        ES: Representa a língua Espanhola (código ISO 639-1: "es").
    """

    PT = "pt"
    EN = "en"
    ES = "es"
