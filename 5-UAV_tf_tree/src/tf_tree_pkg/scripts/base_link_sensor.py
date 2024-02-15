#!/usr/bin/env python

import rospy
import tf

if __name__ == "__main__":
    rospy.init_node('base_link_sensor')
    tf_broadcaster = tf.TransformBroadcaster()

    rate = rospy.Rate(10.0)  # Frecuencia de publicación

    while not rospy.is_shutdown():
        # Sensor 1
        tf_broadcaster.sendTransform((0, 0, 1),  # Cambia estos valores según la posición del sensor 1
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "sensor1",
                                     "base_link")

        # Sensor 2
        tf_broadcaster.sendTransform((1, 1, 0),  # Cambia estos valores según la posición del sensor 2
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "sensor2",
                                     "base_link")

        # Sensor 3
        tf_broadcaster.sendTransform((0, 0, 1),  # Cambia estos valores según la posición del sensor 3
                                     (0, 0, 0, 1),  # Quaternion representing no rotation
                                     rospy.Time.now(),
                                     "sensor3",
                                     "base_link")

        rate.sleep()
