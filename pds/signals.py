import numpy as np

def time_vector(t_start, t_end, fs=1000):
    """
    Generate a uniformly sampled time vector.

    Parameters
    ----------
    t_start : float
        Initial time in seconds.
    t_end : float
        Final time in seconds.
    fs : float, optional
        Sampling frequency in Hz. Default is 1000 Hz.

    Returns
    -------
    numpy.ndarray
        Uniformly sampled time vector.
    """

    if fs <= 0:
        raise ValueError("Sampling frequency fs must be positive.")

    if t_end < t_start:
        raise ValueError("t_end must be greater than or equal to t_start.")

    n_samples = int(np.floor((t_end - t_start) * fs + 1e-12)) + 1

    return t_start + np.arange(n_samples) / fs


def sine_signal(t, A=1, f=1, phase=0):
    """
    Generate a sinusoidal signal.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    A : float, optional
        Signal amplitude. Default is 1.
    f : float, optional
        Signal frequency in Hz. Default is 1 Hz.
    phase : float, optional
        Initial phase in radians. Default is 0.

    Returns
    -------
    numpy.ndarray
        Generated sinusoidal signal.
    """

    return A * np.sin(2 * np.pi * f * t + phase)


def cosine_signal(t, A=1, f=1, phase=0):
    """
    Generate a cosine signal.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    A : float, optional
        Signal amplitude. Default is 1.
    f : float, optional
        Signal frequency in Hz. Default is 1 Hz.
    phase : float, optional
        Initial phase in radians. Default is 0.

    Returns
    -------
    numpy.ndarray
        Generated cosine signal.
    """

    return A * np.cos(2 * np.pi * f * t + phase)


def unit_step(t, A=1):
    """
    Generate a unit step signal.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    A : float, optional
        Step amplitude. Default is 1.

    Returns
    -------
    numpy.ndarray
        Generated unit step signal.
    """

    return A * np.where(t >= 0, 1.0, 0.0)


def exponential_signal(t, A=1, decay=1, shift=0):
    """
    Generate a causal decaying exponential signal.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    A : float, optional
        Signal amplitude. Default is 1.
    decay : float, optional
        Exponential decay constant. Default is 1.
    shift : float, optional
        Time shift in seconds. Default is 0.

    Returns
    -------
    numpy.ndarray
        Generated causal exponential signal.
    """

    tau = t - shift

    x = np.zeros_like(t, dtype=float)

    causal_region = tau >= 0

    x[causal_region] = (
        A * np.exp(-decay * tau[causal_region])
    )

    return x


def rectangular_signal(t, A=1, alpha=0, beta=1):
    """
    Generate a rectangular signal.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    A : float, optional
        Signal amplitude. Default is 1.
    alpha : float, optional
        Center of the rectangular pulse. Default is 0.
    beta : float, optional
        Total width of the rectangular pulse. Default is 1.

    Returns
    -------
    numpy.ndarray
        Generated rectangular signal.

    Raises
    ------
    ValueError
        If beta is not positive.
    """

    if beta <= 0:
        raise ValueError("Parameter beta must be positive.")

    return np.where(
        np.abs(t - alpha) <= beta / 2,
        A,
        0.0
    )


def triangular_signal(t, A=1, alpha=0, beta=2):
    """
    Generate a triangular signal.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    A : float, optional
        Peak amplitude. Default is 1.
    alpha : float, optional
        Time location of the peak. Default is 0.
    beta : float, optional
        Total base width of the triangular signal.
        Default is 2.

    Returns
    -------
    numpy.ndarray
        Generated triangular signal.

    Raises
    ------
    ValueError
        If beta is not positive.

    Notes
    -----
    The triangular signal follows the convention:

        A * tri((t - alpha) / (beta / 2))

    where alpha determines the center of the triangle
    and beta determines its total base width.
    """

    if beta <= 0:
        raise ValueError("Parameter beta must be positive.")

    a = alpha - beta / 2
    b = alpha + beta / 2

    x = np.zeros_like(t, dtype=float)

    rising_region = (t > a) & (t <= alpha)
    falling_region = (t > alpha) & (t < b)

    x[rising_region] = (
        A * (t[rising_region] - a) / (alpha - a)
    )

    x[falling_region] = (
        -A * (t[falling_region] - b) / (b - alpha)
    )

    return x


def impulse_signal(t, A=1, shift=0):
    """
    Generate a discrete numerical representation of an impulse signal.

    Parameters
    ----------
    t : numpy.ndarray
        Time vector.
    A : float, optional
        Amplitude assigned to the impulse sample. Default is 1.
    shift : float, optional
        Time location of the impulse. Default is 0.

    Returns
    -------
    numpy.ndarray
        Numerical representation of the impulse signal.

    Notes
    -----
    This function represents an impulse numerically by assigning
    amplitude A to the sample closest to the specified shift.

    This is intended for visualization and discrete signal exercises.
    It is not an exact numerical representation of the continuous
    Dirac delta distribution.
    """

    x = np.zeros_like(t, dtype=float)

    index = np.argmin(np.abs(t - shift))

    x[index] = A

    return x

