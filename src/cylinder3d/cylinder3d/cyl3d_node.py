import rclpy
from rclpy.node import Node
import numpy as np
from sensor_msgs.msg import PointCloud2
from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy

class Cylinder3DNode(Node):
    def __init__(self):
        super().__init__('cylinder3d_node')
        self.declare_parameters('', [
            ('lidar_topic', '/carla/hero/lidar'),
            ('frame_id', 'lidar_frame'),
            ('model_cfg', ''), ('model_ckpt', ''), ('use_gpu', True),
        ])
        sensor_qos = QoSProfile(depth=5,
                                reliability=QoSReliabilityPolicy.BEST_EFFORT,
                                history=QoSHistoryPolicy.KEEP_LAST)

        topic = self.get_parameter('lidar_topic').value
        self.frame_id = self.get_parameter('frame_id').value
        self.sub = self.create_subscription(PointCloud2, topic, self.cb, sensor_qos)

        # TODO: import and load upstream model here using model_cfg/model_ckpt
        # Example:
        # from <upstream>.inferencer import Inferencer
        # self.model = Inferencer(cfg=self.get_parameter('model_cfg').value,
        #                         ckpt=self.get_parameter('model_ckpt').value,
        #                         use_gpu=self.get_parameter('use_gpu').value)

        self.get_logger().info(f'cylinder3d_node subscribing to {topic}')

        # (optional) publish per-point labels/colors topic if you want a separate stream
        self.pub = self.create_publisher(PointCloud2, '/cylinder3d/colored_cloud', sensor_qos)

    def cb(self, msg: PointCloud2):
        # TODO: convert msg to Nx4 (x,y,z,intensity)
        # pts = ...
        # logits, labels = self.model.infer(pts)
        # produce (optional) colored cloud for debug or for fusion to subscribe
        self.pub.publish(msg)  # temporary pass-through

def main():
    rclpy.init()
    rclpy.spin(Cylinder3DNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
