import math
import random
from typing import Any

from constants import app_constants

from model.node import Node
from model.state import State

from algorithms.algorithm_base import AlgorithmBase
from initial_tour.initial_tour_base import InitialTourBase
from neighbor_tour.neighbor_tour_base import NeighborTourBase

class AdaptiveSimulatedAnnealing(AlgorithmBase):
    NAME: str = 'Adaptive Simulated Annealing'
    result: State = None

    initial_tour: InitialTourBase = None
    neighbor_tour: NeighborTourBase = None
    alpha: float = None
    alpha_factor: float = None
    initial_threshold: float = None
    final_threshold: float = None

    def __init__(self, n_cities: int, city_graph: list[Node], metadata: dict[str, Any]) -> None:
        super().__init__(n_cities, city_graph, metadata)

        if app_constants.METADATA_INITIAL_TOUR not in self.metadata:
            raise ValueError('Initial Tour not provided')
        self.initial_tour = self.metadata[app_constants.METADATA_INITIAL_TOUR]

        if app_constants.METADATA_NEIGHBOR_TOUR not in self.metadata:
            raise ValueError('Neighbor Tour not provided')
        self.neighbor_tour = self.metadata[app_constants.METADATA_NEIGHBOR_TOUR]

        if app_constants.METADATA_ALPHA not in self.metadata:
            raise ValueError('Alpha not provided')
        self.alpha = self.metadata[app_constants.METADATA_ALPHA]
        
        if app_constants.METADATA_ALPHA_FACTOR not in self.metadata:
            raise ValueError('Alpha adaptive factor not provided')
        self.alpha_factor = self.metadata[app_constants.METADATA_ALPHA_FACTOR]

        if app_constants.METADATA_INITIAL_THRESHOLD not in self.metadata:
            raise ValueError('Initial Threshold not provided')
        self.initial_threshold = self.metadata[app_constants.METADATA_INITIAL_THRESHOLD]

        if app_constants.METADATA_FINAL_THRESHOLD not in self.metadata:
            raise ValueError('Final Threshold not provided')
        self.final_threshold = self.metadata[app_constants.METADATA_FINAL_THRESHOLD]
    
    def compute_tour(self, source_id: int) -> State:
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

        current_threshold = self.initial_threshold
        current_iteration = 0

        while current_threshold > self.final_threshold and current_iteration < app_constants.DEFAULT_MAX_ITERATIONS:
            new_state = self.neighbor_tour.generate_neighbor_tour(
                current_state=current_state
            )
            new_state.tour_cost = self.compute_tour_cost(new_state.path)
            new_state.cost = new_state.tour_cost

            self.adapt_cooling_rate(
                current_state=current_state,
                new_state=new_state
            )

            if new_state < current_state or self.compute_acceptance_probability(current_threshold, current_state, new_state):
                current_state = new_state

            current_threshold = current_threshold * self.alpha
            current_iteration += 1
        
        return current_state

    def compute_tour_cost(self, tour: list[int]) -> float:
        tour_cost: float = 0
        
        for node_i_id, node_j_id in zip(tour, tour[1:]):
            tour_cost += self.city_graph[node_i_id].neighbors[node_j_id].weight

        return tour_cost
    
    def compute_acceptance_probability(self, current_threshold: float, current_state: State, new_sate: State):
        minimum_random_chance = random.random()

        try:
            acceptance_probability = 1 / math.exp(
                (new_sate.cost - current_state.cost) / current_threshold
            )
        except OverflowError:
            # In case  the exponential value is very high then acceptance probability is 0
            acceptance_probability = 0
        # print(f'Chance: {minimum_random_chance} | Acp: {acceptance_probability} | C: {new_sate.cost - current_state.cost} | T: {current_threshold}')

        return acceptance_probability > minimum_random_chance

    def adapt_cooling_rate(self, current_state: State, new_state: State):
        if new_state < current_state:
            self.alpha *= 1 + self.alpha_factor
        else:
            self.alpha *= 1 - self.alpha_factor


    def execute(self):
        source_id = self.metadata[app_constants.METADATA_SOURCE_ID]
        
        self.result = self.compute_tour(
            source_id=source_id
        )

    def getTour(self) -> str:
        return ' -> '.join(map(str, self.result.path))

    def getCost(self) -> float:
        return self.result.tour_cost
        
    def getMetadata(self) -> str:
        return {
            'initial_tour': self.initial_tour.get_name(),
            'neighbor_tour': self.neighbor_tour.get_name(),
            'alpha': self.alpha,
            'alpha_factor': self.alpha_factor,
            'initial_threshold': self.initial_threshold,
            'final_threshold': self.final_threshold
        }
