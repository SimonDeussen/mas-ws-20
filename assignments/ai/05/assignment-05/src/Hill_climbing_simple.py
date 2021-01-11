#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import random
import timeit
import os
import csv
from typing import List

from helper import City, hill_climb


def hill_climb_simple(cities: List[City]) -> tuple:
    """Implements the simple hill climbing algorithm."""

    shortest_distance, shortest_sequence, _ = hill_climb(cities)
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

    print(f"Found {len(cities)} in { args.filename}. Example: {cities[0]}")

    start_time = timeit.default_timer()
    least_distance, best_seq = hill_climb_simple(cities)
    end_time = timeit.default_timer()

    print("Best Sequence:", best_seq)
    print("Best Sequence:", " -> ".join([cities[i].name for i in best_seq]))
    print("Least distance from Simple hill climbing:", least_distance)
    print("Time: {}".format(end_time - start_time))
