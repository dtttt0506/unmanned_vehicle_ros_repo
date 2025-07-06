#!/usr/bin/env python

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped, Point
from std_msgs.msg import Header

class PathPlanner:
    def __init__(self):
        rospy.init_node("path_planner_node", anonymous=True)
        self.path_pub = rospy.Publisher("/global_path", Path, queue_size=10)
        self.goal_sub = rospy.Subscriber("/move_base_simple/goal", PoseStamped, self.goal_callback)
        rospy.loginfo("Path Planner Node Initialized.")

    def goal_callback(self, goal_msg):
        rospy.loginfo("Received new goal: x=%f, y=%f" % (goal_msg.pose.position.x, goal_msg.pose.position.y))
        
        # Simulate a simple straight-line path from origin to goal
        path = Path()
        path.header = Header()
        path.header.stamp = rospy.Time.now()
        path.header.frame_id = "map"

        # Start point (origin)
        start_pose = PoseStamped()
        start_pose.header = path.header
        start_pose.pose.position.x = 0.0
        start_pose.pose.position.y = 0.0
        start_pose.pose.orientation.w = 1.0
        path.poses.append(start_pose)

        # Intermediate points (for a smoother path, if needed)
        # For simplicity, just add the goal as the next point
        path.poses.append(goal_msg)

        self.path_pub.publish(path)
        rospy.loginfo("Published a simple path to the goal.")

if __name__ == "__main__":
    try:
        planner = PathPlanner()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


