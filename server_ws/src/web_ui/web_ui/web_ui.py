#!/usr/bin/env python3

import cv2
import rclpy
from rclpy.node import Node
from lampo_interfaces.msg import Map, TrafficLights, TurnSignals

class WebUINode(Node):
    def __init__(self):
        super().__init__("web_ui_node")

        self.map_publisher = self.create_publisher(Map, 'road_map', 2)
        self.lights_publisher = self.create_publisher(TrafficLights, 'traf_lights', 10)
        self.blink_publisher = self.create_publisher(TurnSignals, 'blinkers', 10)

        self.map_timer = self.create_timer(1, self.publish_road_map)

    def publish_road_map(self):
        message = Map()
        message.height = 600
        message.width = 800
        message.tiles_y = 6
        message.tiles_x = 8
        message.roads = [ 6, 10, 14, 10, 14, 12,  6, 12,
                          5,  6, 15, 10,  9,  7,  9,  5,
                          3, 13,  5,  6, 10,  9,  6, 13,
                         5, 6,  1, 8, 5, 5, 6, 10,
                         5, 6,  1, 8, 5, 5, 6, 10,
                         5, 6,  1, 8, 5, 5, 6, 10]

        self.map_publisher.publish(message)
        self.get_logger().info('Publishing road map')


def main(args=None):
    rclpy.init(args=args)

    # initialize model
    web_ui = WebUINode()
    rclpy.spin(web_ui)
    web_ui.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
