import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class   StatusUpdateSubscriber(Node):
    def __init__(self):
        super().__init__('StatusUpdateListener')  # initialise node with name of the node
        self.subscription = self.create_subscription(
            String,
            '/status_updates',
            self.subscriber_callback,
            10
        )

        self.i = 0 #callback counter

    def subscriber_callback(self, msg):
        self.get_logger().info(f'Recieved "{msg.data}" {self.i} times')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    statusUpdateSubscriber = StatusUpdateSubscriber() #create publisher
    rclpy.spin(statusUpdateSubscriber)
    statusUpdateSubscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
