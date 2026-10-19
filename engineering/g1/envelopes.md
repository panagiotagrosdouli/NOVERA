# Three candidate envelopes — illustrative dimensions

All in **millimetres**, except mass in kg. Envelope dimensions are bounding boxes and not manufacturing drawings. All variants use an indoor differential-drive mobile base with two powered wheels and supporting casters; wheel dimensions and hardware TBD.

| Candidate | Height | Base width | Base depth | Nominal robot mass target | Use-case hypothesis |
|---|---:|---:|---:|---:|---|
| A — compact | 900 | 450 | 450 | 28 kg | Small offices and constrained corridors |
| B — balanced | 1050 | 500 | 500 | 36 kg | Accessible interaction and stable indoor base |
| C — tall display | 1200 | 550 | 550 | 46 kg | Larger display at standing eye-line |

## Geometry hypotheses

- Wheelbase and track: TBD by tire placement and stability checks; do not equate outer-shell width to support polygon width.
- A vertically mounted display should be reachable and legible for seated as well as standing visitors. Test with users before fixing display height.
- Keep battery and other dense parts as low as practical; reserve access for service and independently operated emergency-stop hardware.
- Top-level envelopes exclude explicit human-clearance margin; validate door widths, accessible routes, turning footprints and any local requirements before deployment.

## Concept-only front and side elevation (schematic)

```text
 FRONT                           SIDE
 ┌─────────────────┐             ┌─────────────┐
 │ Head / display  │             │ display     │
 └───────┬─────────┘             └────┬────────┘
         │ column                     │ enclosure
     ┌───┴─────────┐              ┌───┴─────────┐
     │ interface & │              │ computer /  │
     │ electronics │              │ electronics │
     └────┬────────┘              └───┬─────────┘
   ┌──────┴────────┐            ┌──────┴────────┐
   │ battery low   │            │ battery low   │
   │ + drive base  │            │ drive base    │
   └─O──────────O──┘            └──O─────────O──┘
   Width A/B/C:                     Depth A/B/C:
   450/500/550                      450/500/550
```

The sketches are conceptual and not dimensioned CAD or proofs of feasible assembly.
