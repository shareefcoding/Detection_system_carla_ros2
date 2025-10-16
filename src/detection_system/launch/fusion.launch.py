# detection_system/launch/fusion.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cylinder3d',
            executable='cylinder3d_node',
            name='cylinder3d_node',
            output='screen',
            parameters=['/home/shareef/CARLA_PROJECT/Detection_system_carla_ros2/src/cylinder3d/config/cyl3d_params.yaml']
        ),
        Node(
            package='detection_system',
            executable='fusion_node',
            name='fusion_node',
            output='screen'
        )
    ])
