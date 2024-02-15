#!/usr/bin/env python

import rospy
import tf

if __name__ == "__main__":
    rospy.init_node('map_vicon')
    tf_broadcaster = tf.TransformBroadcaster()
    
    rate = rospy.Rate(10.0)  # Frecuencia de publicación
    
    while not rospy.is_shutdown():
        tf_broadcaster.sendTransform((0, 0, 0),
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "map",
                                     "vicon")
        
        tf_broadcaster.sendTransform((0, 0, 0),
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "odom",
                                     "map")
        rate.sleep()