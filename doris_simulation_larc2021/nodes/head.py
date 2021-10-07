#!/usr/bin/env python

import numpy as np
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32


class Face:
    def __init__(self):
        rospy.init_node('doris_head', anonymous=False, disable_signals=False)
        
        self.topics = ['/doris_head/horizontal_neck_joint_position_controller/command',
                       '/doris_head/vertical_neck_joint_position_controller/command',
                       '/doris_head/jaw_joint_position_controller/command',
                       '/doris_head/right_vertical_eyebrow_joint_position_controller/command',
                       '/doris_head/left_vertical_eyebrow_joint_position_controller/command',
                       '/doris_head/right_rotacional_eyebrow_joint_position_controller/command',
                       '/doris_head/left_rotacional_eyebrow_joint_position_controller/command',
                       '/doris_head/right_superior_eyelid_joint_position_controller/command',
                       '/doris_head/left_superior_eyelid_joint_position_controller/command',
                       '/doris_head/right_inferior_eyelid_joint_position_controller/command',
                       '/doris_head/left_inferior_eyelid_joint_position_controller/command',
                       '/doris_head/right_eye_horizontal_joint_position_controller/command',
                       '/doris_head/left_eye_horizontal_joint_position_controller/command',
                       '/doris_head/right_eye_vertical_joint_position_controller/command',
                       '/doris_head/left_eye_vertical_joint_position_controller/command']
        
        self.pub = [rospy.Publisher(i , Float64, queue_size=10)
               for i in self.topics]
        
        self.rate = rospy.Rate(60)
        
        rospy.Subscriber("/doris_sentiment", Int32, self.get_pose)
        
      
        self.pose = np.zeros(15)
        
    def publisher(self):
        while not rospy.is_shutdown():
            for p in self.pub:
                for a in self.pose:
                    p.publish(a)
            self.rate.sleep()
    
    def get_pose(self, sentiment):
        if sentiment.data == 0:
            self.pose = np.ones(15)


if __name__ == '__main__':
    try:
        face = Face()
        face.publisher()
    except rospy.ROSInterruptException as e:
        print('Error on initializing servos...')
        print(e)
