#!/usr/bin/env python

import rospy
import tf
import tf2_ros
from geometry_msgs.msg import TransformStamped

rospy.init_node('tf_tree_builder')

tf_broadcaster = tf.TransformBroadcaster()

# Static transform map -> vicon
tf_broadcaster.sendTransform((0, 0, 0),
                             (0, 0, 0, 1),  # Quaternion representing no rotation
                             rospy.Time.now(),
                             "map",
                             "vicon")

# Static transform odom -> base_link
tf_broadcaster.sendTransform((0, 0, 0),
                             (0, 0, 0, 1),  # Quaternion representing no rotation
                             rospy.Time.now(),
                             "odom",
                             "base_link")

tf_listener = tf.TransformListener()

rate = rospy.Rate(10.0)  # Frecuencia de publicación

while not rospy.is_shutdown():
    try:
        # Obtener la transformación entre odom y base_link
        (trans, rot) = tf_listener.lookupTransform('odom', 'base_link', rospy.Time(0))
        
        # Publicar la transformación
        tf_broadcaster.sendTransform(trans,
                                     rot,
                                     rospy.Time.now(),
                                     "base_link",
                                     "sensor1")
        
        # Publicar transformaciones estáticas de sensor1 a sensor2 y sensor3
        tf_broadcaster.sendTransform((0, 0, 0),
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "sensor1",
                                     "sensor2")
        tf_broadcaster.sendTransform((0, 0, 0),
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "sensor1",
                                     "sensor3")
        
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        continue
    
    rate.sleep()
