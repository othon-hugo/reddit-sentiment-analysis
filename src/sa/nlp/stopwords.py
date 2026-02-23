"""Carregamento e composição de stopwords."""

from __future__ import annotations

from pathlib import Path

import nltk
import spacy
from unidecode import unidecode


_NLTK_TO_SPACY: dict[str, str] = {
    "portuguese": "pt",
    "english": "en",
    "spanish": "es",
}


def load_base_stopwords(lang: str = "portuguese") -> set[str]:
    """Mescla stopwords do NLTK e spaCy para o idioma especificado.

    Args:
        lang: nome do idioma no formato NLTK (ex: 'portuguese', 'english').
    """

    nltk.download("stopwords", quiet=True)

    from nltk.corpus import stopwords as nltk_stopwords

    spacy_lang = _NLTK_TO_SPACY.get(lang, lang)
    nlp = spacy.blank(spacy_lang)
    nltk_sw: set[str] = set(nltk_stopwords.words(lang))
    spacy_sw: set[str] = nlp.Defaults.stop_words

    return nltk_sw | spacy_sw


def load_extra_stopwords(path: Path) -> set[str]:
    """Lê um CSV com coluna 'palavra' e retorna as stopwords normalizadas."""

    import pandas as pd

    df = pd.read_csv(path)
    raw: list[str] = df["palavra"].astype(str).tolist()

    return {unidecode(w).lower().strip() for w in raw}


def build_stopwords(
    lang: str = "portuguese",
    extras_path: Path | None = None,
    keep: set[str] | None = None,
) -> set[str]:
    """Compõe o conjunto final de stopwords, subtraindo as palavras que devem ser mantidas."""

    sw = load_base_stopwords(lang)

    if extras_path is not None:
        sw = sw | load_extra_stopwords(extras_path)

    if keep is not None:
        sw = sw - keep

    return sw
