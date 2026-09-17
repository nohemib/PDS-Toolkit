from pds.signals import (
    time_vector,
    impulse_signal
)

from pds.plotting import plot_signal


# ======================================================
# TIME VECTOR
# ======================================================

t = time_vector(-1, 1, fs=10)


# ======================================================
# IMPULSE SIGNAL
# ======================================================

x_impulse = impulse_signal(
    t,
    A=1,
    shift=0.5
)


# ======================================================
# PLOT
# ======================================================

plot_signal(
    t,
    x_impulse,
    title="Unit Impulse Signal",
    ylabel="Amplitude",
    plot_type="stem"
)

