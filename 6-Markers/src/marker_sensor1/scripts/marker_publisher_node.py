#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
import tf

class MarkerPublisherNode:
    def __init__(self):
        rospy.init_node('marker_publisher_node')
        self.marker_pub = rospy.Publisher('marker_topic', Marker, queue_size=10)
        self.tf_broadcaster = tf.TransformBroadcaster()

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = "sensor1_frame"
        marker.header.stamp = rospy.Time.now()
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 0
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.orientation.w = 1
        marker.scale.x = 1
        marker.scale.y = 1
        marker.scale.z = 1
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        self.marker_pub.publish(marker)

    def run(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            self.publish_marker()
            rate.sleep()

if __name__ == "__main__":
    marker_publisher = MarkerPublisherNode()
    marker_publisher.run()
