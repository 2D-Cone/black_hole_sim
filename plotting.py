import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def plot_trajectory(data):
    fig, ax = plt.subplots()

    ax.plot(data["x"], data["y"], label="particle trajectory")
    ax.plot(0, 0, "ko", markersize=8, label="black hole")

    horizon = Circle((0, 0), data["horizon_r"], color="black", alpha=0.3)
    ax.add_patch(horizon)

    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Black Hole Orbit Sim")
    ax.grid(True)
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
    plt.tight_layout()


def plot_diagnostics(data):
    plt.figure()
    plt.plot(data["time"], data["energy"])
    plt.xlabel("time")
    plt.ylabel("total energy")
    plt.title("Energy vs Time")
    plt.grid(True)

    plt.figure()
    plt.plot(data["time"], data["L"])
    plt.xlabel("time")
    plt.ylabel("angular momentum")
    plt.title("Angular Momentum vs Time")
    plt.grid(True)

    plt.show()