"""Geração de gráficos de frequência de palavras."""

from __future__ import annotations

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")
"""Usa o backend 'Agg' do matplotlib para não exigir ambiente gráfico ativo (como exibição pop-up X11 e Qt) e permitir geração headless."""

DEFAULT_COLOR = "steelblue"
"""String base em tom RGB repassado colorizando preenchimento default das barras do gráfico."""

DEFAULT_FIGSIZE = (10, 6)
"""Vetores default para o tamanho predefinido Width/Height da plotagem Matplotlib."""

DEFAULT_DPI = 300
"""Contador padrão para a restrição de Dots per Inch mantendo nível profissional no print da plotagem."""


def generate_frequency_chart(
    word_counts: list[tuple[str, int]],
    output_path: Path,
    *,
    color: str = DEFAULT_COLOR,
    figsize: tuple[int, int] = DEFAULT_FIGSIZE,
    dpi: int = DEFAULT_DPI,
) -> None:
    """
    Constrói via Matplotlib um painel de barras explicitando a incidência de repetições.

    Plota no eixo X as strings em 45 graus (para não truncar visualmente dependendo do width fornecido)
    e o acumulado de frequências absolutas da variável no eixo Y.
    Efetua a execução direta pro buffer gráfico fechando o plot instanciado
    (`fig.savefig`, `plt.close`) impedindo que vazamentos de ram no matplotlib ocorram nas iterações loop.

    Args:
        word_counts (list[tuple[str, int]]): Matriz tabular com as listas de arrays de tupla indicando o String Limpo e seu Score numerico de frequência descendente.
        output_path (Path): Objeto representativo de apontamento que ampara caminhos dinâmicos no host contendo a nomenclatura PNG gravada explicitamente.
        color (str, optional): A cor de exibição visual Matplotlib adotada.
        figsize (tuple[int, int], optional): Limites dimensionais do quadro em Inches.
        dpi (int, optional): Qualidade gráfica base limitante em exportação.

    Observações:
        - O layout (tight_layout) atua de modo dinâmico recalculando grids automaticamente baseados na colisão textual limitante inferior ao rotacionar a string 45 graus.
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
