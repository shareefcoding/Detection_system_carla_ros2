from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    cyl_share = get_package_share_directory('cylinder3d')
    det_share = get_package_share_directory('detection_system')

    cyl_params = os.path.join(cyl_share, 'config', 'cyl3d_params.yaml')
    det_params = os.path.join(det_share, 'config', 'fusion_params.yaml')
    rviz_cfg  = os.path.join(det_share, 'rviz', 'fusion_view.rviz')

    return LaunchDescription([
        # New-style args for static TF
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='lidar_tf',
            arguments=[
                '--frame-id', 'base_link',
                '--child-frame-id', 'lidar_frame',
                '--x', '0', '--y', '0', '--z', '0',
                '--roll', '0', '--pitch', '0', '--yaw', '0',
            ],
            output='screen'
        ),
        Node(
            package='cylinder3d',
            executable='cylinder3d_node',
            name='cylinder3d_node',
            output='screen',
            parameters=[cyl_params]
        ),
        Node(
            package='detection_system',
            executable='fusion_node',
            name='fusion_node',
            output='screen',
            parameters=[det_params]
        ),
        # Node(
        #     package='rviz2',
        #     executable='rviz2',
        #     name='rviz2',
        #     arguments=['-d', rviz_cfg],
        #     output='screen'
        # ),
    ])
