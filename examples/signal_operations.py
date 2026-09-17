from pds.signals import (
    time_vector,
    exponential_signal
)

from pds.operations import (
    amplitude_scale,
    transform_time
)

from pds.plotting import plot_overlay

from pds.plotting import plot_comparison


# ======================================================
# TIME VECTOR
# ======================================================

t = time_vector(-5, 5, fs=50)


# ======================================================
# ORIGINAL SIGNAL
# x4(t) = 3e^(-(t+1))u(t+1)
# ======================================================

x4 = exponential_signal(
    t,
    A=3,
    decay=1,
    shift=-1
)


# ======================================================
# TIME TRANSFORMATION
# x4(-t - 2)
# ======================================================

t_transformed = transform_time(
    t,
    a=-1,
    b=-2
)

x4_transformed = exponential_signal(
    t_transformed,
    A=3,
    decay=1,
    shift=-1
)


# ======================================================
# AMPLITUDE TRANSFORMATION
# y4(t) = -x4(-t - 2)
# ======================================================

y4 = amplitude_scale(
    x4_transformed,
    C=-1
)


# ======================================================
# PLOT
# ======================================================

plot_comparison(
    t,
    x4,
    y4,
    title_1="Original Signal: x4(t)",
    title_2="Transformed Signal: y4(t)",
    ylabel="Amplitude"
)

