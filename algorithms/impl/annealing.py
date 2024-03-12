import heapq
from typing import Any

from model.node import Node
from model.state import State
from algorithms.algorithm_base import AlgorithmBase

from heuristics.heuristic_base import HeuristicBase

class AdaptiveSimulatedAnnealing(AlgorithmBase):
    NAME: str = 'A Star'
    result: State = None
    heuristic: HeuristicBase = None

    def __init__(self, n_cities: int, city_graph: list[Node], metadata: dict[str, Any]) -> None:
        super().__init__(n_cities, city_graph, metadata)

        if 'heuristic' not in self.metadata:
            raise ValueError('Heuristic not provided')
        self.heuristic = self.metadata['heuristic']
    
    def compute_tour(self, source_id: int, n_cities: int, city_graph: list[Node]) -> State:
        

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
        return self.heuristic.get_name()
