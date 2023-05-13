## @package assignment_2_2022
#
#\file node_A1.py
#\brief The node handles the user input of the robot.
#\author Jack McKenna
#\version 1.0
#\date 01/02/2023
#
#\details 
#
# Clients: <BR>
#	/reaching_goal
#
#
# Description: 
#
# This node concerns itself with defining the user input of the robot. The use can select the desired x and y position as a goal for the robot to travel to. The user also has the option to cancel currently active goals. TESTESTESTESTEST
#
#
#

#! /usr/bin/env python3

import rospy
import os
import actionlib.msg
import assignment_2_2022.msg
import actionlib
from geometry_msgs.msg import PoseStamped

# node_A1.py will outline the interface and the functions required to set and cancel the robot's goal

##
#
#\brief This variable acts as a counter for the startup function
#
on_startup = 1
# will allow for a brief description of the node before it is used

##
#\brief Provides a basic node description for ease of use.
#\param on_startup
#\return text display
#
# This function runs on startup of the node and provides a description of it's use to the user.
def startup(on_startup):
	os.system('clear')
	print("--------------------Node A1--------------------\n")
	print("Node A1 acts as the user interface allowing the ")
	print("user to input a desired X, Y goal position. ")
	print("The user can also cancel active goals.")
	print("\nPress enter to continue...")
	input("\n-----------------------------------------------")

##
#\brief Acts as a UI for the user to input the desired coordinates.
#\return text confirmation.
#
# This function takes an intger input from the user for both x and y coordinates then communicates with the server to update the robots goal.
def reaching_goal():
	
	os.system('clear')
	
	print("--------------------------------------------------")
	x_coord = input("Please enter your desired X coordinate: ")
	y_coord = input("Please enter your desired Y coordinate: ")
	
	x_coord = int(x_coord)
	y_coord = int(y_coord)
	
	print("--------------------------------------------------")
	print("X coordinate entered: ", x_coord)
	print("Y coordinate entered: ", y_coord)
	
	print("--------------------------------------------------")
	print("Waiting for server...")
	client.wait_for_server()
	#Allows the action server to startup before continuing
	
	goal = PoseStamped()
	goal.pose.position.x = x_coord
	goal.pose.position.y = y_coord	
	goal = assignment_2_2022.msg.PlanningGoal(goal)
	#Creates the goal required by the action server
	
	client.send_goal(goal)
	print("--------------------------------------------------")
	input("Goal has reached the server! Press enter to continue...")	
	interface()
	#Sends the goal then switches to the interface function

##
#
#\brief Cancels the currently active goal.
#\return text confirmation.
#
# This function communicates with the server that the current goal has been cancelled by the user.
def cancel_goal():
# Cancels any active goals then goes back to interface()
	
	os.system('clear')
	
	client.cancel_goal()
	print("--------------------------------------------------")
	print("Cancelled!")
	print("\nPress enter to continue...")
	input("--------------------------------------------------")
	interface()

##
#
#\brief Takes into account incorrect user inputs.
#\return text confirmation.
#
# This function identifies incorrect inputs and communicates this to the server.
def wrong():
# Takes into account incorrect inputs
	
	os.system('clear')
	
	print("--------------------------------------------------")
	print("That input does not work! Please enter a suitable value.")
	print("\nPress enter to continue...")
	input("--------------------------------------------------")
	interface()
##
#
#\brief Acts as a UI to select other functions.
#\return one of three functions specified by the user.
#
# This function is an interface that asks the user to select one of three options to either Select a goal, Cancel a goal or Exit the node. Upon a wrong input, the wrong function is used.	
def interface():
# Provides the main interface for accessing goal definitions and cancellations

	os.system('clear')
	
	print("--------------------------------------------------")
	print("What would you like to do? \n")
	
	print("1 - Select your goal position\n")
	print("2 - Cancel current goal\n")
	print("3 - Exit the node\n")
	
	x = input("Please select 1, 2 or 3: ")
	
	if (x == "1"):
		reaching_goal()
		
	elif (x == "2"):
		cancel_goal()
		
	elif (x == "3"):
		os.system('clear')
		print("--------------------------------------------------")
		print("Goodbye!")
		print("--------------------------------------------------")		
		exit()
	
	else:
		wrong()
	# Provides the options to input a goal, cancel a goal or exit the node, else wrong() will run		
		
if __name__ == '__main__':
	
	if on_startup == 1:
		startup(on_startup)
		on_startup = 0
	#allows the description to only run once on startup	
	os.system('clear')
	rospy.init_node('node_A1')
	#initialised the node
	
	##
	#
	#\brief This variable accesses the client.
	#
	client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)
	#acesses the /reaching_goal ros topic
	interface()
	
	rospy.spin()
	# keeps the programme running until the node is exited
	



