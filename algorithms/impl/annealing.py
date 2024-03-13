import heapq
from typing import Any
from initial_tour.initial_tour_base import InitialTourBase

from model.node import Node
from model.state import State
from algorithms.algorithm_base import AlgorithmBase

from heuristics.heuristic_base import HeuristicBase
from neighbor_tour.neighbor_tour_base import NeighborTourBase

class AdaptiveSimulatedAnnealing(AlgorithmBase):
    NAME: str = 'Adaptive Simulated Annealing'
    result: State = None

    initial_tour: InitialTourBase = None
    neighbor_tour: NeighborTourBase = None
    alpha: float = None
    final_threshold: float = None

    def __init__(self, n_cities: int, city_graph: list[Node], metadata: dict[str, Any]) -> None:
        super().__init__(n_cities, city_graph, metadata)

        if 'initial_tour' not in self.metadata:
            raise ValueError('Initial Tour not provided')
        self.initial_tour = self.metadata['initial_tour']

        if 'neighbor_tour' not in self.metadata:
            raise ValueError('Neighbor Tour not provided')
        self.neighbor_tour = self.metadata['neighbor_tour']

        if 'alpha' not in self.metadata:
            raise ValueError('Alpha not provided')
        self.alpha = self.metadata['alpha']

        if 'threshold' not in self.metadata:
            raise ValueError('Final Threshold not provided')
        self.final_threshold = self.metadata['threshold']
    
    def compute_tour(self, source_id: int, n_cities: int, city_graph: list[Node]) -> State:
        tour = self.initial_tour.create_initial_tour(
            source_id=source_id
        )

        current_state = State(
            source_id=source_id,
            n_cities=self.n_cities,
            branch_state=True
        )
        current_state.path = tour
        current_state.tour_cost = self.compute_tour_cost(current_state.path)
        current_state.cost = current_state.tour_cost

        current_threshold = 10

        while current_threshold > self.final_threshold:
            new_state = self.neighbor_tour.generate_neighbor_tour(
                current_state=current_state
            )
            new_state.tour_cost = self.compute_tour_cost(new_state.path)
            new_state.cost = new_state.tour_cost

            if new_state < current_state:
                current_state = new_state

            current_threshold = current_threshold * self.alpha
        
        return current_state

    def compute_tour_cost(self, tour: list[int]) -> float:
        tour_cost: float = 0
        
        for node_i_id, node_j_id in zip(tour, tour[1:]):
            tour_cost += self.city_graph[node_i_id].neighbors[node_j_id].weight

        return tour_cost

    def execute(self):
        source_id = self.metadata['source_id']
        
        self.result = self.compute_tour(
            source_id=source_id,
            n_cities=self.n_cities,
            city_graph=self.city_graph
        )

    def getTour(self) -> str:
        return ' -> '.join(map(str, self.result.path))

    def getCost(self) -> float:
        return self.result.tour_cost
        
    def getMetadata(self) -> str:
        return {
            "initial_tour": self.initial_tour.get_name(),
            "neighbor_tour": self.neighbor_tour.get_name(),
            "alpha": self.alpha,
            "final_threshold": self.final_threshold
        }
