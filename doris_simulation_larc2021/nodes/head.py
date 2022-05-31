#!/usr/bin/env python

import numpy as np
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32


class Face:
    def __init__(self):
        rospy.init_node('doris_head', anonymous=False, disable_signals=False)
        
        self.topics = ['/doris_head/horizontal_neck_joint_position_controller/command', #0
                       '/doris_head/vertical_neck_joint_position_controller/command', #1
                       '/doris_head/jaw_joint_position_controller/command', #2
                       '/doris_head/right_vertical_eyebrow_joint_position_controller/command', #3
                       '/doris_head/left_vertical_eyebrow_joint_position_controller/command', #4
                       '/doris_head/right_rotacional_eyebrow_joint_position_controller/command', #5
                       '/doris_head/left_rotacional_eyebrow_joint_position_controller/command', #6
                       '/doris_head/right_superior_eyelid_joint_position_controller/command', #7
                       '/doris_head/left_superior_eyelid_joint_position_controller/command', #8
                       '/doris_head/right_inferior_eyelid_joint_position_controller/command', #9
                       '/doris_head/left_inferior_eyelid_joint_position_controller/command', #10
                       '/doris_head/right_eye_horizontal_joint_position_controller/command', #11
                       '/doris_head/left_eye_horizontal_joint_position_controller/command', #12
                       '/doris_head/right_eye_vertical_joint_position_controller/command', #13
                       '/doris_head/left_eye_vertical_joint_position_controller/command'] #14
        
        self.pub = [rospy.Publisher(i , Float64, queue_size=15)
               for i in self.topics]
        
        self.rate = rospy.Rate(60)
        
        rospy.Subscriber("/doris_sentiment", Int32, self.get_pose)
        
      
        self.pose = np.zeros(15)
        
    def publisher(self):
        while not rospy.is_shutdown():
            for a,p in enumerate(self.pub):
                p.publish(self.pose[a])
            self.rate.sleep()
    
    def get_pose(self, sentiment):
        if sentiment.data == 0: #seriedade
            self.pose = np.zeros(15)
        if sentiment.data == 1: #surpresa
            self.pose = [0.0, 0.0, 0.2, 0.1, 0.1, -0.12, 0.15, -0.27, -0.02, 0.17, 0.24, 0.0, 0.0, 0.0, 0.0]
        if sentiment.data == 2: #tristeza
            self.pose = [0.0, 0.28, 0.0, 0.0, -0.24, 0.33, 0.0, 0.0, 0.20, 0.4, 0.48, 0.0, 0.0, -0.20, -0.17]
        if sentiment.data == 3: #brabo
            self.pose = [0.0, 0.0, 0.0, 0.0, 0.0, 0.17, -0.17, 0.0, 0.31, 0.37, 0.29, 0.21, 0.36, -0.03, -0.05]
        if sentiment.data == 4: #alegre
            self.pose = [0.0, 0.0, 0.25, 0.2, 0.2, -0.22, 0.35, -0.25, 0.18, 0.11, 0.06, 0.0, 0.0, 0.0, 0.0]
        if sentiment.data == 5: #crazy shit
            self.pose = [np.random.uniform(-0.86,0.86), 
                         np.random.uniform(0.0,0.5),
                         np.random.uniform(0.0,0.5),
                         np.random.uniform(0.0,0.2),
                         np.random.uniform(0.0,0.2),
                         np.random.uniform(-0.4,0.17453),
                         np.random.uniform(-0.17453,0.4),
                         np.random.uniform(-0.4,0.17),
                         np.random.uniform(-0.17453,0.4),
                         np.random.uniform(-0.17,0.7854),
                         np.random.uniform(-0.17453,0.7854),
                         np.random.uniform(-0.27453,0.4),
                         np.random.uniform(-0.27453,0.7854),
                         np.random.uniform(-0.2,0.7854),
                         np.random.uniform(-0.17453,0.7854)]
if __name__ == '__main__':
    try:
        face = Face()
        face.publisher()
    except rospy.ROSInterruptException as e:
        print('Error on initializing servos...')
        print(e)
