import copy
import math
import random
from typing import List
from math import sqrt


class City():
    def __init__(self, name: str, longitude: float, latitude: float):
        self.name = name
        self.longitude = float(longitude)
        self.latitude = float(latitude)

    def get_distance_to(self, other_city) -> float:
        """Calculates euclidean distance

        Args:
            other_city (City): Other city object to calculate the distance to.

        Returns:
            float: [description]
        """

        return sqrt((self.longitude - other_city.longitude)**2 + (self.latitude - other_city.latitude)**2)

    def __repr__(self) -> str:
        return f"City({self.name} {self.longitude} {self.latitude})"


def calculate_distance_matrix(cities: List[City]) -> List[List[float]]:
    """Returns NxN matrix filled with euclidean distances between N given cities.

    Args:
        cities (List[City]): List of City Objects

    Returns:
        List[List[float]]: Euclidean distance matrix
    """

    # creates square matrix with place for all distances
    results = [[float('inf') for _ in range(len(cities))] for _ in range(len(cities))]

    for base_index, base_city in enumerate(cities):
        for comparison_index, comparison_city in enumerate(cities):
            if base_index == comparison_index:
                continue
            results[base_index][comparison_index] = base_city.get_distance_to(comparison_city)

    return results


def calculate_total_distance(sequence: List[int], distance_matrix: List[List[float]]) -> float:
    """Looks up the distances and sums them.

    Args:
        sequence (List[int]): The list containing the indexes of cities
        distance_matrix (List[List[float]]): Euclidean distance matrix

    Returns:
        float: Sum of distances
    """
    total_distance = 0
    for i in range(len(sequence)-1):
        total_distance += distance_matrix[sequence[i]][sequence[i+1]]

    return total_distance


def pre_sort_sequence(sequence: List[int], distance_matrix: List[List[float]]) -> List[int]:
    """Makes on pass swapping cities for the shortest distance (just a bad sorting algo with O(n^2))

    Args:
        sequence (List[int]): The list containing the indexes of cities
        distance_matrix (List[List[float]]): [description]

    Returns:
        List[int]: The list containing the indexes of cities but sorted
    """

    working_sequence = [index for index in sequence]

    for index_current_city in range(len(working_sequence)-2):
        current_city = working_sequence[index_current_city]
        next_city = working_sequence[index_current_city+1]

        unsorted_cities = working_sequence[index_current_city+1:len(working_sequence)-1]

        min_distance = distance_matrix[current_city][unsorted_cities[0]]
        nearest_city = next_city

        for unsorted in unsorted_cities:
            if min_distance > distance_matrix[current_city][unsorted]:
                min_distance = distance_matrix[current_city][unsorted]
                nearest_city = unsorted

        index_nearest_city = working_sequence.index(nearest_city)

        # swap the best with the current next city
        working_sequence[index_current_city+1] = working_sequence[index_nearest_city]
        working_sequence[index_nearest_city] = next_city

    return working_sequence


def generate_successors(sequence: List[int], *, random_steps: int = 1) -> List[int]:
    """Generator function exporing the problem space by randomly swapping to cities.

    Args:
        sequence (List[int]): The list containing the indexes of cities

    Yields:
        Iterator[List[int]]: Same list but two cities swapped
    """

    while True:
        permutation = [entry for entry in sequence]

        for _ in range(random.randint(1, random_steps)):
            index_2 = index_1 = random.randint(1, len(sequence)-2)

            while index_1 == index_2:
                index_2 = random.randint(1, len(sequence)-2)

            permutation[index_1], permutation[index_2] = permutation[index_2], permutation[index_1]

        yield permutation


\def hill_climb(
        cities: List[City],
        *, iterations: int = 2000, restarts: int = 5, explore_space: int = 100, steepest_hill: bool = False,
        generate_report: bool = False, pre_sort: bool = False, random_steps: int = 1):
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

    best_cost = float('inf')
    best_seq = None
    distances = []
    seen_states = []

    distance_matrix = calculate_distance_matrix(cities)

    for _ in range(restarts):

        start_sequence = random.sample(range(0, len(cities)), len(cities))
        start_sequence.append(start_sequence[0])

        if pre_sort:
            start_sequence = pre_sort_sequence(start_sequence, distance_matrix)

        current_distance = calculate_total_distance(start_sequence, distance_matrix)
        distances.append(current_distance)

        for __ in range(iterations):
            successor_count = 0

            # I do not want to generate 100 successors if i do not have to.
            # So I use a generator to create them on the fly
            for successor in generate_successors(start_sequence, random_steps=random_steps):
                if successor_count > explore_space:
                    break

                successor_count += 1
                new_distance = calculate_total_distance(successor, distance_matrix)

                if new_distance < current_distance:
                    start_sequence = successor
                    current_distance = new_distance

                    if not steepest_hill:
                        break

            if generate_report:
                distances.append(current_distance)

        seen_states.append((current_distance, start_sequence))

    seen_states.sort(key=lambda x: x[0])

    print(len(distances))

    return seen_states[0][0], seen_states[0][1], distances
