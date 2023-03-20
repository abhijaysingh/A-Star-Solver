import time
import numpy as np
from map import Map
from node import Node, ActionSet
from solver import AStarSolver
from visualizer import Visualizer
import readline

def main():
    map = Map(width=600, height=250)

    while True:
        try:
            s_x, s_y, s_theta = input("\nEnter start state (x y theta) : ").split()
            x, y, theta = input("Enter end state (x y theta) : ").split()

            clearance, radius = input("Enter clearance and radius (clearance, radius) : ").split()
            map.set_clearance_radius(int(clearance), int(radius))

            step_size = int(input("Enter step size [1-10] : "))
            action_set = ActionSet(step_size)
            Node.set_resolution((0.5, 0.5, 30))
            Node.set_actionset(action_set)

            start = Node((int(s_x), int(s_y), int(s_theta)), 0, None)
            end = Node((int(x), int(y), int(theta)), np.inf, None)

            if map.is_valid(start) and map.is_valid(end):
                print("\nStarting search...")
                break
            
            print("\nStart or end state is in obstacle. Try again.")
        except Exception:
            print("\nIncorrect input format. Try again.")
            continue

    solver = AStarSolver(start, end, map)
    start_time = time.time()
    path = solver.solve()
    end_time = time.time()

    print(f"\nFound path in {end_time - start_time} seconds.")
    print("Distance from state to goal : ", path[-1].cost_to_come)

    nodes = solver.get_explored_nodes()
    print(f"Final node in the path : {path[-1].state[:2]}")
    print(f"Number of nodes explored : {len(nodes)}")

    visualizer = Visualizer(map, path, nodes)
    # visualizer.plot(step_size=200)
    visualizer.record_opencv(map, step_size=1, record=False)

if __name__ == "__main__":

    """
        Github link: https://github.com/abhijaysingh/ENPM661-Project-3
    
    """
    main()