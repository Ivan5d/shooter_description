#!/usr/bin/env python

import rospy

#Import the type of message type
from std_msgs.msg import String
   
    def talker():
        #Publica: topic named chatter, type String, 
        pub = rospy.Publisher('topic_llamado_chatter', String, queue_size=10)

        #Inicia el nodo
        rospy.init_node('talker', anonymous=True)

        #10 veces por segundo
        rate = rospy.Rate(10) 
        
        while not rospy.is_shutdown():
           hello_str = "hello world %s" % rospy.get_time()
           rospy.loginfo(hello_str)
           pub.publish(hello_str)
           rate.sleep()
   
    if __name__ == '__main__':
        try:
            talker()
        except rospy.ROSInterruptException:
            pass