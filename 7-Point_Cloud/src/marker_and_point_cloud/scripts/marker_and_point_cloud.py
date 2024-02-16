#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker, MarkerArray
from sensor_msgs.msg import PointCloud
import tf
from geometry_msgs.msg import Point

class MarkerPublisherNode:
    def __init__(self):
        rospy.init_node('marker_publisher_node')
        self.marker_pub = rospy.Publisher('marker_topic', Marker, queue_size=10)
        self.point_cloud_pub = rospy.Publisher('point_cloud_topic', PointCloud, queue_size=10)
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
        marker.scale.x = 0.3  # Cambia estos valores para ajustar el tamaño del marcador
        marker.scale.y = 0.3  # Cambia estos valores para ajustar el tamaño del marcador
        marker.scale.z = 0.3  # Cambia estos valores para ajustar el tamaño del marcador
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        self.marker_pub.publish(marker)

    def publish_point_cloud(self):
        point_cloud = PointCloud()
        point_cloud.header.frame_id = "sensor2_frame"
        point_cloud.header.stamp = rospy.Time.now()
        # Agrega algunos puntos a la nube de puntos
        point1 = Point(x=1, y=0, z=0)
        point2 = Point(x=0, y=1, z=0)
        point3 = Point(x=0, y=0, z=1)
        point_cloud.points = [point1, point2, point3]
        self.point_cloud_pub.publish(point_cloud)

    def run(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            self.publish_marker()
            self.publish_point_cloud()
            rate.sleep()

if __name__ == "__main__":
    marker_publisher = MarkerPublisherNode()
    marker_publisher.run()
