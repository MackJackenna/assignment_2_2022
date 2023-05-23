#! /usr/bin/env python3

import rospy
import os
import math
from assignment_2_2022.msg import Vel

on_startup = 1


token = 0

temp = 0 


avg_vel = 0


set_goal = 0

def startup(on_startup):
	
	os.system('clear')
	print("--------------------Node C----------------------\n")
	print("Node C compares the robot's current position")
	print("with the set user goal, and returns back the")
	print("position and velocity from the goal.")
	print("\nPress enter to continue...")
	input("\n------------------------------------------------")


def subscriber(a):

	global token, temp, avg_vel, set_goal
	
	goal_x = rospy.get_param("/des_pos_x")
	goal_y = rospy.get_param("/des_pos_y")
	
	robot_x = a.x
	robot_y = a.y
	
	set_goal = math.sqrt(((goal_x - robot_x)**2)+((goal_y - robot_y)**2))
	
	
	
	robot_vel_x = a.vel_x
	robot_vel_y = a.vel_y
	
	robot_vel = math.sqrt(((robot_vel_x)**2)+((robot_vel_y)**2))

	
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
	print("Node C is running!")
	print("------------------------------------------------")
	rospy.init_node("node_C")
	rospy.Subscriber('position_and_velocity', Vel, subscriber)
	

	message_rate = input("Please enter the rate at which you would like the messages to publish: ")
	message_rate = int(message_rate)

	
	while not rospy.is_shutdown():

		print("------------------------------------------------")
		print("The robot's current distance from the goal is ", set_goal)
		print("The robot's current average veloctiy is ", avg_vel)
		print("------------------------------------------------")
		rospy.sleep(message_rate)
