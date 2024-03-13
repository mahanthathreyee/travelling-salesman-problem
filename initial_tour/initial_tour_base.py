from abc import ABC

from model.node import Node

class InitialTourBase(ABC):
    NAME: str = None

    n_cities: int = None
    city_graph: list[Node] = None

    def __init__(self, n_cities: int, city_graph: list[Node]) -> None:
        super().__init__()

        self.n_cities = n_cities
        self.city_graph = city_graph

    def get_name(self) -> str:
        return self.NAME
    
    def create_initial_tour(self, source_id: int) -> list[int]:
        pass
