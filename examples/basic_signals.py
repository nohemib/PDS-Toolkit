from pds.signals import time_vector, sine_signal
from pds.plotting import plot_signal


# Generate time vector
t = time_vector(0, 0.2, fs=1000)

# Generate sinusoidal signal
x = sine_signal(t, A=1, f=50)

# Plot signal
plot_signal(
    t,
    x,
    title="50 Hz Sinusoidal Signal",
    ylabel="Amplitude [V]"
)

