import sys
from alpha.mathlib import geometry  # find and run geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search path
# 1. current folder
# 2. folders in PYTHONPATH   separate with ; on Windows and : on Mac/Linux
# 3. standard (non-local) in sys.prefix
print(f"sys.prefix: {sys.prefix}")
print()
for folder in sys.path:
    print(folder)

