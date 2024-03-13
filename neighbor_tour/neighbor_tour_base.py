from abc import ABC

from model.node import Node
from model.state import State

class NeighborTourBase(ABC):
    NAME: str = None

    n_cities: int = None
    city_graph: list[Node] = None

    def __init__(self, n_cities: int, city_graph: list[Node]) -> None:
        super().__init__()

        self.n_cities = n_cities
        self.city_graph = city_graph

    def get_name(self) -> str:
        return self.NAME
    
    def generate_neighbor_tour(self, current_state: State) -> State:
        pass
