from abc import ABC
from argparse import Namespace

from model.node import Node

class HeuristicBase(ABC):
    NAME: str = None
    args: Namespace = None
    cache: dict[frozenset, float] = {}

    n_cities: int = None
    city_graph: list[Node] = None

    def __init__(self, n_cities: int, city_graph: list[Node]) -> None:
        super().__init__()

        self.n_cities = n_cities
        self.city_graph = city_graph

    def get_name(self) -> str:
        return self.NAME
    
    def compute_cost(self, source_id: int, start_id: int, unmarked_nodes: set[int]) -> float:
        pass
