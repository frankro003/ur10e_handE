#!/usr/bin/env python
# license removed for brevity
import rospy
import std_msgs.msg
import trajectory_msgs.msg

def talker():
    #pub = rospy.Publisher('chatter', std_msgs.msg.String, queue_size=10)
    pub = rospy.Publisher('/arm_controller/command', trajectory_msgs.msg.JointTrajectory, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(50) # 10hz
    jt = trajectory_msgs.msg.JointTrajectory()
    jtp = trajectory_msgs.msg.JointTrajectoryPoint()
    while not rospy.is_shutdown():
        jt.header.stamp = rospy.Time.now()
        jt.joint_names = ['shoulder_pan_joint','shoulder_lift_joint','elbow_joint','wrist_1_joint','wrist_2_joint','wrist_3_joint']
        jtp.positions = [0.4014,0.3316,-2.3561,-0.9773,-0.4014,3.0194]
        jtp.velocities = [0.1,0.1,0.1,0.1,0.1,0.1]
        jtp.accelerations = [0,0,0,0,0,0]
        jtp.effort = [0,0,0,0,0,0]
        jtp.time_from_start  = rospy.Duration(1,0)
        jt.points = [jtp]
        rospy.loginfo(jt)
        pub.publish(jt)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass