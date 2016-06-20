#!/usr/bin/env python
# license removed for brevity
import rospy
import random
from yarp_bottle_generator_ros_examples.msg import MotorControl

def talker():
    pub = rospy.Publisher('/fakebot_motor_control_ros', MotorControl, queue_size=10)
    rospy.init_node('motor_control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
            for joint_ in range(0, 2):
                msg = MotorControl()
                msg.joint = joint_
                msg.angle = random.uniform(-20, 20)
                pub.publish(msg) 
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
