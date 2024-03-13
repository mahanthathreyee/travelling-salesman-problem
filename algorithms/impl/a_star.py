import heapq
from typing import Any

from constants import app_constants

from model.node import Node
from model.state import State

from algorithms.algorithm_base import AlgorithmBase
from heuristics.heuristic_base import HeuristicBase

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
        state_space: list[State] = []

        initial_state = State(
            source_id=source_id,
            n_cities=self.n_cities
        )
        heapq.heappush(state_space, initial_state)

        while state_space:
            current_state = heapq.heappop(state_space)

            if not current_state.unvisited:
                return current_state
            
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

                heapq.heappush(state_space, new_state)

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
