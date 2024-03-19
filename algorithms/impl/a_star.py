import heapq
from typing import Any

from constants import app_constants

from model.node import Node
from model.state import State

from algorithms.algorithm_base import AlgorithmBase
from heuristics.heuristic_base import HeuristicBase
from initial_tour.impl.greedy_initial import GreedyInitialTour

class AStar(AlgorithmBase):
    NAME: str = 'A Star'
    result: State = None
    heuristic: HeuristicBase = None

    def __init__(self, n_cities: int, city_graph: list[Node], metadata: dict[str, Any]) -> None:
        super().__init__(n_cities, city_graph, metadata)

        if app_constants.METADATA_HEURISTIC not in self.metadata:
            raise ValueError('Heuristic not provided')
        self.heuristic = self.metadata[app_constants.METADATA_HEURISTIC]
    
    def compute_tour(self, source_id: int) -> State:
        current_longest_path = 0
        best_state: State = None
        state_space: list[State] = []

        global_minimum_cost = self.compute_initial_tour_cost(source_id=source_id)

        initial_state = State(
            source_id=source_id,
            n_cities=self.n_cities
        )
        heapq.heappush(state_space, initial_state)

        while state_space:
            current_state = heapq.heappop(state_space)

            if not current_state.unvisited:
                # All nodes have been visited
                if current_state.cost < global_minimum_cost:
                    global_minimum_cost = current_state.cost
                    best_state = current_state
            
            for neighbor_id in current_state.unvisited:
                neighbor_path = self.city_graph[current_state.current_city_id].neighbors[neighbor_id]
                
                heuristic_cost = self.heuristic.compute_cost(
                    source_id=neighbor_id,
                    start_id=source_id,
                    unmarked_nodes=current_state.unvisited
                )
                new_cost = current_state.cost + neighbor_path.weight + heuristic_cost

                new_state = current_state.construct_new_state(
                    neighbor_id=neighbor_id,
                    cost=new_cost,
                    tour_cost=neighbor_path.weight
                )

                if new_state.cost < global_minimum_cost:
                    heapq.heappush(state_space, new_state)

                if len(new_state.path) > current_longest_path:
                    current_longest_path = len(new_state.path)
                    print(f'Current Path Length: {current_longest_path} of {self.n_cities} | State Space Size: {len(state_space)}')

        return best_state
    
    def compute_initial_tour_cost(self, source_id: int) -> float:
        initial_tour = GreedyInitialTour(
            n_cities=self.n_cities,
            city_graph=self.city_graph
        )
        tour = initial_tour.create_initial_tour(source_id=source_id)

        tour_cost: float = 0
        for node_i_id, node_j_id in zip(tour, tour[1:]):
            tour_cost += self.city_graph[node_i_id].neighbors[node_j_id].weight

        return tour_cost

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
        return self.heuristic.get_name()
