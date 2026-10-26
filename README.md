# TurtleBot3 Navigation with ROS 2 and Nav2

This project demonstrates autonomous navigation using TurtleBot3 in Gazebo with ROS 2 Jazzy and Navigation2 (Nav2). The robot navigates to goals set in RViz while avoiding obstacles.

The project uses existing ROS 2 packages and Nav2 components.

## Requirements

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo
- RViz
- Colcon

### Install ROS 2 Jazzy

If ROS 2 is not installed, follow the [official installation guide](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html).

### Install Nav2 and simulation dependencies

```bash
sudo apt update

sudo apt install \
  ros-jazzy-navigation2 \
  ros-jazzy-nav2-bringup \
  'ros-jazzy-nav2-minimal-tb*' \
  python3-colcon-common-extensions
```

Source ROS 2:

```bash
source /opt/ros/jazzy/setup.bash
```

## Build

Clone this repository into a ROS 2 workspace:

```bash
mkdir -p ~/tb3_ws/src
cd ~/tb3_ws/src

git clone https://github.com/lonebots/antropi-rsei.git
```

Build the package:

```bash
cd ~/tb3_ws

source /opt/ros/jazzy/setup.bash

colcon build --symlink-install
```

Source the workspace:

```bash
source install/setup.bash
```

## Run

Launch the simulation:

```bash
ros2 launch tb3_nav2_assignment navigation.launch.py
```

This starts Gazebo, RViz, TurtleBot3, and Nav2.


## Navigate to a Goal

1. Wait for Gazebo, RViz, and Nav2 to start.
2. Confirm that the map is visible in RViz and Nav2 is active.
3. If needed, click **Startup** in the Nav2 panel.
4. Set the robot's initial pose using **2D Pose Estimate**.
5. Select **Nav2 Goal** and click a destination on the map.
6. Observe the planned path and the robot's movement in Gazebo.
7. Test a goal that requires navigating around an obstacle.


## References

- [ROS 2 Jazzy installation](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)
- [Nav2 Jazzy Quickstart](https://docs.nav2.org/jazzy/getting_started/quickstart/quickstart/#quickstart)
- [Nav2 documentation](https://docs.nav2.org/)
- [TurtleBot3 documentation](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
