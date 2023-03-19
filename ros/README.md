# BZU Workshop - Spring 2023

<p align="center">
<picture>
  <img alt="Purpose Logo" src="../purpose_logo.png" width="20%" hight="20%" >
</picture>
</p>

## Robot Operating System - ROS

The following instructions for installing ROS Kinetic on Ubuntu 16.04 (Xenial)

### Installing Required ROS Packages:

Just copy and paste the following commands in the terminal in your Ubuntu OS.

------------

#### Setup your sources.list
```sh
sudo apt install curl
```

------------

#### Set up your keys
```sh
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

------------

#### Installation

Make sure your OS package index is up-to-date:
```sh
sudo apt-get update
```

------------

#### Desktop-Full Install: (Recommended)
```sh
sudo apt-get install ros-kinetic-desktop-full
```

------------

#### Environment setup
```sh
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

source ~/.bashrc
```

------------

#### Dependencies for building packages
```sh
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

------------

#### Initialize rosdep
```sh
sudo rosdep init

rosdep update
```

------------

#### Test Environment Setup

At home directory, take a look on ```bashrc``` to check out the ```setup.bash```

```sh
gedit .bashrc
```

You should find  ```source /opt/ros/kinetic/setup.bash``` at the end of file.

------------

#### Create Workspace

```sh
mkdir -p ~/bzu_ws/src

cd bzu_ws/
```

compile the default files

```sh
catkin_make
```

Run ROS master

```sh
roscore
```

Explore the default topics

```sh
rostopic list
```

It is not recommended to make all your ROS projects in one workspace.

One of the best practices is to customize the workspace for your ```setup.bash``` file

```sh
gedit .bashrc

source /home/meqdad/bzu_ws/devel/setup.bash
```

#### Create package

```sh
cd bzu_ws/src

catkin_create_pkg ros_demo std_msgs rospy roscpp
```

Defualt packages (```std_msgs rospy roscpp```)

Our created package (```ros_demo```)

Compile created package

```sh
cd bzu_ws/

catkin_make
```

</br>

**Reference:** http://wiki.ros.org/kinetic/Installation/Ubuntu

**Thanks for attending workshop**

_Purpose Team_
