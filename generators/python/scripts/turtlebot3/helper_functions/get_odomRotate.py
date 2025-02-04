def get_odomRotate(tf_listener, odom_frame, base_frame):
    try:
        (trans, rot)  = tf_listener.lookupTransform(odom_frame, base_frame, rospy.Time(0))
    except (tf.Exception, tf.ConnectivityException, tf.LookupException):
        rospy.loginfo("TF Exception")
        return

    return quat_to_angle(geometry_msgs.msg.Quaternion(*rot))

