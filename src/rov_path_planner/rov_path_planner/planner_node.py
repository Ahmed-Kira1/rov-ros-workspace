import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped


class RovPathPlannerNode(Node):
    def __init__(self):
        super().__init__("rov_path_planner_node")
        self.mode = "IDLE"
        self.mode_sub = self.create_subscription(String, "/rov/system/mode", self.mode_callback, 10)
        self.path_pub = self.create_publisher(Path, "/rov/planner/path", 10)
        self.timer = self.create_timer(1.0, self.publish_sample_path)
        self.get_logger().info("ROV Path Planner node initialized and ready.")

    def mode_callback(self, msg: String):
        self.mode = msg.data
        self.get_logger().info(f"System mode updated: {self.mode}")

    def publish_sample_path(self):
        path_msg = Path()
        path_msg.header.stamp = self.get_clock().now().to_msg()
        path_msg.header.frame_id = "map"
        for i in range(5):
            pose = PoseStamped()
            pose.header = path_msg.header
            pose.pose.position.x = float(i) * 0.5
            pose.pose.position.y = float(i) * 0.2
            pose.pose.position.z = -1.0
            pose.pose.orientation.w = 1.0
            path_msg.poses.append(pose)
        self.path_pub.publish(path_msg)


def main(args=None):
    rclpy.init(args=args)
    node = RovPathPlannerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
