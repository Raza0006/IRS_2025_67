import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class   StatusUpdatePublisher(Node):
    def __init__(self):
        super().__init__('StatusUpdatePublisher')  # initialise node with name of the node
        self.publisher_ = self.create_publisher(String, '/status_updates', 10) # Create publisher, specified queue  buffer and topic 
        timer_period = 0.5  # publish rate seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.i = 0 #callback counter

    def timer_callback(self):
        msg = String()
        msg.data = f'Exploding in {self.i}'
        self.publisher_.publish(msg)

        self.get_logger().info(f'Published "{msg.data}" seconds')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    statusUpdatePublisher = StatusUpdatePublisher() #create publisher
    rclpy.spin(statusUpdatePublisher)
    statusUpdatePublisher.destroy_node()
    rclpy.shutdown

if __name__ == '__main__':
    main()
