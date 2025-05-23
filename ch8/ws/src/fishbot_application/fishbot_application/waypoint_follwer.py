from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

def main():
    rclpy.init()
    
    navigator = BasicNavigator()
    navigator.waitUntilNav2Active()

    goal_pose = []
    goal_pose1 = PoseStamped()
    goal_pose1.header.frame_id = 'map'
    goal_pose1.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose1.pose.position.x = 0.0
    goal_pose1.pose.position.y = 0.0
    goal_pose1.pose.orientation.w = 1.0
    goal_pose.append(goal_pose1)
    
    goal_pose2 = PoseStamped()
    goal_pose2.header.frame_id ='map'
    goal_pose2.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose2.pose.position.x = 1.0
    goal_pose2.pose.position.y = 1.0
    goal_pose2.pose.orientation.w = 1.0
    goal_pose.append(goal_pose2)
    
    goal_pose3 = PoseStamped()
    goal_pose3.header.frame_id ='map'
    goal_pose3.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose3.pose.position.x = 2.0
    goal_pose3.pose.position.y = 2.0
    goal_pose3.pose.orientation.w = 1.0
    goal_pose.append(goal_pose3)
    
    navigator.followWaypoints(goal_pose)
    
    while not navigator.isTaskComplete():
        feedback = navigator.getFeedback()
        navigator.get_logger().info(f"current goal idx: {feedback.current_waypoint}")
        
    result = navigator.getResult()
    
    if result == TaskResult.SUCCEEDED:
        navigator.get_logger().info("navigation succeed!")
    elif result == TaskResult.CANCELED:
        navigator.get_logger().warn("navigation canceled!")
    elif result == TaskResult.FAILED:
        navigator.get_logger().error("navigation failed!")
    else:
        navigator.get_logger().error("navigation error!")
        
    navigator.destroy_node()
    rclpy.shutdown()