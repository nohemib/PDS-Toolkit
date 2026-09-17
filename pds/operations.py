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


def time_shift(t, t0):
    """
    Generate the transformed time argument for x(t - t0).

    Parameters
    ----------
    t : numpy.ndarray
        Original time vector.
    t0 : float
        Time-shift parameter.

    Returns
    -------
    numpy.ndarray
        Transformed time argument t - t0.

    Notes
    -----
    A positive t0 produces x(t - t0), corresponding
    to a delay of the signal.

    A negative t0 produces x(t + |t0|), corresponding
    to an advance of the signal.
    """

    return t - t0


def time_scale(t, a):
    """
    Generate the transformed time argument for x(a*t).

    Parameters
    ----------
    t : numpy.ndarray
        Original time vector.
    a : float
        Time-scaling factor.

    Returns
    -------
    numpy.ndarray
        Transformed time argument a*t.

    Raises
    ------
    ValueError
        If a is zero.

    Notes
    -----
    If |a| > 1, the signal is compressed in time.

    If 0 < |a| < 1, the signal is expanded in time.

    If a < 0, the transformation also includes
    time reversal.
    """

    if a == 0:
        raise ValueError("Time-scaling factor a must be nonzero.")

    return a * t


def time_fold(t):
    """
    Generate the transformed time argument for x(-t).

    Parameters
    ----------
    t : numpy.ndarray
        Original time vector.

    Returns
    -------
    numpy.ndarray
        Time-reversed argument -t.

    Notes
    -----
    This transformation reflects the signal
    with respect to the vertical axis.
    """

    return -t

def transform_time(t, a=1, b=0):
    """
    Generate the transformed time argument for x(a*t + b).

    Parameters
    ----------
    t : numpy.ndarray
        Original time vector.
    a : float, optional
        Time-scaling factor. Default is 1.
    b : float, optional
        Time-shift term inside the signal argument.
        Default is 0.

    Returns
    -------
    numpy.ndarray
        Transformed time argument a*t + b.

    Raises
    ------
    ValueError
        If a is zero.

    Notes
    -----
    This function represents the general time transformation:

        x(a*t + b)

    The parameter a controls time scaling and possible
    time reversal, while b contributes to the time shift.
    """

    if a == 0:
        raise ValueError("Time-scaling factor a must be nonzero.")

    return a * t + b

