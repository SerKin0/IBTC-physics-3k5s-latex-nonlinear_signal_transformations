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


x = [150.0, 151.0, 152.0, 153.0, 154.0, 155.0, 156.0, 157.0, 158.0, 159.0, 160.0, 161.0, 162.0, 163.0, 164.0, 165.0, 166.0, 167.0, 168.0, 169.0, 170.0, 171.0, 172.0, 173.0, 174.0, 175.0, 176.0, 177.0, 178.0, 179.0, 179.1, 179.2, 179.3, 179.4, 179.5, 179.6, 179.7, 179.8, 179.9, 180.0, 180.1, 180.2, 180.3, 180.4, 180.5, 180.6, 180.7, 180.8, 180.9, 181.0, 182.0, 183.0, 184.0, 185.0, 186.0, 187.0, 188.0, 189.0, 190.0, 191.0, 192.0, 193.0, 194.0, 195.0, 196.0, 197.0, 198.0, 199.0, 200.0, 201.0, 202.0, 203.0, 204.0, 205.0, 206.0, 207.0, 208.0, 209.0, 210.0]
y = [140.0, 160.0, 160.0, 160.0, 160.0, 160.0, 160.0, 180.0, 180.0, 180.0, 180.0, 180.0, 180.0, 200.0, 200.0, 220.0, 220.0, 240.0, 260.0, 260.0, 280.0, 300.0, 320.0, 340.0, 380.0, 400.0, 460.0, 500.0, 580.0, 640.0, 640.0, 640.0, 640.0, 660.0, 660.0, 660.0, 660.0, 660.0, 640.0, 60.0, 640.0, 660.0, 640.0, 640.0, 640.0, 640.0, 640.0, 640.0, 640.0, 640.0, 580.0, 520.0, 440.0, 400.0, 380.0, 340.0, 300.0, 280.0, 260.0, 240.0, 240.0, 220.0, 220.0, 220.0, 200.0, 180.0, 180.0, 180.0, 180.0, 160.0, 160.0, 140.0, 140.0, 140.0, 140.0, 140.0, 140.0, 140.0, 120.0]


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
    draw_graph(file_name="graph_1", size=(12, 5))
