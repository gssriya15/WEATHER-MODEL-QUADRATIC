# Version 1: Hardcoded values
a = 0.5
b = -3
c = 28
t = 5  # Example: 5th hour/day

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")
