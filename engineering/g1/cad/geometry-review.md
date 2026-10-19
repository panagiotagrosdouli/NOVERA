# CAD V1 — floor-contact and mass placement review

**Status:** preliminary point-mass/schematic analysis. This is not a production CAD assembly or measured center of gravity.

## Proposed ground-contact layout (XY, millimetres)
- Left/right powered wheel contacts: **(-191, 0)** and **(+191, 0)**.
- Front/rear idealized caster contacts: **(0, -173)** and **(0, +173)**.
- Z=0 represents the nominal level floor.
- Wheel radius is **76 mm**; wheel centers are set at **Z=76** (previous model had Z=86, leaving an unintended 10 mm gap).
- Schematic caster spheres have radius **35 mm**, centers at **Z=35**.

In this simplified geometry the convex hull of the four nominal contact points is a diamond, not a square. Real caster offset, swivel position, compliance and changing wheel loading can modify or shrink this polygon. Accordingly, the support geometry **cannot yet establish real tipping or braking limits**.

## Indicative estimated mass properties

From `mass-components.csv`, the six *assumed* component point masses sum to **36 kg**. `check_geometry.py` calculates the hypothetical 3D CG and a basic static inclusion check.

```bash
python3 engineering/g1/cad/check_geometry.py
```

The expected approximate result is **CG (0, -8.75, 433.9) mm**. These coordinates come from a manually estimated placement table, **not from solid-model densities or verified hardware**. The lateral/longitudinal result is sensitive to mass positioning, especially battery placement.

## Dimensioned design envelope (mm)

| View | Nominal dimensions | Constraints to investigate |
|---|---|---|
| Front | maximum width 500; height 1050 | Wheel protrusion, accessible display, tip margins |
| Side | maximum depth 500; height 1050 | Turning/doorway clearance, contact patch, braking pitch |
| Top | maximum 500 × 500 | Sensor field of view, collision footprint, charger access |

The file `envelope-views.svg` illustrates orthographic bounding envelopes and major dimensions. It is **not a tolerance-controlled technical drawing**.

## Before any physical prototype

Model mechanical fasteners, shell thickness, real wheel bearings and casters; then calculate solid-model mass properties and worst-case load cases. Validate power-off stops and real support contacts with a responsible robotics engineer.
