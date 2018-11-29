#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
def move():
	data=rospy.wait_for_message("/scan", LaserScan)
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)	
	current_dis=0
	t1=0
	t0=0
	print (data.angle_min)
	center=data.ranges[0]
	rospy.loginfo(center)
	msg= Twist()
	if( center>0.5):
		msg.linear.x= 0.25
	else:
		msg.linear.x= 0.0
		pub.publish(msg)
		return
	t0=rospy.Time.now().to_sec()
	while(current_dis<0.5):
		pub.publish(msg)
		t1=rospy.Time.now().to_sec()
		current_dis=msg.linear.x*(t1-t0)
	print current_dis
	msg.linear.x= 0.0	
	pub.publish(msg)

if __name__ == '__main__':
	rospy.init_node('checkObstacle', anonymous=True)
	move()

