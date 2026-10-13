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

    ax.plot(x_c0, y_c0, marker="o", markersize=2, linewidth=1, color="black", zorder=1, label=r"$C = 0~\text{нФ}$")
    ax.set_xlabel(r"$U_\text{вх}, мВ$")
    ax.set_ylabel(r"$U_\text{вых}$, мВ")

    ax.plot(x_c15, y_c15, marker="o", markersize=2, linewidth=1, linestyle='--', color="black", zorder=1, label=r"$C = 15~\text{нФ}$")
    ax.set_xlabel(r"$f_\text{мод},~\text{кГц}$")
    ax.set_ylabel(r"$U_\text{вых},~\text{мВ}$")
    
    plt.legend()

    plt.savefig(f"{file_name}.pdf", format="pdf")
    plt.show()


if __name__ == "__main__":
    x_c0 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
    y_c0 = [864.0, 848.0, 864.0, 856.0, 864.0, 856.0, 864.0, 856.0, 856.0, 848.0, 864.0, 856.0, 856.0, 856.0, 856.0]
    
    x_c15 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
    y_c15 = [480.0, 464.0, 440.0, 408.0, 376.0, 344.0, 312.0, 296.0, 272.0, 256.0, 248.0, 232.0, 224.0, 216.0, 208.0]
    
    draw_graph(file_name=__file__[:-3], size=(8, 5))
