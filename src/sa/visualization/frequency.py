"""Geração de gráficos de frequência de palavras."""

from __future__ import annotations

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

DEFAULT_COLOR = "steelblue"
DEFAULT_FIGSIZE = (10, 6)
DEFAULT_DPI = 300


def generate_frequency_chart(
    word_counts: list[tuple[str, int]],
    output_path: Path,
    *,
    color: str = DEFAULT_COLOR,
    figsize: tuple[int, int] = DEFAULT_FIGSIZE,
    dpi: int = DEFAULT_DPI,
) -> None:
    """Gera e salva um gráfico de barras com as palavras mais frequentes.

    Args:
        word_counts: lista de tuplas (palavra, frequência), já ordenada.
        output_path: caminho do arquivo de saída.
        color: cor das barras.
        figsize: dimensões da figura (largura, altura).
        dpi: resolução da imagem.
    """

    words = [w for w, _ in word_counts]
    freqs = [f for _, f in word_counts]

    fig, ax = plt.subplots(figsize=figsize)

    ax.bar(words, freqs, color=color)
    ax.set_ylabel("Frequência")
    ax.set_xlabel("Palavra")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    fig.savefig(str(output_path), dpi=dpi)

    plt.close(fig)
