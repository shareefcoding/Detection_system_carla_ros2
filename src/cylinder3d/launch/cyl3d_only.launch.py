from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='lidar_tf',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'lidar_frame']
        ),
        Node(
            package='cylinder3d',
            executable='cylinder3d_node',
            name='cylinder3d_node',
            output='screen',
            parameters=['share/cylinder3d/config/cyl3d_params.yaml']
        ),
    ])
