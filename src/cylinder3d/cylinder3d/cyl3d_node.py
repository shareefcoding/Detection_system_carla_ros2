# cylinder3d/cylinder3d/cyl3d_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

class Cylinder3DNode(Node):
    def __init__(self):
        super().__init__('cylinder3d_node')
        self.declare_parameters('', [
            ('lidar_topic', '/carla/hero/lidar'),
            ('model_cfg', ''), ('model_ckpt', ''), ('use_gpu', True)
        ])
        self.model_cfg = self.get_parameter('model_cfg').get_parameter_value().string_value
        self.model_ckpt = self.get_parameter('model_ckpt').get_parameter_value().string_value
        self.use_gpu = self.get_parameter('use_gpu').get_parameter_value().bool_value

        # TODO: replace with correct API from upstream repo
        # self.model = Cylinder3DInferencer(self.model_cfg, self.model_ckpt, use_gpu=self.use_gpu)

        topic = self.get_parameter('lidar_topic').get_parameter_value().string_value
        self.sub = self.create_subscription(PointCloud2, topic, self.cb, 10)
        self.pub = self.create_publisher(PointCloud2, '/cylinder3d/colored_cloud', 10)

    def cb(self, msg: PointCloud2):
        # TODO: convert PointCloud2 → numpy (x,y,z,intensity)
        # logits, labels, colors = self.model.infer(points)
        # msg_out = make_colored_pointcloud2(msg.header, points, colors)
        # self.pub.publish(msg_out)
        self.pub.publish(msg)  # temporary passthrough

def main():
    rclpy.init()
    rclpy.spin(Cylinder3DNode())
    rclpy.shutdown()

if __name__ == '__main__':
    main()

