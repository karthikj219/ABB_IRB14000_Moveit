cmake_minimum_required(VERSION 2.8.3)
project(test1_moveit_config)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  tf
  robot_state_publisher
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})

catkin_install_python(PROGRAMS
  scripts/mainNode.py
 DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})