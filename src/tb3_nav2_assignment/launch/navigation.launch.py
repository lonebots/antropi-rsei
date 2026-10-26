from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    nav2_simulation_launch = PathJoinSubstitution([
        FindPackageShare('nav2_bringup'),
        'launch',
        'tb3_simulation_launch.py',
    ])

    return LaunchDescription([
        DeclareLaunchArgument(
            'headless',
            default_value='False',
            description='Run Gazebo without its graphical interface.',
        ),

        DeclareLaunchArgument(
            'autostart',
            default_value='True',
            description='Automatically activate Nav2 lifecycle nodes.',
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_simulation_launch),
            launch_arguments={
                'headless': LaunchConfiguration('headless'),
                'autostart': LaunchConfiguration('autostart'),
            }.items(),
        ),
    ])
