from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
import xacro

def generate_launch_description():
 share=Path(get_package_share_directory('novera_description'))
 description=xacro.process_file(str(share/'urdf/novera.urdf.xacro')).toxml()
 return LaunchDescription([
  IncludeLaunchDescription(PythonLaunchDescriptionSource(str(Path(get_package_share_directory('ros_gz_sim'))/'launch/gz_sim.launch.py')),launch_arguments={'gz_args':'-r '+str(share/'worlds/indoor.sdf')}.items()),
  Node(package='robot_state_publisher',executable='robot_state_publisher',parameters=[{'robot_description':description,'use_sim_time':True}]),
  Node(package='ros_gz_sim',executable='create',arguments=['-name','novera_one','-topic','robot_description','-z','0.02']),
  Node(package='ros_gz_bridge',executable='parameter_bridge',parameters=[{'config_file':str(share/'config/bridge.yaml'),'use_sim_time':True}])])
