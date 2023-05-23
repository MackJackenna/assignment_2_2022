#! /usr/bin/env python3

import rospy
import os
import assignment_2_2022.msg
from std_srvs.srv import Empty, EmptyResponse

on_startup = 1


goal_tally = 0


cancel_tally = 0


def startup(on_startup):
	
	os.system('clear')
	print("--------------------Node B----------------------\n")
	print("Node B will provide the user with the running ")
	print("total of succesfully reached goals and canceled ")
	print("goals as and when one occurs. ")
	print("\nPress enter to continue...")
	input("\n------------------------------------------------")


def subscriber(a):

	if a.status.status == 2:
	
		global cancel_tally
		cancel_tally += 1
		os.system('rosservice call tally')
		
		
	if a.status.status == 3:
	
		global goal_tally
		goal_tally += 1
		os.system('rosservice call tally')
				
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
