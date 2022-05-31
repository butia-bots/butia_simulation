#!/usr/bin/env python

import numpy as np
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32


class Face:
    def __init__(self):
        rospy.init_node('doris_faces', anonymous=False, disable_signals=False)
        
        self.topic = '/doris_sentiment'
        
        self.pub = rospy.Publisher(self.topic , Int32, queue_size=15)
               
        self.rate = rospy.Rate(0.5)
        
        self.faces = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 5, 5, 5, 5, 0]
        
    def publisher(self):
        while not rospy.is_shutdown():
            for a in self.faces:
                self.pub.publish(a)
                print("Adivinhe o sentimento!")
                self.rate.sleep()

if __name__ == '__main__':
    try:
        face = Face()
        face.publisher()
    except rospy.ROSInterruptException as e:
        print('aaaaaaaaaaaaa')
        print(e)
