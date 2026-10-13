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

    ax.plot(x_on, y_on, marker="o", markersize=3, linewidth=1, color="black", zorder=1, label=r"Включенный детектор")
    ax.set_xlabel(r"$U_\text{вх}, мВ$")
    ax.set_ylabel(r"$U_\text{вых}$, мВ")

    ax.plot(x_off, y_off, marker="o", markersize=3, linewidth=1, linestyle='--', color="black", zorder=1, label=r"Выключенный детектор")
    ax.set_xlabel(r"$f,~\text{кГц}$")
    ax.set_ylabel(r"$U_\text{вых},~\text{мВ}$")
    
    plt.legend()

    plt.savefig(f"{file_name}.pdf", format="pdf")
    plt.show()


if __name__ == "__main__":
    x_on = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0]
    y_on = [1.56, 0.76, 1.5, 0.94, 0.6, 0.6, 0.68, 0.92, 1.44, 2.98, 2.68, 1.52, 1.0, 0.72, 0.6, 0.48, 0.4, 0.36, 0.32, 0.3, 0.26]
    
    x_off = [5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0]
    y_off = [1.6, 2.28, 2.3, 1.44, 1.52, 1.94, 2.8, 5.08, 7.24, 4.52, 2.96, 2.2, 1.8, 1.52, 1.4, 1.24, 1.08, 1.0, 0.92, 0.88, 0.84]
    
    draw_graph(file_name=__file__[:-3], size=(8, 5))
