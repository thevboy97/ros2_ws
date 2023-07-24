# ROS subscriber to evaluate time difference

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from datetime import datetime


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.previous_time = None
        self.publisher_ = self.create_publisher(String, 'diff', 10)

        self.subscription = self.create_subscription(
            String,
            'data',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        
        current_time = datetime.strptime(msg.data.split(',')[3], '%Y-%m-%d %H:%M:%S%z').timestamp()
        if self.previous_time is not None:
            diff = current_time - self.previous_time
            msg = String()
            msg.data = str(diff)
            self.publisher_.publish(msg)
            self.get_logger().info('Time difference: "%s"' % msg.data)
        
        self.previous_time = current_time

        

def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
