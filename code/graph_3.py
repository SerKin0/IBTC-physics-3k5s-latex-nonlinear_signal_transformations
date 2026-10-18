import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


def apply_rcparams(size: tuple[float, float]):
    plt.rcParams.update(
        {
            "font.family": "CMU Serif",
            "font.size": 12,
            "mathtext.fontset": "cm",
            "axes.linewidth": 0.8,
            "axes.grid": True,
            "grid.linewidth": 0.4,
            "grid.alpha": 0.5,
            "xtick.direction": "in",
            "ytick.direction": "in",
            "xtick.minor.visible": True,
            "ytick.minor.visible": True,
            "xtick.major.width": 0.8,
            "ytick.major.width": 0.8,
            "xtick.minor.width": 0.4,
            "ytick.minor.width": 0.4,
            "figure.figsize": size,
            "figure.dpi": 150,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        }
    )


def set_settings(ax):
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.grid(which="major", linewidth=0.5, alpha=0.65)
    ax.grid(which="minor", linewidth=0.25, alpha=0.4)
    ax.tick_params(which="both", top=True, right=True)
    return ax


def draw_graph(file_name: str = "graph", size: tuple = (8, 10)):
    apply_rcparams(size)
    fig, ax = plt.subplots()
    set_settings(ax)

    ax.plot(x, y, marker="o", markersize=2, linewidth=1, color="black", zorder=1)
    ax.set_xlabel(r"$U_\text{вх}$, мВ")
    ax.set_ylabel(r"$U_\text{вых}$, мВ")

    plt.savefig(f"{file_name}.pdf", format="pdf")
    plt.show()


if __name__ == "__main__":
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    y = [10.0, 33.0, 63.0, 97.0, 130.0, 165.0, 202.0, 238.0, 275.0, 312.0, 349.0, 386.0, 426.0, 465.0, 502.0, 540.0, 579.0, 616.0, 655.0, 693.0]
    x = [i * 1000 for i in x]
    draw_graph(file_name=__file__[:-3], size=(8, 5))
