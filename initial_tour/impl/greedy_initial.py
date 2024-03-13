import heapq
from constants import app_constants

from model.edge import Edge
from model.node import Node

from initial_tour.initial_tour_base import InitialTourBase

class GreedyInitialTour(InitialTourBase):
    NAME: str = 'Greedy Initial Tour'

    def create_initial_tour(self, source_id: int) -> list[int]:
        path = [source_id]
        visited = set(path)

        while len(path) < self.n_cities:
            current_node = self.city_graph[path[-1]]

            min_next_node_weight = app_constants.INFINITY
            min_next_node_id = -1

            for neighbor_path in current_node.neighbors:
                if neighbor_path.destination_id not in visited:
                    if neighbor_path.weight < min_next_node_weight:
                        min_next_node_weight = neighbor_path.weight
                        min_next_node_id = neighbor_path.destination_id
            
            if min_next_node_id == -1:
                break

            path += [min_next_node_id]
            visited.add(min_next_node_id)

        return path
