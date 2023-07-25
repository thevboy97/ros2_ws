# Work Test
Publish data from from a csv file and subscribe to it to get the time difference between consecutive datapoints in ROS using python.

# Description
Inside the ```ros2_ws/src/py_pubsub/py_pubsub``` folder, ```publisher_member_function.py``` and ```subscriber_member_function.py``` contain the pythonic publisher and subscriber nodes respectively. The publisher logs the coordinates (longitude, latitude, altitude), time and actual speed on topic ```data```. The subscriber reads the message and publishes the time difference in seconds on topic ```diff```. 

# Requirements
1) ROS2 Humble
2) python3
3) pandas
4) datetime

# How to run
1) Make sure there is ROS2 Humble version installed, and pandas and datetime libraries are installed for use in python3. Download the ```ros2_ws``` repository to local machine and rename the folder exactly to ```ros2_ws```, if it says ```ros2_ws-main```.
2) Install any missing dependencies.
   ```rosdep install -i --from-path src --rosdistro humble -y```
3) Build the package in the root workspace ros2_ws using colcon build.
   ```colcon build --packages-select py_pubsub```
4) In a new terminal, navigate to ros2_ws and source the steup files.
   ```source install/setup.bash```
5) Run talker node for the publisher to view the coordinates (longitude, latitude, altitude), time and actual speed on topic ```data```.
   ```ros2 run py_pubsub talker```
6) In a new terminal, source the setup files from inside ros2_ws again, and then start the listener node to see the time difference in seconds on topic ```diff```.
   ```ros2 run py_pubsub listener```
