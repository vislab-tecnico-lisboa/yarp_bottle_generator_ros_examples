# yarp_bottle_generator_ros_examples

This is ROS package that contains the message files (.msg) and the python 
scripts that complement the tutorial examples of 
(yarp-bottle-generator)[https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator]: 
* [tutorial_example_ros_yarp.ini](https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator/blob/master/app/tutorial_example_ros_yarp.ini)
* [tutorial_exampla_yarp_ros.ini](https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator/blob/master/app/tutorial_example_yarp_ros.ini)

## Requirements
* Compile YARP with ROS support, YARP examples, and additional devices. For YARP-ROS support, select the 
[flags](http://www.yarp.it/yarp_with_ros_configure.html)
	CREATE_GUIS
	CREATE_LIB_MATH
	CREATE_OPTIONAL_CARRIERS
	CREATE_DEVICE_LIBRARY_MODULES
Select the following devices
	ENABLE_yarpcar_tcpros_carrier
	ENABLE_yarpcar_rossrv_carrier
	ENABLE_yarpcar_xmlrpc_carrier
	ENABLE_yarpmod_fakeIMU
	ENABLE_yarpmod_fakeMotorControl
* Compile YARP fakebot tutorial, located in the <yarp-repository>/example/tutorial/fakebot, usign the following .ini file
	device group

	[part robot]
	device fakebot
	background back.ppm
	target fore.ppm
	noise 0.01

	[part grab]
	device grabber
	subdevice robot
	name /fakebot/camera

	[part board]
	device controlboard
	subdevice robot
	name /fakebot/motor
	allow-deprecated-devices

## Package install
* Follow the (instructions)[http://wiki.ros.org/catkin/Tutorials/create_a_workspace] for creating a new workspace
* Clone this repository in the `/src` folder of the workspace
* Type `catkin_make`
* Set the enviroment variable `ROS_HOSTNAME` to the IP address (e.g. `export ROS_HOSTNAME=10.0.3.31`), otherwise the yarpserver will not find the topics

## Executing the examples

### YARP-ROS tutorial example
Execute the following command sequence:
	yarpserver --ros
	yarpdev --device fakeIMU


