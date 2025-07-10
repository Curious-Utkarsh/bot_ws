#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from time import sleep

class EdgeAvoidanceBot(Node):
    def __init__(self):
        super().__init__('edge_avoidance_bot')
        
        self.publisher = self.create_publisher(Twist, '/wheel_controller/cmd_vel_unstamped', 10)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)
        self.timer = self.create_timer(0.1, self.control_loop)
        self.cmd_vel = Twist()

        self.up = 0.0
        self.down = 0.0

        self.flag = False

    def lidar_callback(self, msg):
        # Extract ranges
        ranges = msg.ranges
        valid_ranges = [r if r > 0.05 and r < 4.0 else 4.0 for r in ranges]

        self.up = valid_ranges[6]
        self.down = valid_ranges[2]
        #print(len(valid_ranges))

        # Log the regions
        self.get_logger().info(f"Distances - U: {self.up:.2f}, - D: {self.down:.2f}")

    def control_loop(self):
        # Default forward motion
        self.cmd_vel.linear.x = 0.3
        self.cmd_vel.angular.z = 0.0

        #Edge Detection
        if self.down > 0.50:
            self.flag = True #Edge Detected

        if self.flag == True and self.up > 0.60:
            self.cmd_vel.linear.x = -0.4
            self.cmd_vel.angular.z = -1.65
            self.get_logger().info("Edge ahead! Reversing and turning.")
        else:
            self.flag = False



        # Send command
        self.publisher.publish(self.cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    bot = EdgeAvoidanceBot()
    rclpy.spin(bot)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
