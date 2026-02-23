"""Geração de nuvens de palavras."""

from __future__ import annotations

from pathlib import Path

from wordcloud import WordCloud  # type: ignore[import-untyped]

DEFAULT_WIDTH = 800
"""Limitante numérico referenciador a base default da largura gerado em pixels WC."""

DEFAULT_HEIGHT = 400
"""Limitante numérico referenciador a base default da altura do canvas gerado em pixels WC."""

DEFAULT_COLORMAP = "viridis"
"""Tabela Colorida nativa empregada como contraste default sob paletas da interface."""

DEFAULT_BACKGROUND = "white"
"""Canvas Default da string preenchação visual background da img exportada."""


def generate_wordcloud(
    text: str,
    output_path: Path,
    *,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    colormap: str = DEFAULT_COLORMAP,
    background_color: str = DEFAULT_BACKGROUND,
) -> None:
    """
    Constrói estruturalmente a projeção (Lexical Tag Cloud/WordCloud) via interface empacotadora externa.

    Orquestra as lógicas e matrizes configuradas (Colormaps e Backgrounds) instanciando
    a classe principal de computação da Engine `WordCloud`. Essa base iterará massivamente em cima
    do formato em texto cru corrido alocando em tamanho de fonte superior o que for majoritário e menor
    o que for secundário. No fim o transborda de memórias pros bytes do filesystem explicitamente.

    Args:
        text (str): Grande texto base iterável limpo unificado e distanciado unicamente de espaços e não arrays em lista.
        output_path (Path): Path seguro estipulado da emissão em PNG para salvamento disco na infra.
        width (int, optional): Ocupação canvas lateral configurada a lib de plotagem Wordcloud.
        height (int, optional): Ocupação canvas vertical em base configurada sobre a classe instanciadora lib.
        colormap (str, optional): A palheta estipulada matplotlib validada com cores mapeadas aceitas.
        background_color (str, optional): Backfill inferior limpo para render de contraste base.
    """

    wc = WordCloud(
        width=width,
        height=height,
        background_color=background_color,
        colormap=colormap,
    )

    wc.generate(text)
    wc.to_file(str(output_path))
