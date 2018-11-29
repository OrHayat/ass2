#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
import sys
import os
import random
from sensor_msgs.msg import Image, LaserScan, CameraInfo
import random
from std_msgs.msg import Bool, Int32, Float32
import numpy as np
import time
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from node3 import find_object
PI = 3.1415926535897
def rotate(angle):
	data=rospy.wait_for_message("/scan", LaserScan)
	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)	
	current_dis=0
	t1=0
	t0=0
	center=data.ranges[0]
	rospy.loginfo(center)
	vel_msg= Twist()
	print("Let's rotate your robot")
	speed = angle/2
	angular_speed = speed*2*PI/360
        relative_angle = angle*2*PI/360
	#We wont use linear components
        vel_msg.linear.x=0
	vel_msg.linear.y=0
	vel_msg.linear.z=0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
       	vel_msg.angular.z = abs(angular_speed)
    	t0 = rospy.Time.now().to_sec()
    	current_angle = 0
    	while((not rospy.is_shutdown()) and current_angle < relative_angle):
        	velocity_publisher.publish(vel_msg)
        	t1 = rospy.Time.now().to_sec()
        	current_angle = angular_speed*(t1-t0)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)


def move_forward():
	data=rospy.wait_for_message("/scan", LaserScan)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)	
	current_dis=0
	t1=0
	t0=0
	print (data.angle_min)
	center=data.ranges[0]
	rospy.loginfo(center)
	msg= Twist()
	if( center>0.7):
		msg.linear.x= 0.1
	else:
		msg.linear.x= 0.0
		pub.publish(msg)
		return False
	t0=rospy.Time.now().to_sec()
	while((not rospy.is_shutdown()) and current_dis<0.5):
		pub.publish(msg)
		t1=rospy.Time.now().to_sec()
		current_dis=msg.linear.x*(t1-t0)
	print current_dis
	msg.linear.x= 0.0	
	pub.publish(msg)
	return True

	
def move ():
	global r
	global g
	global b
	r=input("insert red\n")
	g=input ("insert green\n")
	b=input("insert blue\n")
	found=False
	print "move function"
	len=find_object(r,g,b)
	while((not rospy.is_shutdown())and len is None or len>0.6):
		print "len="+str(len)
		moved = move_forward()
		if(moved ==False):
		    rotate(random.uniform( 20, 50 ))
		len=find_object(r,g,b)

if __name__ == '__main__':
     try:
	 rospy.init_node('move', anonymous=True)
         move()
     except rospy.ROSInterruptException: pass
