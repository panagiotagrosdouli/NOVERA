# CAD V1 — Candidate B (conceptual)

Parametric **OpenSCAD source:** [novera-one-v1-b.scad](novera-one-v1-b.scad). This is a real editable 3D geometric model, **not** a dimensioned production CAD assembly or manufacturable engineering design.

## Geometry (mm)
- Maximum proposed envelope: **500 W × 500 D × 1050 H**
- Chassis: rounded 468 × 468 × 170
- Drive wheel placeholder: radius 76, thickness 42, centers at X ±191, Y 0, Z 86
- Body: 272 W × 235 D, spanning nominally Z 175–800
- Head: 325 W × 145 D × 190, spanning Z 860–1050
- Internal battery, electronics, and display shapes are packaging placeholders.

**Bounding-box warning:** Minkowski rounding and wheel geometry are visual envelope approximations. Display and other parts are not fastened; nominal Z gaps are intentional. The resulting mesh is a multi-part concept visualization, not an assembled watertight solid suitable for additive manufacture. Casters and wheel contacts are not mechanically verified.

## Local use
Install OpenSCAD and run:
```bash
openscad -o novera-one-v1-b.stl novera-one-v1-b.scad
```
STL is for inspection only, not fabrication. You can edit W, D, H and subsystem dimensions in the source; **H is currently a named target, not a derived constraint**.

## Remaining G1 work
1. Real wheel contact coordinates and stable caster geometry.
2. Physical connection design, wall thickness, service access and full collision clearance.
3. CAD material densities and measured component masses, then full 3D CG.
4. Tip, brake, speed, pinch-point and emergency-stop hazard analysis.
5. Reachability and accessible interface height assessment.

No claim of working hardware or compliance.
