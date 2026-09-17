"""
Signal Operations Example

This example demonstrates amplitude and time transformations
using the reusable functions available in PDS Toolkit.
"""

from pds import (
    time_vector,
    triangular_signal,
    amplitude_scale,
    add_constant,
    transform_time,
    plot_overlay,
)


# ======================================================
# ORIGINAL SIGNAL
# ======================================================

t = time_vector(-5, 5, fs=20)

x = triangular_signal(
    t,
    A=1,
    alpha=0,
    beta=2
)


# ======================================================
# 1. AMPLITUDE SCALING
# y(t) = 2x(t)
# ======================================================

y_amplitude = amplitude_scale(
    x,
    C=2
)

plot_overlay(
    t,
    signals=[x, y_amplitude],
    labels=["x(t)", "2x(t)"],
    title="Amplitude Scaling"
)


# ======================================================
# 2. ADDITION OF A CONSTANT
# y(t) = x(t) + 2
# ======================================================

y_constant = add_constant(
    x,
    C=2
)

plot_overlay(
    t,
    signals=[x, y_constant],
    labels=["x(t)", "x(t) + 2"],
    title="Addition of a Constant"
)


# ======================================================
# 3. GENERAL TIME TRANSFORMATION
# y(t) = x(2t - 2)
# ======================================================

t_transformed = transform_time(
    t,
    a=2,
    b=-2
)

y_time = triangular_signal(
    t_transformed,
    A=1,
    alpha=0,
    beta=2
)

plot_overlay(
    t,
    signals=[x, y_time],
    labels=["x(t)", "x(2t - 2)"],
    title="General Time Transformation"
)
