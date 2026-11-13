# ROS 2 Jazzy / Gazebo Harmonic scaffold — NOT EXECUTED

Ubuntu 24.04 target. No ROS or Gazebo executable was available in the implementation runtime. XML parsing is not a simulation build or integration test. This scaffold must not be marked a complete MVP.

After installing official ROS Jazzy / ros_gz packages in an approved environment:

```sh
source /opt/ros/jazzy/setup.bash
cd ros2
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
ros2 launch novera_description sim.launch.py
```

Candidate B dimensions are hypotheses. ROS uses X forward / Y left; existing OpenSCAD uses X lateral / Y longitudinal. This deliberate 90-degree coordinate mapping preserves 382mm drive track and ±173mm caster positions. Inertias are positive placeholder estimates, not the G1 point-mass distribution or real material properties. Body is simplified collision geometry; no manufacturing inference.

Expected checks still UNEXECUTED: Gazebo spawn and contacts, wheel direction, odometry/TF consistency, LiDAR ray hits, RGB-D topic/frame names, IMU, bridge discovery, clock, headless GPU support and stopping behavior. Empty frame links may be merged during URDF→SDF conversion; inspect the resulting model and sensor poses. Add optical camera transforms after topic validation.

Missing integrations: SLAM Toolbox launch/config, saved map, AMCL localization, Nav2 behavior tree/controller tuning and waypoint action client; RViz2 configuration; ROS velocity supervisor independent from the local 2D service; Gazebo-to-browser telemetry adapter. The direct cmd_vel bridge is a simulator-only development interface and has no safety supervisor: never connect it to physical hardware. Simulated estop currently exists only in research/supervisor.py, not this scaffold.

Gate procedure: record OS/package versions and seed; build; capture /clock /scan /imu /odom /tf /camera data and rosbag; map controlled world; save/relocalize map; execute approved waypoints; inject sensor/link/energy faults; verify all motion inhibited and stop latched; archive logs with failures. Do not mark release passed until those artifacts exist. Physical stop validation is a separate gate.
