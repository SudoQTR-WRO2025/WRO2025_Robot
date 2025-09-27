#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarReader(Node):
    def _init_(self):
        super()._init_('lidarRead')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        ranges = [r if r > msg.range_min else float('inf') for r in msg.ranges]

        mid_index = len(ranges) // 2
        right_index = 3 * len(ranges) // 4
        left_index = len(ranges) // 4

        left_dist = ranges[left_index]
        right_dist = ranges[right_index]
        forward_dist = ranges[mid_index]

        print(f"Right: {right_dist:.2f}  Left: {left_dist:.2f}  Forward: {forward_dist:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = LidarReader()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if _name_ == '_main_':
    main()
