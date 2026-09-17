from pds.signals import (
    time_vector,
    sine_signal
)

from pds.operations import (
    amplitude_scale,
    add_constant
)

from pds.plotting import plot_overlay


# ======================================================
# TIME VECTOR
# ======================================================

t = time_vector(0, 0.2, fs=200)


# ======================================================
# ORIGINAL SIGNAL
# ======================================================

x = sine_signal(
    t,
    A=2,
    f=20
)


# ======================================================
# AMPLITUDE SCALING
# ======================================================

y_positive = amplitude_scale(x, 2)

y_negative = amplitude_scale(x, -1)

y_shifted = add_constant(x, 3)

y_shifted = add_constant(x, 3)


# ======================================================
# PLOTS
# ======================================================

plot_overlay(
    t,
    signals=[x, y_positive],
    labels=["Original signal", "C = 2"],
    title="Positive Amplitude Scaling",
    ylabel="Amplitude [V]"
)

plot_overlay(
    t,
    signals=[x, y_negative],
    labels=["Original signal", "C = -1"],
    title="Negative Amplitude Scaling",
    ylabel="Amplitude [V]"
)

plot_overlay(
    t,
    signals=[x, y_shifted],
    labels=["Original signal", "C = 3"],
    title="Addition of a Constant",
    ylabel="Amplitude [V]"
)

plot_overlay(
    t,
    signals=[x, y_shifted],
    labels=["Original signal", "C = 3"],
    title="Addition of a Constant",
    ylabel="Amplitude [V]"
)