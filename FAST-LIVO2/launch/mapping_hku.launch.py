from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    share = get_package_share_directory("fast_livo")
    return LaunchDescription(
        [
            DeclareLaunchArgument("play_bag", default_value="false"),
            DeclareLaunchArgument("use_rviz", default_value="true"),
            DeclareLaunchArgument(
                "bag_path",
                default_value="/home/can/codehub/dataset/HKU_Main_Building_ros2_compatible",
            ),
            Node(
                package="fast_livo",
                executable="fastlivo_mapping",
                name="laserMapping",
                output="screen",
                parameters=[
                    os.path.join(share, "config", "avia.yaml"),
                    os.path.join(share, "config", "camera_pinhole.yaml"),
                    {"use_sim_time": True},
                ],
            ),
            Node(
                condition=IfCondition(LaunchConfiguration("use_rviz")),
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                arguments=["-d", os.path.join(share, "rviz_cfg", "fast_livo2.rviz")],
                parameters=[{"use_sim_time": True}],
                output="screen",
            ),
            ExecuteProcess(
                condition=IfCondition(LaunchConfiguration("play_bag")),
                cmd=[
                    "ros2",
                    "bag",
                    "play",
                    LaunchConfiguration("bag_path"),
                    "--clock",
                    "--delay",
                    "3",
                ],
                output="screen",
            ),
        ]
    )
