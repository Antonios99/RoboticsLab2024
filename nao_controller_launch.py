from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():


   return LaunchDescription([

   
   #Node(
      #package="movement",
      #namespace="movement",
      #excecutable="movement.py",
      #name="movement"
   #),
   
   Node(
      package="my_robot_controller",
      namespace="my_robot_controller",
      executable="pepper_controller",
   ),
   Node(
      package="speech",
      namespace="speech",
      executable="speech_controller",
   ),
   """
   Node(
      package="ros_gz_bridge",
      #namespace="gazebo_bridge",
      executable="parameter_bridge",
      ros_arguments=["-p","config_file:=/home/ros/ros2_ws/src/my_robot_controller/config/full.yaml"]
   ),
   Node(
      package="naoqi_interface",
      namespace="naoqi_interface",
      executable="interface_controller",
   ),
   """
   ])

