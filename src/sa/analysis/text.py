import re
from enum import Enum

import emoji
from langdetect import LangDetectException, detect  # type: ignore[import-untyped]

BAD_CHARACTERS = re.compile(r"[\000-\010]|[\013-\014]|[\016-\037]")


class Language(str, Enum):
    PT = "pt"
    EN = "en"
    ES = "es"


def preprocess_text(content: str) -> str:
    """Remove quebras de linha, emojis e caracteres ilegais."""

    texto: str = content.replace("\n", " ").strip()
    texto = str(emoji.demojize(texto))
    texto = BAD_CHARACTERS.sub("", texto)

    return texto.strip().lower()


def matches_language(text: str, lang: Language = Language.PT) -> bool:
    """Verifica se o texto está em português via langdetect."""

    try:
        return detect(text).casefold() == lang.value.casefold()  # type: ignore[no-any-return]
    except LangDetectException:
        return False
