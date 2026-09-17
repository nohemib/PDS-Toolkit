"""
Plotting Examples

This example demonstrates the main visualization tools
available in PDS Toolkit.
"""

from pds import (
    time_vector,
    triangular_signal,
    transform_time,
    plot_signal,
    plot_overlay,
    plot_comparison,
)


# ======================================================
# SIGNAL GENERATION
# ======================================================

t = time_vector(-4, 4, fs=20)

x = triangular_signal(
    t,
    A=1,
    alpha=0,
    beta=2
)

t_transformed = transform_time(
    t,
    a=1,
    b=-2
)

y = triangular_signal(
    t_transformed,
    A=1,
    alpha=0,
    beta=2
)


# ======================================================
# 1. INDIVIDUAL PLOT
# ======================================================

plot_signal(
    t,
    x,
    title="Individual Signal"
)


# ======================================================
# 2. OVERLAID SIGNALS
# ======================================================

plot_overlay(
    t,
    signals=[x, y],
    labels=["x(t)", "x(t - 2)"],
    title="Overlaid Signal Comparison"
)


# ======================================================
# 3. SIDE-BY-SIDE COMPARISON
# ======================================================

plot_comparison(
    t,
    x,
    y,
    title_1="Original Signal: x(t)",
    title_2="Transformed Signal: x(t - 2)"
)