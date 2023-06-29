# A* Solver

## Team

* Abhijay Singh (UID - 118592619)
* Tharun Puthanveettil (UID - 119069516)

## Dependencies

* python3 interpreter
* Python packages - numpy, time, matplotlib, copy, math, collections, queue, opencv, readline

## Execution

* **A\* Solver** 
    
    - To execute the program for this problem, navigate to the submission folder and use the following commands
        ```
        cd <path_to_submission>/code/
        python3 a_star_Abhijay_Tharun.py
        ```

    - Once you run the program, enter the start and goal states in the format shown below:
        ```
        Enter start state (x y theta) : 125 125 0
        Enter end state (x y theta) : 11 11 0
        Enter clearance and radius (clearance, radius) : 5 5
        Enter step size [1-10] : 10
        ```

    - Each line of input should be in the format `x y theta` where `x`, `y` and `theta` are the x and y coordinates of the point and theta is the orientation of the robot respectively.
    
    - The program will not run if only one of the coordinates is entered or if the coordinates are not integers.
    
    - The program will not run if the clearance and radius are not entered in the format `clearance, radius`.

    - Since the quiver plot in matplotlib is not very efficient, the animation can be played in three ways.
        - The first method is using OpenCV. Please use the function in `line 51` of the `a_star_Abhijay_Tharun.py` file. (**Suggested method**) To record the animation, please set the `record` variable to `True` in the `visualizer.record_opencv()` function in the `a_star_Abhijay_Tharun.py` file (line **51**).
        - The second method is using matplotlib scatter plot. Please use the function in `line 50` of the `a_star_Abhijay_Tharun.py` file.
        - The third method is using matplotlib quiver plot. Please uncomment `lines 99-103` and comment `lines 103-104` in the `visualizer.py` file. (**Not recommended**)

    - To increase the speed of the animation, change the value of `step_size` in the `visualizer.plot()` and `visualizer.record_opencv()` functions in the `a_star_Abhijay_Tharun.py` file (lines **50/51**).
    

## Results
* **A\* Solver** 
    
    - The outputs is as shown below:
        ```
        Enter start state (x y theta) : 125 125 0
        Enter end state (x y theta) : 11 11 0
        Enter clearance and radius (clearance, radius) : 5 5
        Enter step size [1-10] : 10

        Starting search...

        Found path in 1.2484350204467773 seconds.
        Distance from state to goal :  180
        Final node in the path : [11.02885683 10.89745962]
        Number of nodes explored : 10460
        ```
    
    - The animation video link - [Videos](https://drive.google.com/drive/folders/10thXvk4uNb31oMe0pjVKG6o6Dnd6WHWf?usp=share_link)

## Help
For any assistance with executing the programs or questions related to them, please reach out to us at abhijay@umd.edu or tvpian@umd.edu.
