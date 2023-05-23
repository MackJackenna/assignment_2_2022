#! /usr/bin/env python3

import rospy
import os
import actionlib.msg
import assignment_2_2022.msg
import actionlib
from geometry_msgs.msg import PoseStamped


on_startup = 1


def startup(on_startup):
	os.system('clear')
	print("--------------------Node A1--------------------\n")
	print("Node A1 acts as the user interface allowing the ")
	print("user to input a desired X, Y goal position. ")
	print("The user can also cancel active goals.")
	print("\nPress enter to continue...")
	input("\n-----------------------------------------------")


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
	
	goal = PoseStamped()
	goal.pose.position.x = x_coord
	goal.pose.position.y = y_coord	
	goal = assignment_2_2022.msg.PlanningGoal(goal)
	
	
	client.send_goal(goal)
	print("--------------------------------------------------")
	input("Goal has reached the server! Press enter to continue...")	
	interface()
	


def cancel_goal():

	
	os.system('clear')
	
	client.cancel_goal()
	print("--------------------------------------------------")
	print("Cancelled!")
	print("\nPress enter to continue...")
	input("--------------------------------------------------")
	interface()

def wrong():

	
	os.system('clear')
	
	print("--------------------------------------------------")
	print("That input does not work! Please enter a suitable value.")
	print("\nPress enter to continue...")
	input("--------------------------------------------------")
	interface()
	
def interface():


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
		
		
if __name__ == '__main__':
	
	if on_startup == 1:
		startup(on_startup)
		on_startup = 0
		
	os.system('clear')
	rospy.init_node('node_A1')
	
	

	client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)
	
	interface()
	
	rospy.spin()
	
	



