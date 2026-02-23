"""Geração de nuvens de palavras."""

from __future__ import annotations

from pathlib import Path

from wordcloud import WordCloud  # type: ignore[import-untyped]

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 400
DEFAULT_COLORMAP = "viridis"
DEFAULT_BACKGROUND = "white"


def generate_wordcloud(
    text: str,
    output_path: Path,
    *,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    colormap: str = DEFAULT_COLORMAP,
    background_color: str = DEFAULT_BACKGROUND,
) -> None:
    """Gera e salva uma nuvem de palavras em formato PNG.

    Args:
        text: texto já limpo (tokens separados por espaço).
        output_path: caminho do arquivo de saída.
        width: largura da imagem em pixels.
        height: altura da imagem em pixels.
        colormap: mapa de cores matplotlib.
        background_color: cor de fundo da imagem.
    """

    wc = WordCloud(
        width=width,
        height=height,
        background_color=background_color,
        colormap=colormap,
    )

    wc.generate(text)
    wc.to_file(str(output_path))
