#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:04:22 2018

@author: iswariya
"""
from helper import City, hill_climb
from typing import List
import csv
import argparse
import os
import random
import timeit


def hill_climb_steepest_descent(cities: List[City]) -> tuple:
    """Implements the steepest hillclimb algorithm."""

    shortest_distance, shortest_sequence, _ = hill_climb(cities, steepest_hill=True)
    return shortest_distance, shortest_sequence


if __name__ == '__main__':

    # Reading txt file path from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str, default="data/49_cities.txt")
    args = parser.parse_args()

    working_directory = os.path.dirname(os.path.realpath(__file__))

    file_path = os.path.join(working_directory, args.filename)

    with open(file_path) as file:
        reader = csv.DictReader(file)
        cities = [City(row["name"], row["longitude"], row["latitude"]) for row in reader]

    print(f"Found {len(cities)} in {args.filename}. Example: {cities[0]}")

    start_time = timeit.default_timer()
    least_distance, best_seq = hill_climb_steepest_descent(cities)
    end_time = timeit.default_timer()

    print("Best Sequence:", best_seq)
    print("Best Sequence:", " -> ".join([cities[i].name for i in best_seq]))
    print("Least distance from Steepest hill climbing:", least_distance)
    print("Time: {}".format(end_time - start_time))
