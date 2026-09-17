from pds.signals import (
    time_vector,
    sine_signal,
    cosine_signal,
    unit_step,
    exponential_signal
)

from pds.plotting import plot_signal

# ======================================================
# TIME VECTOR
# ======================================================

t = time_vector(-0.05, 0.20, fs=1000)

# ======================================================
# SIGNALS
# ======================================================

x_sine = sine_signal(
    t,
    A=1,
    f=50
)

x_cos = cosine_signal(
    t,
    A=1,
    f=50
)

x_step = unit_step(
    t,
    A=3
)

x_exp = exponential_signal(
    t,
    A=2,
    decay=3,
    shift=0
)

# ======================================================
# PLOTS
# ======================================================

plot_signal(
    t,
    x_sine,
    title="50 Hz Sinusoidal Signal",
    ylabel="Amplitude [V]"
)

plot_signal(
    t,
    x_cos,
    title="50 Hz Cosine Signal",
    ylabel="Amplitude [V]"
)

plot_signal(
    t,
    x_step,
    title="Unit Step Signal",
    ylabel="Amplitude"
)

plot_signal(
    t,
    x_exp,
    title="Causal Exponential Signal",
    ylabel="Amplitude"
)

