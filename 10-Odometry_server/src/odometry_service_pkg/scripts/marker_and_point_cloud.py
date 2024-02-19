#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from sensor_msgs.msg import PointCloud2, PointField
import tf
import math
import struct
from std_srvs.srv import Trigger, TriggerResponse

class MarkerPublisherNode:
    def __init__(self):
        rospy.init_node('marker_publisher_node')
        self.marker_pub = rospy.Publisher('marker_topic', Marker, queue_size=10)
        self.point_cloud_pub = rospy.Publisher('point_cloud_topic', PointCloud2, queue_size=10)
        self.tf_broadcaster = tf.TransformBroadcaster()
        self.odometry_service = rospy.Service('odometry_service', Trigger, self.handle_odometry_service)
        self.is_publishing_odometry = False  # Variable para controlar si se está publicando odometría


    def circular_moving(self):
        t = rospy.Time.now().to_sec() * math.pi
        self.tf_broadcaster.sendTransform((2.0 * math.sin(0.5*t), 2.0 * math.cos(0.5*t), 0.0),
                                          (0.0, 0.0, 0.0, 1.0),
                                          rospy.Time.now(),
                                          "base_link",
                                          "odom")

    def handle_odometry_service(self, request):
        rospy.loginfo("Received trigger for publishing odometry.")

        if not self.is_publishing_odometry:  # Si no se está publicando la odometría, iniciar la publicación
            self.is_publishing_odometry = True
            response_message = "Odometry publishing started."
        else:  # Si ya se está publicando la odometría, detenerla
            self.is_publishing_odometry = False
            response_message = "Odometry publishing stopped."
        
        response = TriggerResponse()
        response.success = True
        response.message = response_message
        return response

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
        marker.scale.x = 0.3 
        marker.scale.y = 0.3 
        marker.scale.z = 0.3 
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        self.marker_pub.publish(marker)

    def publish_point_cloud(self):
        point_cloud = PointCloud2()
        point_cloud.header.frame_id = "sensor2_frame"
        point_cloud.header.stamp = rospy.Time.now()
        point_cloud.height = 1
        point_cloud.width = 3
        point_cloud.fields = [PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
                              PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
                              PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1)]
        point_cloud.is_bigendian = False
        point_cloud.point_step = 12
        point_cloud.row_step = point_cloud.point_step * point_cloud.width
        point_cloud.is_dense = True

        points = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        point_cloud_data = []
        for point in points:
            point_cloud_data.extend(struct.pack('fff', *point))
        point_cloud.data = bytearray(point_cloud_data)
        self.point_cloud_pub.publish(point_cloud)


    def run(self):
        rate = rospy.Rate(100)  # 100 Hz
        while not rospy.is_shutdown():
            self.publish_marker()
            self.publish_point_cloud()
            if self.is_publishing_odometry:
                        self.circular_moving()
            rate.sleep()

if __name__ == "__main__":
    marker_publisher = MarkerPublisherNode()
    marker_publisher.run()
