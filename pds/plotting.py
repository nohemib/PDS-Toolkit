import matplotlib.pyplot as plt


def plot_signal(
    t,
    x,
    title="Signal",
    xlabel="Time [s]",
    ylabel="Amplitude",
    marker="o",
    markersize=4,
    linewidth=1,
    grid=True,
    xlim=None,
    ylim=None,
    save_path=None
):
    """
    Plot a signal as a function of time.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    x : numpy.ndarray
        Signal values.
    title : str, optional
        Plot title.
    xlabel : str, optional
        Label for the x-axis.
    ylabel : str, optional
        Label for the y-axis.
    marker : str or None, optional
        Marker style.
    markersize : float, optional
        Marker size.
    linewidth : float, optional
        Line width.
    grid : bool, optional
        Enable or disable the grid.
    xlim : tuple or None, optional
        Limits for the x-axis.
    ylim : tuple or None, optional
        Limits for the y-axis.
    save_path : str or None, optional
        Path used to save the figure.

    Returns
    -------
    None
    """

    plt.figure(figsize=(10, 5))

    plt.plot(
        t,
        x,
        marker=marker,
        markersize=markersize,
        linewidth=linewidth
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.grid(grid)

    if xlim is not None:
        plt.xlim(xlim)

    if ylim is not None:
        plt.ylim(ylim)

    if save_path is not None:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()