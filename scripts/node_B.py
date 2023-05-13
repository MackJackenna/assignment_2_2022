## @package assignment_2_2022
#
#\file node_B.py
#\brief This node acts as a running tally for goals.
#\author Jack McKenna
#\version 1.0
#\date 01/02/2023
#
#\details 
#
# Subscribes to: <BR>
#	/reaching_goal/result
#
# Server: <BR>
#	tally
#
# Description:
#
# This node takes a running tally of how many goals have been successfully reached or successfully cancelled. It will display as and when one of these conditions are updated.
#


#! /usr/bin/env python3

import rospy
import os
import assignment_2_2022.msg
from std_srvs.srv import Empty, EmptyResponse

# node_B.py will display to the user how many goals have been reached sucessfully and how many have been cancelled

##
#
#\brief This variable acts as a counter for the startup function
#
on_startup = 1

##
#
#\brief This variable acts as a tally for goals reached
#
goal_tally = 0

##
#
#\brief This variable acts as a tally for goals cancelled
cancel_tally = 0
# Stores the number of goals reached and goals cancelled

##
#\brief Provides a basic node description for ease of use.
#\param on_startup
#\return text display
#
# This function runs on startup of the node and provides a description of it's use to the user.
def startup(on_startup):
	
	os.system('clear')
	print("--------------------Node B----------------------\n")
	print("Node B will provide the user with the running ")
	print("total of succesfully reached goals and canceled ")
	print("goals as and when one occurs. ")
	print("\nPress enter to continue...")
	input("\n------------------------------------------------")

##
#\brief This functions updates the tallys.
#\param a
#\return service()
#
# This function subscribes to /reaching_goal/status. A status indicator of 2 translates into a cancelled goal, an indicator of 3 is a reached goal.
def subscriber(a):

	if a.status.status == 2:
	# 2 indicates that the current goal has been cancelled as taken from the /reaching_goal/status topic
		global cancel_tally
		cancel_tally += 1
		os.system('rosservice call tally')
		# Will call the tally when a cancel occurs
		
	if a.status.status == 3:
	# 3 indicated that a goal has been reached successfuly
		global goal_tally
		goal_tally += 1
		os.system('rosservice call tally')
		# Will call the tally when a goal is reached

##
#\brief A service which displays the tallys
#\param b
#\return a displaay of the current tally
#
# This function is initiated by the publisher and prints to the user the amount of times the goal and cancel tally has been updated.		
def service(b):

	global goal_tally, cancel_tally
	print("------------------------------------------------")
	print("The robot has reached it's goal ", goal_tally, "times!")
	print("The goal has been cancelled ", cancel_tally, "times!")
	print("------------------------------------------------")
	return EmptyResponse()
			

if __name__ == '__main__':
	
	if on_startup == 1:
		startup(on_startup)
		on_startup = 0
	
	os.system('clear')
	print("------------------------------------------------")
	print("Node B is running!")
	print("------------------------------------------------")
	
	rospy.init_node("node_B")
	
	rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, subscriber)
	rospy.Service("tally", Empty, service)

	rospy.spin()
	
	
