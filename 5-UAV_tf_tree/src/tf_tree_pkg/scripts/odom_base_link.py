#!/usr/bin/env python

import rospy
import tf

if __name__ == "__main__":
    rospy.init_node('odom_base_link')
    tf_broadcaster = tf.TransformBroadcaster()
    
    rate = rospy.Rate(10.0)  # Frecuencia de publicación
    
    while not rospy.is_shutdown():
        tf_broadcaster.sendTransform((2, 2, -2),
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "base_link",
                                     "odom")
        rate.sleep()
