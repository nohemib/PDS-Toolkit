def amplitude_scale(x, C):
    """
    Scale the amplitude of a signal by a constant.

    Parameters
    ----------
    x : numpy.ndarray
        Input signal.
    C : float
        Scaling constant.

    Returns
    -------
    numpy.ndarray
        Amplitude-scaled signal.
    """

    return C * x


def add_constant(x, C):
    """
    Add a constant value to a signal.

    Parameters
    ----------
    x : numpy.ndarray
        Input signal.
    C : float
        Constant added to the signal.

    Returns
    -------
    numpy.ndarray
        Vertically shifted signal.
    """

    return x + C