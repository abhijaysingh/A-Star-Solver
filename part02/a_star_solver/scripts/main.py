#!/usr/bin/env python3

import time
import numpy as np
from map import Map
from node import Node, ActionSet
from solver import AStarSolver
from ros_publisher import ROSPublisher
import readline
import rospy
import pandas as pd

def main():
    map = Map(width=600, height=200)

    while True:
        try:
            s_x, s_y, s_theta = input("\nEnter start state (x y theta) : ").split()
            if float(s_x) < 0 or float(s_y) < 0 or float(s_theta) < 0:
                print("\nStart state must be non-negative. Try again.")
                continue
            x, y = input("Enter end state (x y) : ").split()
            if float(x) < 0 or float(y) < 0:
                print("\nEnd state must be non-negative. Try again.")
                continue

            clearance = input("Enter clearance in cms (clearance - whole number) : ")
            if int(clearance) < 0:
                print("\nClearance must be non-negative. Try again.")
                continue
            map.set_clearance_radius(int(clearance))

            RPM1, RPM2 = input("Enter RPM1 and RPM2 (RPM1 RPM2) : ").split()
            if int(RPM1) < 0 or int(RPM2) < 0:
                print("\nRPM1 and RPM2 must be non-negative. Try again.")
                continue
            RPM1 = 2 * np.pi * int(RPM1) / 60
            RPM2 = 2 * np.pi * int(RPM2) / 60
            action_set = ActionSet(RPM1=RPM1, RPM2=RPM2, map=map)
            Node.set_resolution((1, 1, 30))
            Node.set_actionset(action_set)

            s_x = (float(s_x) * 100) + 50
            s_y = (float(s_y) * 100) + 100
            start = Node((s_x, s_y, int(s_theta)), 0, None)
            x = (float(x) * 100) + 50
            y = (float(y) * 100) + 100
            end = Node((x, y, 0), np.inf, None)

            if map.is_valid(start.state[0], start.state[1]) and map.is_valid(end.state[0], end.state[1]):
                print("\nStarting search...")
                break
            
            print("\nStart or end state is in obstacle. Try again.")
        except Exception:
            print("\nIncorrect input format. Try again.")
            continue

    solver = AStarSolver(start, end, map)
    start_time = time.perf_counter()
    path = solver.solve()
    end_time = time.perf_counter()

    if path is None:
        print("\nNo path found.")
        return

    print(f"\nFound path in {end_time - start_time} seconds.")
    print("Distance from state to goal : ", path[-1].cost_to_come / 100)

    nodes = solver.get_explored_nodes()
    print(f"Final node in the path : {path[-1].state}")
    print(f"Number of nodes explored : {len(nodes)}")

    publisher = ROSPublisher(action_set.r, action_set.l)

    while not rospy.is_shutdown():
        for node in path:
            if node.parent_action is None:
                continue
            vel_mag, theta_dot = publisher.vel_calc(node.state[2], node.parent_action[0], node.parent_action[1])
            publisher.twist.linear.x = vel_mag/100
            publisher.twist.angular.z = theta_dot
            publisher.vel_pub.publish(publisher.twist)
            publisher.rate.sleep()

            if node == path[-1]:
                publisher.twist.linear.x = 0
                publisher.twist.angular.z = 0
                publisher.vel_pub.publish(publisher.twist)
                break
            time.sleep(1)

        break


if __name__ == "__main__":
    main()