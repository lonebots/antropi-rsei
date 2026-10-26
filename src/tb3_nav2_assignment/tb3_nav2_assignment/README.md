# TurtleBot3 Autonomous Navigation with ROS 2 Nav2

## Overview

This project demonstrates autonomous navigation using TurtleBot3 in a
Gazebo simulation with ROS 2 Jazzy and Navigation2 (Nav2).

The robot receives a navigation goal through RViz, plans a path, and
uses Nav2 to move toward the goal while avoiding obstacles represented
in its navigation costmaps.

The project uses the existing TurtleBot3 simulation and Nav2 packages.
No custom path-planning or control algorithms are implemented.

## Technology Stack

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo simulation
- TurtleBot3
- Navigation2 (Nav2)
- RViz
- Python launch system

## Architecture

The navigation pipeline is:

Gazebo simulation
    |
    v
Simulated sensors and odometry
    |
    v
ROS 2 topics and TF transforms
    |
    v
Localization and costmaps
    |
    v
Nav2 planner
    |
    v
Nav2 controller
    |
    v
Velocity commands
    |
    v
TurtleBot3 movement in Gazebo

RViz is used to visualize the robot, map, sensor information, planned
path, and navigation goals.

## Prerequisites

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo supported by the installed Jazzy Nav2 packages
- Colcon and the ROS 2 build tools

Install the required packages:

```bash
sudo apt update

sudo apt install \
  ros-jazzy-navigation2 \
  ros-jazzy-nav2-bringup \
  'ros-jazzy-nav2-minimal-tb*' \
  python3-colcon-common-extensions
