"""Limpeza e normalização de textos em linguagem natural."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

import emoji
from langdetect import LangDetectException, detect  # type: ignore[import-untyped]
from unidecode import unidecode

from sa.model import Language


if TYPE_CHECKING:
    from spacy.language import Language as SpacyLanguage

PUNCTUATION_PATTERN = re.compile(r"[.,!?();:/]")
REPEATED_K_PATTERN = re.compile(r"k{2,}")
BAD_CHARACTERS = re.compile(r"[\000-\010]|[\013-\014]|[\016-\037]")


def matches_language(text: str, lang: Language = Language.PT) -> bool:
    """Verifica se o texto está em português via langdetect."""

    try:
        return detect(text).casefold() == lang.value.casefold()  # type: ignore[no-any-return]
    except LangDetectException:
        return False


def normalize_text(content: str) -> str:
    """Remove quebras de linha, emojis e caracteres ilegais."""

    texto: str = content.replace("\n", " ").strip()
    texto = str(emoji.demojize(texto))
    texto = BAD_CHARACTERS.sub("", texto)

    return texto.strip().lower()


def preprocess_text(
    text: str,
    stopwords: set[str],
    nlp: "SpacyLanguage",
    allowed_pos: set[str] | None = None,
    min_token_len: int = 3,
) -> list[str]:
    """Pipeline de limpeza: remoção de pontuação, normalização, lematização e filtragem.

    Args:
        text: texto bruto a ser limpo.
        stopwords: conjunto de stopwords a serem removidas.
        nlp: modelo spaCy carregado.
        allowed_pos: conjunto de POS tags permitidas (ex: {"NOUN", "ADJ"}).
                     Se None, aceita NOUN, ADJ, VERB, ADV.
        min_token_len: comprimento mínimo do lema para ser incluído.

    Returns:
        Texto limpo com lemas filtrados.
    """

    if allowed_pos is None:
        allowed_pos = {"NOUN", "ADJ", "VERB", "ADV"}

    normalized = PUNCTUATION_PATTERN.sub(" ", unidecode(str(text)).lower())
    pre_filtered = " ".join(w for w in normalized.split() if w not in stopwords)

    doc = nlp(pre_filtered)

    tokens: list[str] = []

    for token in doc:
        lemma = token.lemma_.lower().strip()

        if REPEATED_K_PATTERN.fullmatch(lemma):
            continue

        if token.pos_ in allowed_pos and len(lemma) >= min_token_len and lemma not in stopwords:
            tokens.append(lemma)

    return tokens
