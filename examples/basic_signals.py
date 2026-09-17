from pds.signals import (
    time_vector,
    rectangular_signal,
    triangular_signal
)

from pds.plotting import plot_signal


# ======================================================
# TIME VECTOR
# ======================================================

t = time_vector(-5, 3, fs=20)


# ======================================================
# RECTANGULAR SIGNAL
# ======================================================

x_rect = rectangular_signal(
    t,
    A=1,
    alpha=-1,
    beta=3
)


# ======================================================
# TRIANGULAR SIGNAL
# ======================================================

x_tri = triangular_signal(
    t,
    A=1,
    alpha=-2,
    beta=4
)


# ======================================================
# PLOTS
# ======================================================

plot_signal(
    t,
    x_rect,
    title="Rectangular Signal",
    ylabel="Amplitude"
)

plot_signal(
    t,
    x_tri,
    title="Triangular Signal",
    ylabel="Amplitude"
)

