## @package assignment_2_2022
#
#\file node_C.py
#\brief This node displays the robot's current position away from the set goal.
#\author Jack McKenna
#\version 1.0
#\date 01/02/2023
#
#\details 
#
# Subscribes to: <BR>
#	position_and_velocity
#	/des_pos_x
#	/des_pos_y
#
# Description:
#
# This node compares the robot's current position with the goal set by the user and returns the distance between.
#


#! /usr/bin/env python3

import rospy
import os
import math
from assignment_2_2022.msg import Vel

# node_C.py displays to the user the robots position relative to the desired set goal

##
#
#\brief This variable acts as a counter for the startup function
#
on_startup = 1

##
#
#\brief Acts as a counter to change conditions.
token = 0

##
#
#\brief An intermediate variable.
temp = 0 

##
#
#\brief A variable to store the avergae velocity.
avg_vel = 0

##
#
#\brief A varaible to store the user set goal.
set_goal = 0
# Variable initialisation

##
#\brief Provides a basic node description for ease of use.
#\param on_startup
#\return text display
#
# This function runs on startup of the node and provides a description of it's use to the user.
def startup(on_startup):
	
	os.system('clear')
	print("--------------------Node C----------------------\n")
	print("Node C compares the robot's current position")
	print("with the set user goal, and returns back the")
	print("position and velocity from the goal.")
	print("\nPress enter to continue...")
	input("\n------------------------------------------------")

##
#
#\brief This function identifies the robots position and goal position.
#\param a
#\return The average velocity
#
# This function stores the robots current position and set goal position then computes, using pythagorean theorem, the straight line distance of the robot away from the goal.
def subscriber(a):

	global token, temp, avg_vel, set_goal
	
	goal_x = rospy.get_param("/des_pos_x")
	goal_y = rospy.get_param("/des_pos_y")
	
	robot_x = a.x
	robot_y = a.y
	
	set_goal = math.sqrt(((goal_x - robot_x)**2)+((goal_y - robot_y)**2))
	#Pythagorean theorem, C = sqrt((A^2)+(B^2));
	# This returns the distance of the goal from the robot
	
	
	robot_vel_x = a.vel_x
	robot_vel_y = a.vel_y
	
	robot_vel = math.sqrt(((robot_vel_x)**2)+((robot_vel_y)**2))
	#Pythagorean theorem, C = sqrt((A^2)+(B^2))
	# This returns the avergae veolcity
	
	
	if token < 5:
		temp = temp + robot_vel
		token += 1
		
	elif token == 5:
		token = 0
		temp /= 5
		avg_vel = temp
		temp = 0
		
		
if __name__ == '__main__':
	
	if on_startup == 1:
		startup(on_startup)
		on_startup = 0
		
	os.system('clear')
	print("------------------------------------------------")
	print("Node D is running!")
	print("------------------------------------------------")
	rospy.init_node("node_C")
	rospy.Subscriber('position_and_velocity', Vel, subscriber)
	
	##
	#
	#\brief This variable takes a user input as the rate in which the messages will publish to the terminal.
	message_rate = input("Please enter the rate at which you would like the messages to publish: ")
	message_rate = int(message_rate)
	#allows user input for the rate at which the messages appear
	
	while not rospy.is_shutdown():
	# while loop is active as the node is running
		print("------------------------------------------------")
		print("The robot's current distance from the goal is ", set_goal)
		print("The robot's current average veloctiy is ", avg_vel)
		print("------------------------------------------------")
		rospy.sleep(message_rate)
		
		
	


