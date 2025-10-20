import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import PointCloud2
from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy

from sensor_msgs_py import point_cloud2 as pc2
from .pc2_utils import points_rgb_to_cloud

class FusionNode(Node):
    def __init__(self):
        super().__init__('fusion_node')
        self.declare_parameters('', [
            ('lidar_topic', '/carla/hero/lidar'),
            ('segmented_topic', '/fusion/segmented_cloud'),
            ('frame_id', 'lidar_frame'),
        ])

        sensor_qos = QoSProfile(
            depth=5,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST
        )
        lidar_topic = self.get_parameter('lidar_topic').value
        self.out_topic = self.get_parameter('segmented_topic').value
        self.frame_id = self.get_parameter('frame_id').value

        self.sub = self.create_subscription(PointCloud2, lidar_topic, self.cb, sensor_qos)
        self.pub = self.create_publisher(PointCloud2, self.out_topic, sensor_qos)
        self.get_logger().info(f'fusion_node: subscribing {lidar_topic} → publishing {self.out_topic}')

    def cb(self, msg: PointCloud2):
        # Use read_points_numpy to avoid structured dtypes
        try:
            # Returns (N,3) float32 for x,y,z
            xyz = pc2.read_points_numpy(msg, field_names=['x', 'y', 'z'])
        except AttributeError:
            # Fallback if your ROS distro lacks read_points_numpy
            # Convert generator of tuples → plain array
            pts_list = list(pc2.read_points(msg, field_names=['x', 'y', 'z'], skip_nans=True))
            if not pts_list:
                return
            xyz = np.asarray(pts_list, dtype=np.float32)

        if xyz.size == 0:
            return

        # TODO: replace with your labels → colors after Cylinder3D & fusion
        colors = np.full((xyz.shape[0], 3), [128, 128, 128], dtype=np.uint8)

        header = msg.header
        header.frame_id = self.frame_id  # keep consistent for RViz/TF
        cloud = points_rgb_to_cloud(header, xyz[:, :3].astype(np.float32, copy=False), colors)
        self.pub.publish(cloud)

def main():
    rclpy.init()
    rclpy.spin(FusionNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
