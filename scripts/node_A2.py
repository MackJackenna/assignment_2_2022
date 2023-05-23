## @package assignment_2_2022
#
#\file node_A2.py
#\brief This node prints the current position of the robot to the user.
#\author Jack McKenna
#\version 1.0
#\date 01/02/2023
#
#\details 
#
# Subscribes to: <BR>
#	/odom
#
#Publishes to: <BR>
#	position_and_velocity
#
# Description:
#
# This node prints to the user the current position of the robot as a set of coordinates (x,y,vel_x,vel_y).
#



#! /usr/bin/env python3

import rospy
import os
from nav_msgs.msg import Odometry
from assignment_2_2022.msg import Vel

# node_A2 outlines a custon message that retrieves (x, y, vel_x, vel_y) of the robot and prints it to the terminal

##
#
#\brief This variable acts as a counter for the startup function
#
on_startup = 1
# used for brief node description

##
#\brief Provides a basic node description for ease of use.
#\param on_startup
#\return text display
#
# This function runs on startup of the node and provides a description of it's use to the user.
def startup(on_startup):
	
	os.system('clear')
	print("--------------------Node A2--------------------\n")
	print("Node A2 prints the current position of the")
	print("in the form (x, y, vel_x, vel_y).")
	print("\nPress enter to continue...")
	input("\n-----------------------------------------------")

##
#
#\brief Publishes data from \odom to the user
#\param a
#\return intermediate text message.
#
# This function employs a publisher that subscribes to the /odom (odometry) topic to extract the robots position.
def callback(a):
	
	pub = rospy.Publisher('position_and_velocity', Vel, queue_size=1)
	
	message = Vel()
	
	message.x = a.pose.pose.position.x
	message.y = a.pose.pose.position.y
	message.vel_x = a.twist.twist.linear.x
	message.vel_y = a.twist.twist.linear.y
	#extracts data from the /odom topic to publish to the user
	
	print("--------------------------------------------------")
	print(message)
	pub.publish(message)
	#Prints the message to the terminal
		
		
if __name__ == '__main__':
	
	if on_startup == 1:
		startup(on_startup)
		on_startup = 0
		
	rospy.init_node('node_A2')
	rospy.Subscriber("/odom", Odometry, callback)
	
	rospy.spin()
	
