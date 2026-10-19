# Provisional power and energy budget — candidate B

Figures below are **planning assumptions**, not measured draws or selected electrical ratings.

| Load | Average power | Illustrative peak | Notes |
|---|---:|---:|---|
| Two drive motors combined | 35 W | 180 W | Strongly dependent on speed, terrain and gearing |
| Compute and control | 35 W | 65 W | Candidate class not yet selected |
| Sensors and localization | 18 W | 28 W | Depends on actual lidar / depth configuration |
| Display, audio and interface | 25 W | 45 W | Brightness and sound dependent |
| Auxiliary conversion and lighting | 12 W | 24 W | Does not include unbudgeted actuators |
| **Total** | **125 W** | **342 W** | Peak concurrency is a worst-case illustrative sum |

## Runtime scenario

Illustrative battery pack: **24 V nominal × 30 Ah = 720 Wh**. Assume 80% usable energy after margins: **576 Wh**.

At **125 W** estimated average input, idealized runtime is **576 / 125 ≈ 4.6 hours**. Real duty cycles, battery age, temperature, DC conversion losses, acceleration and stops may materially change this. **Do not advertise 4.6 hours as product runtime.**

Battery sizing, chemistry, BMS, protective circuits, wiring gauges, charging method and safety compliance remain unselected.

## Next validation

Record measured idle/rolling/turning energy on low-risk subsystem test rigs; establish simultaneous peak currents, regenerative/braking behavior and fuse sizing with qualified electrical engineering review.
