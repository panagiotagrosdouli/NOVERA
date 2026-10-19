# First-pass mass and stability analysis

Candidate **B** with a 36 kg target. The table represents a *hypothetical allocation* with estimated component heights, not a measured mass distribution.

| Group | Estimated mass (kg) | Assumed center height above floor (m) |
|---|---:|---:|
| Battery, protected power and enclosure | 9 | 0.18 |
| Drive system, wheels, caster and controller | 8 | 0.16 |
| Frame, shells and mounts | 7 | 0.52 |
| Computer, sensors and cabling | 4 | 0.72 |
| Screen, head and interface | 5 | 0.91 |
| Mechanical/design reserve | 3 | 0.55 |
| **Total** | **36** | — |

### Vertical center-of-mass estimate

`z_CG = sum(m_i × z_i) / sum(m_i)`

Using the above assumptions:

`z_CG = (9×0.18 + 8×0.16 + 7×0.52 + 4×0.72 + 5×0.91 + 3×0.55)/36 ≈ 0.434 m`.

This estimates **vertical** center of gravity only. Fore-aft and lateral centers require a real CAD bill of materials and positions.

### Illustrative tipping threshold

If the *effective support-polygon half-width* were 0.20 m and the CG lay centrally, a simplified quasi-static critical horizontal acceleration would be approximately:

`a_crit ≈ g × b / z_CG = 9.81 × 0.20 / 0.434 ≈ 4.52 m/s²`.

This is **not a validated operating acceleration limit or safe maneuver threshold**. Actual stability is governed by wheel/caster contact geometry, obstacles, floor friction, uneven loading, braking and dynamics. An engineer must evaluate realistic support polygon and margins. No robot should be driven based on this idealized number.

### Required next measurements

1. Define exact wheel and caster ground contact coordinates for all three envelopes.
2. Compute loaded/empty 3D CG in CAD, including a conservative head/display configuration.
3. Analyze stopping, slope/threshold, acceleration and push disturbances with safety factors.
4. Test under supervision using a controlled low-energy rig after hazard assessment.
