# ROS publisher to log coordinates and time data

import rclpy
from rclpy.node import Node
import pandas as pd


from std_msgs.msg import String



class MinimalPublisher(Node):

    def __init__(self):
        self.data = pd.read_csv("./src/py_pubsub/py_pubsub/Dataset.csv").filter(items = ['Longitude', 'Latitude','Altitude','Time', 'Actual_Speed'])
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'data', 10)
        timer_period = 1/3 # 3 Hz frequency 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    

    def timer_callback(self):
        msg = String()
        msg.data =  ','.join(map(str, self.data.iloc[self.i].to_list()))
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
