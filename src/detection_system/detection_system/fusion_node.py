import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

class FusionNode(Node):
    def __init__(self):
        super().__init__('fusion_node')
        self.sub = self.create_subscription(PointCloud2, '/carla/hero/lidar', self.cb, 10)
        self.pub = self.create_publisher(PointCloud2, '/fusion/segmented_cloud', 10)
        self.get_logger().info('fusion_node up. Subscribing to /carla/hero/lidar')

    def cb(self, msg: PointCloud2):
        # TODO: later—call cylinder3d service or topic, then apply fusion boosts
        self.pub.publish(msg)  # pass-through for now

def main():
    rclpy.init()
    node = FusionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
