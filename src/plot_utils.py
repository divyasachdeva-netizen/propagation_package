import matplotlib.pyplot as plt

def plot_spectrum(E, F, xlabel="Energy (eV)", ylabel="Flux"):
    plt.loglog(E, F)
    plt.grid(True, ls="--", alpha=0.4)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
