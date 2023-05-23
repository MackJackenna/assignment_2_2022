#! /usr/bin/env python3

import rospy
import os
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import Vel

on_startup = 1

def startup(on_startup):
	
	os.system('clear')
	print("--------------------Node A2--------------------\n")
	print("Node A2 prints the current position of the")
	print("in the form (x, y, vel_x, vel_y).")
	print("\nPress enter to continue...")
	input("\n-----------------------------------------------")

def callback(a):
	
	pub = rospy.Publisher('position_and_velocity', Vel, queue_size=1)
	
	message = Vel()
	
	message.x = a.pose.pose.position.x
	message.y = a.pose.pose.position.y
	message.vel_x = a.twist.twist.linear.x
	message.vel_y = a.twist.twist.linear.y
	
	
	print("--------------------------------------------------")
	print(message)
	pub.publish(message)
	
		
		
if __name__ == '__main__':
	
	if on_startup == 1:
		startup(on_startup)
		on_startup = 0
		
	rospy.init_node('node_A2')
	rospy.Subscriber("/odom", Odometry, callback)
	
	rospy.spin()
	
	
	
		
	
	
