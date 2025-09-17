import rclpy
import json
from rclpy.node import Node
from std_msgs.msg import String

class   StatusUpdateSubscriber(Node):
    def __init__(self):
        super().__init__('StatusUpdateSubscriber')  # initialise node with name of the node
        self.subscription = self.create_subscription(
            String,
            '/hmi/unified_status',
            self.subscriber_callback,
            10
        )

        self.i = 0 #callback counter

    def subscriber_callback(self, msg):
        try:
            data = json.loads(msg.data) # parse JSON string into Python dict
            stamp = data["stamp"]
            box = data["box"]
            counts = data["counts"]
            print("Received PLC status:")
            print(f"Time: {stamp['sec']}.{stamp['nanosec']}")
            print(f"Box weight raw={box['weight_raw']}")
            print(f" Location: {box['location']}")
            print(f" Counts: big={counts['big']}, medium={counts['medium']}, "
            f"small={counts['small']}, total={counts['total']}")
            print() # empty line at the end
        except Exception as e:
            self.get_logger().error(f"Failed to parse JSON: {e}\nRaw msg={msg.data}")

def main(args=None):
    rclpy.init(args=args)
    statusUpdateSubscriber = StatusUpdateSubscriber() #create publisher
    rclpy.spin(statusUpdateSubscriber)
    statusUpdateSubscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
