#!/usr/bin/env python

import rospy
import keyboard 

#Import the type of message type
from std_msgs.msg import String
   
#-----------------------------Import from turtlebot3_telep_key
import rospy
from geometry_msgs.msg import Twist
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios

TORPEDO_MAX_LIN_VEL = 0.22

def getKey():
    if os.name == 'nt':
        return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


#--------------------------------------------
def talker():
    #Publica: topic named chatter, type String, 
    pub = rospy.Publisher('topico_llamado_chatter', String, queue_size=10)
 
    #Inicia el nodo
    rospy.init_node('talker', anonymous=True)

    #10 veces por segundo
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
        key = getKey()
        hello_str = ".. %s" % key
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
   
if __name__ == '__main__':
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass