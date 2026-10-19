# System architecture — candidate v0.1

```mermaid
flowchart TD
 U[Visitor / operator] --> UI[Touchscreen, speaker, microphone]
 UI --> APP[Application computer]
 APP --> NAV[Navigation / localization software]
 NAV --> CTRL[Motion controller]
 CTRL --> DRV[Motor drivers]
 DRV --> MOT[Drive motors]
 SENS[Lidar / depth / proximity sensors] --> NAV
 ENC[Wheel encoders / IMU] --> CTRL
 SAFE[Physical E-stop / independent safety path] --> POWER[Motion power cutoff]
 POWER --> DRV
 BAT[Battery pack, BMS, fuse, power distribution] --> POWER
 BAT --> APP
 OP[Operator supervised override] --> APP
 ```

**Important:** This is a functional concept, not a verified functional-safety architecture. The e-stop must not rely on an operating system, Wi-Fi, cloud API or ordinary application software. Validate stopping distance, accessible stop placement, bumper/contact sensing and watchdog behavior through hazard analysis and physical tests.

Candidate software split: Linux/ROS 2 on application computer for orchestration; independently controlled low-level motor/stop system; local UI available without cloud connection. Cloud voice services, if ever added, must have a privacy review and must not be needed for safety.

Interfaces to define: power voltages and peak currents, CAN/UART/Ethernet links, sensor update rates, emergency-stop wiring, charger connection, audio/video privacy controls. None finalized.
