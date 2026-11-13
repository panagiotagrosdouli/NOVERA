# NOVERA ONE research software

Run `python3 research/server.py`, then open http://127.0.0.1:8765/digital-twin.html. Run `python3 -m unittest discover -s tests -p 'test_*.py' -v`.

This executable is a local 2D kinematic simulator with raycast LiDAR, deterministic approved waypoint supervision, conservative collision hold, latched simulated stop, link watchdog, fault injection and a battery energy model. It does not implement SLAM, AMCL, Nav2, RGB-D, physical dynamics or real safety. The map and building information are fictional test fixtures explicitly labeled. No camera/microphone capture or cloud AI is used. English/Greek scripted answers never issue motion commands. Separate consent and a supervised mission button are required.

Known limitation: direct waypoint tracking stops at obstacles; no path planning or autonomous obstacle recovery. Do not describe this as the requested complete ROS/Gazebo MVP. See `ros2/README.md` for the unexecuted integration scaffold and release gates.

Telemetry API is the actual evolving local simulator state, not prerecorded animation. GitHub Pages has no Python API; disconnected twin shows OFFLINE and never invents telemetry. Loopback service is for one trusted local operator; not an authenticated network deployment. No messages retained. Stop the process to erase state.
