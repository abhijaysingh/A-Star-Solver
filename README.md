# A* Solver for Turtlebot3 in ROS

## Setup
```
pip3 install -r requirements.txt
```
- ROS - noetic, turtlebot3 (needs to be installed), gazebo_ros

## Execution

* **Part 01 - A\* Solver** 
    
    - To execute the program for this problem, navigate to the project folder and use the following commands
        ```
        cd <path_to_project>/code/
        python3 main.py
        ```

    - Once you run the program, enter the start and goal states in the format shown below:
        ```
        Enter start state (x y theta) : 50 100 0
        Enter end state (x y) : 300 180
        Enter clearance (clearance) : 5
        Enter RPM1 and RPM2 (RPM1, RPM2) : 30 60
        ```

    - Each line of input should be in the format x y theta where x, y and theta are the x and y coordinates of the point and theta is the orientation of the robot respectively.

    - The program will not run if only one of the coordinates is entered or if the coordinates are not integers.

    - The program will not run if the clearance and radius are not entered in the format clearance, radius.

* **Part 02 - ROS**

    - Build the ROS package using the following command:
        ```
        catkin_make
        ```
    - Source the ROS workspace using the following command:
        ```
        source devel/setup.bash
        ```
    
    - Enter the following command to launch the ROS node:
        ```
        roslaunch a_star_solver astar_map.launch
        ```

    - If the roslaunch command doesn't work then navigate to the launch folder in the submission folder and use the following command:
        ```
        roslaunch astar_map.launch
        ```

    - Press the enter key once to display the options for the program.

    - Once you run the program, enter the start and goal states in the format shown below:
        ```
        Enter start state (x y theta) : 0 0 0
        Enter end state (x y) : 5 0
        Enter clearance (clearance) : 5
        Enter RPM1 and RPM2 (RPM1, RPM2) : 30 60
        ```
    - The inputs for the coordinates should be with respect to the Gazebo world frame. 

## Results
* **A\* Solver** 
    
    - The outputs is as shown below:
        ```
        Enter start state (x y theta) : 50 100 0
        Enter end state (x y) : 300 180
        Enter clearance (clearance) : 5
        Enter RPM1 and RPM2 (RPM1, RPM2) : 30 60

        Starting search...

        Found path in 1.832632303237915 seconds.
        Distance from state to goal :  3.4211943997592833
        Final node in the path : [299.95249664 181.2539106   65.34      ]
        Number of nodes explored : 1829
        ```
    - The animation video link is [here](https://drive.google.com/drive/folders/19rUXHqT4XGNATDRHBpmevm8oGCOTXusi?usp=sharing).

* **ROS**
    - The outputs is as shown below:
        ```
        Enter start state (x y theta) : 50 100 0
        Enter end state (x y) : 550 100
        Enter clearance (clearance) : 5
        Enter RPM1 and RPM2 (RPM1, RPM2) : 50 100

        Starting search...

        Found path in 0.5591976642608643 seconds.
        Distance from state to goal :  6.4622560884342075
        Final node in the path : [549.42340336 100.48810098 251.1       ]
        Number of nodes explored : 593
        ```

