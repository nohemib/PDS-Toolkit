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
    save_path=None,
    plot_type="line",
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
     plot_type : str, optional
        Plot representation. Available options are
        "line" and "stem". Default is "line".

    Returns
    -------
    None
    """

    plt.figure(figsize=(10, 5))

    if plot_type == "line":

        plt.plot(
            t,
            x,
            marker=marker,
            markersize=markersize,
            linewidth=linewidth
        )

    elif plot_type == "stem":

        plt.stem(
            t,
            x,
            linefmt="-",
            markerfmt="o",
            basefmt=" "
        )

    else:
        raise ValueError(
            "plot_type must be 'line' or 'stem'."
        )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.grid(grid)

    plt.minorticks_on()

    plt.grid(
        True,
        which="major",
        alpha=0.6
    )

    plt.grid(
        True,
        which="minor",
        alpha=0.2
    )

    if xlim is not None:
        plt.xlim(xlim)

    if ylim is not None:
        plt.ylim(ylim)

    if save_path is not None:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    fig = plt.gcf()
    ax = plt.gca()

    plt.show()

    return fig, ax