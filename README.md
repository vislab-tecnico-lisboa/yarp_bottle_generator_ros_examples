# yarp_bottle_generator_ros_examples

This is ROS package that contains the message files (.msg) and the python 
scripts that complement the tutorial examples of 
[yarp-bottle-generator](https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator): 
* [tutorial_example_ros_yarp.ini](https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator/blob/master/app/tutorial_example_ros_yarp.ini)
* [tutorial_exampla_yarp_ros.ini](https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator/blob/master/app/tutorial_example_yarp_ros.ini)

## Requirements
ROS installed
Compile YARP with ROS support, YARP examples, and additional devices.
For YARP-ROS support, select the [flags](http://www.yarp.it/yarp_with_ros_configure.html)

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

Compile YARP fakebot tutorial, located in the <yarp-repository>/example/tutorial/fakebot, usign the following <my-fakebot>.ini file

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
* Follow the [instructions](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) for creating a new workspace
* Clone this repository in the `/src` folder of the workspace
* Type `catkin_make`
* Set the enviroment variable `ROS_HOSTNAME` to the IP address (e.g. `export ROS_HOSTNAME=10.0.3.31`), otherwise the yarpserver will not find the topics

## Executing the examples

### YARP-ROS tutorial example
Execute the following command sequence (better if you open a terminal for each command):

	roscore
	yarpserver --ros
	yarpidl_rosmsg --name /typ@/yarpidl
	yarpdev --device fakeIMU
	yarpdev --device test_motor --allow-deprecated-devices --name /dummy_head --axes 5
	rosrun yarp_bottle_generator_ros_examples motor_inertial_reader.py

The final step is to create, compile and execute the code generated by the yarp-bottle-generator example [tutorial_example_yarp_ros.ini](https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator/blob/master/app/tutorial_example_yarp_ros.ini), as follows:

	<path-to-yarp-bottle-generator-exec>/yarpBottleGenerator tutorial_example_yarp_ros.ini yarp_ros_tutorial.cpp
	cd $BOTTLE_GENERATOR_DIR/results/yarp_ros_tutorial
	cmake .
	make
	./yarp_ros_tutorial

### ROS-YARP tutorial example
Execute the following command sequence (better if you open a terminal for each command):

	roscore
	yarpserver --ros
	yarpidl_rosmsg --name /typ@/yarpidl
	<path-to-fakebot-executable>/run_fakebot --from <path-to-fakebot>/<my-fakebot>.ini
	rosrun yarp_bottle_generator_ros_examples fakebot_motor_control.py

The final step is to create, compile and execute the code generated by the yarp-bottle-generator example [tutorial_example_ros_yarp.ini](https://github.com/vislab-tecnico-lisboa/yarp-bottle-generator/blob/master/app/tutorial_example_ros_yarp.ini), as follows:

	<path-to-yarp-bottle-generator-exec>/yarpBottleGenerator tutorial_example_ros_yarp.ini ros_yarp_tutorial.cpp
	cd $BOTTLE_GENERATOR_DIR/results/ros_yarp_tutorial
	cmake .
	make
	./ros_yarp_tutorial

