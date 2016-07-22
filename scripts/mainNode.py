#!/usr/bin/env python

import rospy
import sys
import copy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg


def move_robot():
	print "Starting rospy and moveit..."
	moveit_commander.roscpp_initialize(sys.argv)
	rospy.init_node('move_group_py')

	robot = moveit_commander.RobotCommander()
	scene = moveit_commander.PlanningSceneInterface()
	group1 = moveit_commander.MoveGroupCommander("both_arms")



	display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory, queue_size=1)
	group1.allow_replanning(True)
	group1.set_planning_time(10.0)


	print "Waiting for RViz"
	rospy.sleep(10)
	print "Initializing..."

	print "Reference frame: %s" %group1.get_planning_frame()

	print "Generating plan..."
	group_values = group1.get_current_joint_values()
	group_values[1] = 0
	group_values[2] = 0
	group1.set_joint_value_target(group_values)


	plan1 = group1.plan()
	rospy.sleep(5)

	print "Executing..."
	plan1 = group1.go()

	#print "Visualizing plan..."
	#display_trajectory = moveit_msgs.msg.DisplayTrajectory()
	#display_trajectory.trajectory_start = group1.get_current_joint_values()
	#display_trajectory.trajectory.append(plan1)
	#display_trajectory_publisher.publish(display_trajectory);

	
if __name__ == '__main__':
	try:
		move_robot()
	except rospy.ROSInterruptException:
		pass