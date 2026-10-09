
import numpy as np
import pandas as pd
import matplotlib
import scipy

print("=" * 50)
print("ALEX MOTORSPORT ENGINEERING")
print("YEAR 1 - DAY 1")
print("=" * 50)

print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("SciPy version:", scipy.__version__)

speeds = np.array([40, 42, 45, 43, 47])

print()
print("Sample racing data")
print("Maximum speed:", speeds.max())
print("Average speed:", speeds.mean())

print()
print("Alex Motorsport Engineering environment ready.")
