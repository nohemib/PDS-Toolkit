from pds.signals import (
    time_vector,
    triangular_signal
)

from pds.operations import transform_time

from pds.plotting import plot_overlay


# ======================================================
# TIME VECTOR
# ======================================================

t = time_vector(-5, 5, fs=20)


# ======================================================
# ORIGINAL SIGNAL
# ======================================================

x = triangular_signal(
    t,
    A=1,
    alpha=1,
    beta=2
)


# ======================================================
# GENERAL TIME TRANSFORMATION
# ======================================================

t_transformed = transform_time(
    t,
    a=-2,
    b=-2
)

y = triangular_signal(
    t_transformed,
    A=1,
    alpha=1,
    beta=2
)


# ======================================================
# PLOT
# ======================================================

plot_overlay(
    t,
    signals=[x, y],
    labels=["x(t)", "x(-2t - 2)"],
    title="General Time Transformation",
    ylabel="Amplitude"
)

