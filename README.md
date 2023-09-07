# A* Solver

## Setup

To install the dependencies, run the following commands in the terminal:
```bash
pip3 install -r requirements.txt
```

## Usage

    
- To execute the program for this problem, navigate to the project folder and use the following commands
        ```bash
        cd <path_to_project>/code/
        python3 main.py
        ```

- Once you run the program, enter the start and goal states in the format shown below:
    ```bash
    Enter start state (x y theta) : 125 125 0
    Enter end state (x y theta) : 11 11 0
    Enter clearance and radius (clearance, radius) : 5 5
    Enter step size [1-10] : 10
    ```

- Each line of input should be in the format `x y theta` where `x`, `y` and `theta` are the x and y coordinates of the point and theta is the orientation of the robot respectively.
    
- The program will not run if only one of the coordinates is entered or if the coordinates are not integers.
    
- The program will not run if the clearance and radius are not entered in the format `clearance, radius`.
    

## Results
    
- The outputs is as shown below:
    ```
    Enter start state (x y theta) : 125 125 0
    Enter end state (x y theta) : 11 11 0
    Enter clearance and radius (clearance, radius) : 5 5
    Enter step size [1-10] : 10
    
    Starting search...
    
    Found path in 0.4900341033935547 seconds.
    Distance from state to goal :  230
    Final node in the path : [10.35898385  11.07695155   240.]
    Number of nodes explored : 4162
    ```
    
- The animation video link - [Videos](https://drive.google.com/drive/folders/10thXvk4uNb31oMe0pjVKG6o6Dnd6WHWf?usp=share_link)