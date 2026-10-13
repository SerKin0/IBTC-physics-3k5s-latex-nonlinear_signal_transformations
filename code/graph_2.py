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
    ax.set_xlabel(r"$f$, кГц")
    ax.set_ylabel(r"$U_\text{вых}$, мВ")

    plt.savefig(f"{file_name}.pdf", format="pdf")
    plt.show()


if __name__ == "__main__":
    x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 150.0, 151.0, 152.0, 153.0, 154.0, 155.0, 156.0, 157.0, 158.0, 159.0, 160.0, 161.0, 162.0, 163.0, 164.0, 165.0, 166.0, 167.0, 168.0, 169.0, 170.0, 171.0, 172.0, 173.0, 174.0, 175.0, 176.0, 177.0, 178.0, 179.0, 180.0, 181.0, 182.0, 183.0, 184.0, 185.0, 186.0, 187.0, 188.0, 189.0, 190.0, 191.0, 192.0, 193.0, 194.0, 195.0, 196.0, 197.0, 198.0, 199.0, 200.0]
    y = [0.4, 0.54, 0.68, 0.88, 1.2, 1.62, 3.1, 1.96, 1.96, 2.4, 3.14, 4.6, 7.5, 12.5, 10.6, 7.3, 5.36, 4.24, 3.52, 3.04, 2.66, 2.34, 2.14, 1.98, 1.8, 1.7, 1.6, 1.54, 1.44, 1.3, 0.72, 0.76, 0.76, 0.84, 0.84, 0.88, 0.96, 1.0, 1.08, 1.2, 1.32, 1.52, 1.76, 2.2, 3.0, 4.36, 4.4, 2.68, 1.8, 1.36, 1.08, 0.92, 0.84, 0.72, 0.6, 0.56, 0.52, 0.48, 0.4, 0.4, 0.4, 0.4, 0.42, 0.48, 0.52, 0.52, 0.6, 0.72, 0.8, 0.96, 1.08, 1.36, 1.8, 2.64, 4.4, 4.32, 2.96, 2.16, 1.72, 1.44, 1.28]
    y = [i * 100 for i in y]
    
    draw_graph(file_name=__file__[:-3], size=(12, 5))
