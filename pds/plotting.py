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


def plot_overlay(
    t,
    signals,
    labels=None,
    title="Signal Comparison",
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
    Plot multiple signals on the same axes.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    signals : list
        List of signals to plot.
    labels : list of str or None, optional
        Labels associated with each signal.
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
    tuple
        Matplotlib figure and axes objects.
    """

    fig, ax = plt.subplots(figsize=(10, 5))

    if labels is not None and len(labels) != len(signals):
        raise ValueError(
            "The number of labels must match the number of signals."
        )

    for i, signal in enumerate(signals):

        label = labels[i] if labels is not None else None

        ax.plot(
            t,
            signal,
            marker=marker,
            markersize=markersize,
            linewidth=linewidth,
            label=label
        )

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.minorticks_on()
    ax.grid(grid, which="major", alpha=0.6)
    ax.grid(grid, which="minor", alpha=0.2)

    if labels is not None:
        ax.legend()

    if xlim is not None:
        ax.set_xlim(xlim)

    if ylim is not None:
        ax.set_ylim(ylim)

    if save_path is not None:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()

    return fig, ax


def plot_comparison(
    t,
    x,
    y,
    title_1="Original Signal",
    title_2="Transformed Signal",
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
    Plot an original signal and a transformed signal side by side.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    x : numpy.ndarray
        Original signal.
    y : numpy.ndarray
        Transformed signal.
    title_1 : str, optional
        Title of the original signal.
    title_2 : str, optional
        Title of the transformed signal.
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
        Limits for both x-axes.
    ylim : tuple or None, optional
        Limits for both y-axes.
    save_path : str or None, optional
        Path used to save the figure.

    Returns
    -------
    tuple
        Matplotlib figure and axes objects.
    """

    fig, axes = plt.subplots(
        1,
        2,
        figsize=(12, 5),
        sharex=True,
        sharey=True
    )

    axes[0].plot(
        t,
        x,
        marker=marker,
        markersize=markersize,
        linewidth=linewidth
    )

    axes[1].plot(
        t,
        y,
        marker=marker,
        markersize=markersize,
        linewidth=linewidth
    )

    axes[0].set_title(title_1)
    axes[1].set_title(title_2)

    for ax in axes:
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        ax.minorticks_on()
        ax.grid(grid, which="major", alpha=0.6)
        ax.grid(grid, which="minor", alpha=0.2)

        if xlim is not None:
            ax.set_xlim(xlim)

        if ylim is not None:
            ax.set_ylim(ylim)

    fig.tight_layout()

    if save_path is not None:
        fig.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight"
        )

    plt.show()

    return fig, axes