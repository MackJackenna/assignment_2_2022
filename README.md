# About Repository:
This repoistory outlines four distinct nodes that provide information to the user about a laser-vision robot that can be moved within an arena. Node_A1 allows the user to input a desired (x,y) goal for the robot, as well as the ability to cancel any active goals. Node_A2 provides the user with the robots current position and velocity within the arena. Node_B displays to the user how many goals have been successfully reached or cancelled since startup. Node_C gives the user the position of the robot away from the set goal, as well as it's average velocity.

# How to Launch:
To launch, gnome-terminal must be installed on the docker image, this can be done by running *sudo apt-get update* and then *sudo apt-get install gnome-terminal*. You can then run the whole package using the command **roslaunch assignment_2_2022 all_nodes.launch**. This will open four individual terminals with each of the nodes active.

# Pseudocode for Node_A1 and Node_A2:
Node_A1:

    Import rospy
    Import os
    Import actionlib.msg
    Import assignment_2_2022.msg
    From geometry_msgs.msg Import PoseStamped

    Set on_startup To 1
    
    Define Function startup(on_startup)
	
	    System Clear
	    Print "--------------------Node A1--------------------"
	    Print "Node A1 acts as the user interface allowing the"
	    Print "user to input a desired X, Y goal position. "
	    Print "The user can also cancel active goals."
	    Print "Press enter to continue..."
	    User Input enter

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
 
    Define Function startup(on_startup)
	
	    System Clear
	    Print "--------------------Node A2--------------------"
	    Print "Node A2 prints the current position of the"
	    Print "in the form (x, y, vel_x, vel_y)."
	    Print "Press enter to continue..."
	    User Input enter

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


    If __name__ is Equal to '__main__'
	
	    If on_startup is Equal to 1
		    Call Function startup
		    Set on_startup Equal to 0
	
	    Initialise Node
	    Call Subscriber

	    Call rospy.spin()
	    
# Things to improve:
Node_C does not use a parameter to change the message rate of display but instead asks for a user integer input. Given a revisit of the package, this would be ammended to include the parameter.
Modifying the launch file to include the geometry of the four terminals relative to the screen would help to make the running of the package more fluid, with less work to do for the user.
The actual position of the robot seems to be out by 0.5 in the x coordinate, I am unsure whether this is down to my coding or to the simulation environment.

	
	
