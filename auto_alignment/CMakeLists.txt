cmake_minimum_required(VERSION 2.8.3)
project(auto_alignment)

set(CMAKE_BUILD_TYPE "Release")
# set(CMAKE_CXX_FLAGS "-std=c++11")
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -g")

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  sensor_msgs
  roscpp
  rospy
  rosbag
  std_msgs
  tf
)

find_package(Eigen3 REQUIRED)
find_package(PCL REQUIRED)

find_package(OpenMP REQUIRED)

include_directories(
  include
	${catkin_INCLUDE_DIRS} 
	${PCL_INCLUDE_DIRS}
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs nav_msgs roscpp rospy std_msgs
  DEPENDS EIGEN3 PCL 
  INCLUDE_DIRS include
)

add_executable(auto_align_node 
  src/auto_align_node.cpp
  include/scancontext/Scancontext.cpp
)
target_compile_options(auto_align_node 
  PRIVATE ${OpenMP_CXX_FLAGS}
)
target_link_libraries(auto_align_node 
  ${catkin_LIBRARIES} ${PCL_LIBRARIES}
  ${OpenMP_CXX_FLAGS}
)





