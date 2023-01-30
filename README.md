# Pseudocode:
Node_A1:

    Import rospy
    Import os
    Import actionlib.msg
    Import assignment_2_2022.msg
    From geometry_msgs.msg Import PoseStamped

    Set on_startup To 1

    Define Function reaching_goal()

	    System Clear
	    User Input x_coord
	    User Input y_coord

	    Set x_coord To Integer
	    Set y_coord To Integer

	    Print "--------------------------------------------------"
	    Print "X coordinate entered:", x_coord
	    Print "Y coordinate entered:", y_coord
	    Print "--------------------------------------------------"
	    Print "Waiting for server..."
	
	    Waits for the server to load

	    Set goal To PoseStamped()
	    Set x_coord To goal.pose.position.x
	    Set y_coord To goal.pose.position.y
	    Set goal To assignment_2_2022.msg.PlanningGoal(goal)

	    Sends goal to client

	    Print "--------------------------------------------------"
	    User Input enter
	    Call Function interface()

    Define Function cancel_goal()

	    System Clear
	    Cancels current goal
	    Print "--------------------------------------------------"
	    Print "Cancelled!"
	    Print "Press enter to continue..."
	    User Input enter
	    Call Function interface()

    Define Function wrong()
	
	    System Clear
	    Print "--------------------------------------------------"
	    Print "That input does not work! Please enter a suitable value."
	    Print "Press enter to continue..."
	    User Input enter
	    Call Function interface()

    Define Function interface()

	    System Clear
	    Print "--------------------------------------------------"
	    Print "What would you like to do?"
	    Print option 1
	    Print option 2
	    Print option 3
	    Set x To User Input "Please select 1, 2 or 3: "

	    If x is Equal to 1
		    Call reaching_goal()

	    If x is Equal to 2
		    Call cancel_goal()

	    If x is Equal to 3
		    System Clear
		    Print "--------------------------------------------------"
		    Print "Goodbye!"
		    Print "--------------------------------------------------"
		    Exit programme

	    Else
		    Call wron()

    Define Function startup(on_startup)
	
	    System Clear
	    Print "--------------------Node A1--------------------"
	    Print "Node A1 acts as the user interface allowing the"
	    Print "user to input a desired X, Y goal position. "
	    Print "The user can also cancel active goals."
	    Print "Press enter to continue..."
	    User Input enter

    If __name__ Is Equal to '__main__'
	
	    If on_startup is Equal to 1
		    Call startup
		    Set on_startup Equal to 0
	
	    System Clear
	    Initialise Node
	    Set client Equal to actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction)
	    Call interface()

	    Call rospy.spin()
       
Node_A2:

    Import rospy
    Import os
    From nav_msgs.msg Import Odometry
    From assignment_2_2022.msg Import Vel

    Set on_startup Equal To 1

    Define Function callback(a)
	
	    Set pub Equal to rospy.Publisher('position_and_velocity', Vel, queue_size=1)
	    Set message Equal to Vel()
	    Set message.x Equal to a.pose.pose.position.x
	    Set message.y Equal to a.pose.pose.position.y
	    Set message.vel_x Equal to a.twist.twist.linear.x
	    Set message.vel_y Equal to a.twist.twist.linear.y

	    Print "--------------------------------------------------"
	    Print Variable message
	    Publish Variable message

    Define Function startup(on_startup)
	
	    System Clear
	    Print "--------------------Node A2--------------------"
	    Print "Node A2 prints the current position of the"
	    Print "in the form (x, y, vel_x, vel_y)."
	    Print "Press enter to continue..."
	    User Input enter

    If __name__ is Equal to '__main__'
	
	    If on_startup is Equal to 1
		    Call Function startup
		    Set on_startup Equal to 0
	
	    Initialise Node
	    Call Subscriber

	    Call rospy.spin()

	
	
