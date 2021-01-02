#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import random
import timeit
import os
import csv
from typing import List

from helper import City, hill_climb


def hill_climb_simple(cities: List[City]):
    """Implements the simple and steepest hillclimb algorithm.

    Args:
        cities (List[City]): List of cities with coordinates as Longitude and Latitude
        iterations (int, optional): Explorations of the problem space done before restarting. Defaults to 2000.
        restarts (int, optional): How many times to start from a random configuration. Defaults to 5.
        explore_space (int, optional): Number of successors to generate from the problem space. Defaults to 100.
        steepest_hill (bool, optional): If True, all generated successor are evaluated. For False the first successor decreasing distance gets chosen. Defaults to False.
        generate_report (bool, optional): If True returns metrics needed for plotting. Defaults to False.

    Returns:
        [type]: [description]
    """

    shortest_distance, shortest_sequence, _ = hill_climb(cities)

    return shortest_distance, shortest_sequence


if __name__ == '__main__':

    # Reading txt file path from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()

    working_directory = os.path.dirname(os.path.realpath(__file__))

    if args.filename:
        file_name = args.filename
    else:
        file_name = "data/cities_full.txt"

    file_path = os.path.join(working_directory, file_name)

    with open(file_path) as file:
        reader = csv.DictReader(file)
        cities = [City(row["name"], row["longitude"], row["latitude"]) for row in reader]

    print(f"Found {len(cities)} in {file_name}. Example: {cities[0]}")

    start_time = timeit.default_timer()

    least_distance, best_seq = hill_climb_simple(cities)

    end_time = timeit.default_timer()

    print("Best Sequence:", best_seq)
    print("Best Sequence:", " -> ".join([cities[i].name for i in best_seq]))
    print("Least distance from Simple hill climbing:", least_distance)
    print("Time: {}".format(end_time - start_time))
