from argparse import Namespace
import heapq

from model.node import Node
from model.state import State
from algorithms.algorithm_base import AlgorithmBase

class DijikstraTSP(AlgorithmBase):
    NAME: str = 'Dijikstra based TSP'
    result: State = None
    
    def compute_tour(source_id: int, n_cities: int, city_graph: list[Node]) -> State:
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
                
                new_cost = current_state.cost + neighbor_path.weight
                new_state = current_state.construct_new_state(
                    neighbor_id=neighbor_id,
                    cost=new_cost
                )

                heapq.heappush(state_space, new_state)

    def execute(self):
        source_id = self.args.source_id
        
        self.result = DijikstraTSP.compute_tour(
            source_id=source_id,
            n_cities=self.n_cities,
            city_graph=self.city_graph
        )

    def getTour(self) -> str:
        return ' -> '.join(map(str, self.result.path))

    def getCost(self) -> float:
        return self.result.cost
        