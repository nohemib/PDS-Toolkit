"""
PDS Toolkit

Reusable tools for Digital Signal Processing exercises,
signal generation, transformations, and visualization.
"""

from .signals import (
    time_vector,
    sine_signal,
    cosine_signal,
    unit_step,
    exponential_signal,
    rectangular_signal,
    triangular_signal,
    impulse_signal,
)

from .operations import (
    amplitude_scale,
    add_constant,
    time_shift,
    time_scale,
    time_fold,
    transform_time,
)

from .plotting import (
    plot_signal,
    plot_overlay,
    plot_comparison,
)


__all__ = [
    # Signal generation
    "time_vector",
    "sine_signal",
    "cosine_signal",
    "unit_step",
    "exponential_signal",
    "rectangular_signal",
    "triangular_signal",
    "impulse_signal",

    # Signal operations
    "amplitude_scale",
    "add_constant",
    "time_shift",
    "time_scale",
    "time_fold",
    "transform_time",

    # Visualization
    "plot_signal",
    "plot_overlay",
    "plot_comparison",
]
