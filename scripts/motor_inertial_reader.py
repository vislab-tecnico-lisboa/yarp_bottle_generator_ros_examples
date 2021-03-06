#!/usr/bin/env python
import rospy
from yarp_bottle_generator_ros_examples.msg import MotorsInertial

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard inertial data %s", data.inertial)
    rospy.loginfo(rospy.get_caller_id() + " I heard encoders data %s", data.encoders)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('motors_inertial_listener', anonymous=True)

    rospy.Subscriber("/motors_inertial_port", MotorsInertial, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
