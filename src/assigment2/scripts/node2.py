#!/usr/bin/env python
import rospy
PI = 3.1415926535897
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
def rotate():
	data=rospy.wait_for_message("/scan", LaserScan)
	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)	
	current_dis=0
	t1=0
	t0=0
	center=data.ranges[0]
	rospy.loginfo(center)
	vel_msg= Twist()
	print("Let's rotate your robot")
	angle = input("Type your distance (degrees):")
	speed = angle/5
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
    	while(current_angle < relative_angle):
        	velocity_publisher.publish(vel_msg)
        	t1 = rospy.Time.now().to_sec()
        	current_angle = angular_speed*(t1-t0)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)




if __name__ == '__main__':
	rospy.init_node('checkObstacle', anonymous=True)
	rotate()

