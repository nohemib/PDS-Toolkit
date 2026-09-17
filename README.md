# PDS Toolkit

A reusable Python toolkit for Digital Signal Processing exercises, signal generation, transformations, and visualization.

This project is being developed as part of the Master's Degree in Advanced Technology at UPIITA-IPN.

The main goal of PDS Toolkit is to simplify the implementation of common signal processing exercises by separating signal generation, signal operations, and visualization into reusable Python modules.

## Features

### Signal Generation

PDS Toolkit currently supports:

- Time vector generation
- Sinusoidal signals
- Cosine signals
- Unit step signals
- Causal exponential signals
- Rectangular signals
- Triangular signals
- Numerical impulse representation

### Signal Operations

Available operations include:

- Amplitude scaling
- Addition of constants
- Time shifting
- Time scaling
- Time reversal
- General time transformations of the form:

\[
x(at+b)
\]

### Visualization

The toolkit includes reusable functions for:

- Individual signal plots
- Discrete stem plots
- Overlaid signal comparisons
- Side-by-side signal comparisons
- Figure export for reports and documentation

## Project Structure

```text
PDS-Toolkit/
├── pds/
│   ├── __init__.py
│   ├── signals.py
│   ├── operations.py
│   └── plotting.py
│
├── examples/
│   ├── basic_signals.py
│   ├── signal_operations.py
│   └── plotting_examples.py
│
├── homework/
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/nohemib/PDS-Toolkit.git
```

Move into the project directory:

```bash
cd PDS-Toolkit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

A basic sinusoidal signal can be generated and plotted with:

```python
from pds import (
    time_vector,
    sine_signal,
    plot_signal,
)

t = time_vector(0, 0.2, fs=1000)

x = sine_signal(
    t,
    A=1,
    f=50
)

plot_signal(
    t,
    x,
    title="50 Hz Sinusoidal Signal",
    ylabel="Amplitude [V]"
)
```

## Signal Transformations

General time transformations can be represented using:

```python
from pds import (
    time_vector,
    triangular_signal,
    transform_time,
    plot_comparison,
)

t = time_vector(-5, 5, fs=20)

x = triangular_signal(
    t,
    A=1,
    alpha=0,
    beta=2
)

t_transformed = transform_time(
    t,
    a=2,
    b=-2
)

y = triangular_signal(
    t_transformed,
    A=1,
    alpha=0,
    beta=2
)

plot_comparison(
    t,
    x,
    y,
    title_1="Original Signal",
    title_2="Transformed Signal"
)
```

This example represents:

\[
y(t)=x(2t-2)
\]

## Examples

The `examples/` directory contains executable examples demonstrating the main features of the toolkit.

Run them from the project root using:

```bash
python -m examples.basic_signals
```

```bash
python -m examples.signal_operations
```

```bash
python -m examples.plotting_examples
```

## Documentation

Each function includes a NumPy-style docstring describing its parameters, return values, and mathematical interpretation when applicable.

Documentation can also be inspected directly from Python:

```python
from pds import triangular_signal

help(triangular_signal)
```

## Development Status

PDS Toolkit is currently under active development.

The project is initially focused on reusable tools for Digital Signal Processing coursework and will be expanded as new signal processing concepts are implemented.

## Author

**Nohemi Barranco Alavez**

Master's Degree in Advanced Technology  
UPIITA - Instituto Politécnico Nacional

## Disclaimer

This is a personal academic software project and is not an official software package of Instituto Politécnico Nacional.