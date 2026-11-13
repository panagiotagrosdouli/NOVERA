# Candidate B engineering continuation

Assumptions remain 500×500×1050 mm, 36 kg mass allocation, 76 mm wheel radius and 382 mm drive track. Existing OpenSCAD source is preserved; stale wheel-center documentation corrected from 86 to 76 mm. Existing 3D point-mass CG check remains reproducible. New ROS axes are X forward/Y left, rotated relative to the CAD X lateral/Y longitudinal convention.

## Geometry and mechanical constraints
OpenSCAD is a disconnected envelope study. Manufacturing walls, mounts, fasteners, bearings, tolerances, cable routes, service openings and wheel/shell clearance are not defined. The diamond contact polygon is not the shell bounding rectangle. Determine support contacts for caster swivel extremes and payload/CG bounds before dynamic stability work. No first-order tipping number is a safe operating limit.

## Power and drivetrain trade
Existing assumed mean/peak loads are 125/342 W. The 24V × 30Ah = 720Wh pack with 0.8 usable fraction yields 576Wh; 576Wh/125W is arithmetic, not runtime evidence. A differential drive is simpler to model than omni-drive but cannot move laterally and needs caster/contact assessment. Motor torque, gear ratio, wheel load, continuous thermal current, brakes, stopping distance, fuse coordination, charger and BMS are TBD. No part selected or sourced price asserted.

## Preliminary electrical interfaces
Battery/BMS → fuse/disconnect → separate protected motion and compute rails. Independent physical emergency-stop path must remove/inhibit motion energy without depending on ROS, Wi-Fi or the web service. Encoder/controller interface, watchdog timing, current ratings, DC/DC isolation and reset circuits require qualified design. Compute-to-controller link may be CAN/UART; no selection made. LiDAR/depth links may be USB/Ethernet; datasheets and bandwidth needed.

## Component sourcing register
See component-sourcing.csv. Every mass, rating, price and datasheet field remains TBD until a real manufacturer's source is retrieved and reviewed. Do not convert these subsystem placeholders into a quoted BOM. Component sourcing and design qualification remain externally required.

## Traceability and safety
R-02: local software stop test passes, independent physical stop unimplemented. R-03/R-10: capture disabled, local consent and no retained dialogue; physical indicators/user review pending. R-04/R-07: link-loss/low-battery stop unit tests; no physical safety implication. R-05: bilingual scripted text; full-site localization incomplete. R-09: point-mass arithmetic only. R-01/R-06/R-08: controlled physical and accessibility user validation required.
