import heapq
from argparse import Namespace

from model.node import Node
from model.state import State
from algorithms.algorithm_base import AlgorithmBase

from heuristics import heuristic_factory
from heuristics.heuristic_base import HeuristicBase

class AStar(AlgorithmBase):
    NAME: str = 'Dijikstra based TSP'
    result: State = None
    heuristic: HeuristicBase = None

    def __init__(self, args: Namespace, n_cities: int, city_graph: list[Node]) -> None:
        super().__init__(args, n_cities, city_graph)
        
        self.heuristic = heuristic_factory.get_heuristic(self.args.heuristic)
        self.heuristic = self.heuristic()
    
    def compute_tour(self, source_id: int, n_cities: int, city_graph: list[Node]) -> State:
        state_space: list[State] = []

        initial_state = State(
            source_id=source_id,
            n_cities=n_cities
        )
        heapq.heappush(state_space, initial_state)

        while state_space:
            current_state = heapq.heappop(state_space)

            if not current_state.unvisited:
                return current_state
            
            for neighbor_id in current_state.unvisited:
                neighbor_path = city_graph[current_state.current_city_id].neighbors[neighbor_id]
                
                heuristic_cost = self.heuristic.compute_cost(current_state.current_city_id, neighbor_id)
                new_cost = current_state.cost + neighbor_path.weight + heuristic_cost

                new_state = current_state.construct_new_state(
                    neighbor_id=neighbor_id,
                    cost=new_cost
                )

                heapq.heappush(state_space, new_state)

    def execute(self):
        source_id = self.args.source_id
        
        self.result = AStar.compute_tour(
            self,
            source_id=source_id,
            n_cities=self.n_cities,
            city_graph=self.city_graph
        )

    def getTour(self) -> str:
        return ' -> '.join(map(str, self.result.path))

    def getCost(self) -> float:
        return self.result.cost
        