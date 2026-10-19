"""Reproducible envelope and estimated point-mass centroid checks. No external dependencies."""
from pathlib import Path
import csv, math
ROOT=Path(__file__).resolve().parent
rows=list(csv.DictReader((ROOT/"mass-components.csv").open()))
assert len(rows)==6
mass=sum(float(r["mass_kg"]) for r in rows)
assert abs(mass-36)<1e-9
def weighted(axis):
    return sum(float(r["mass_kg"])*float(r[axis]) for r in rows)/mass
x,y,z=(weighted(a) for a in ["x_mm","y_mm","z_mm"])
# Assumed diamond-shaped contact polygon: drive contacts (+/-191,0), casters (0,+/-173).
# Point inside the convex diamond if |x|/191 + |y|/173 <=1.
margin=1-abs(x)/191-abs(y)/173
assert margin>0
assert 0<=z<=1050
assert abs(z-433.8888888888889)<0.01
print(f"Mass estimate {mass:.1f} kg; CG=({x:.1f},{y:.1f},{z:.1f}) mm")
print(f"Nominal 2D contact polygon inclusion margin (dimensionless)={margin:.3f}")
print("PASS: conceptual arithmetic only; NOT a dynamic stability or compliance validation.")
