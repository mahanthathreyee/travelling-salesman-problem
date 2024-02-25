from abc import ABC
from typing import Any

from model.node import Node

class AlgorithmBase(ABC):
    NAME = None
    
    n_cities: int = 0
    city_graph: list[Node] = None

    metadata: dict[str, Any]
    
    def __init__(self, n_cities: int, city_graph: list[Node], metadata: dict[str, Any]) -> None:
        self.n_cities = n_cities
        self.city_graph = city_graph
        self.metadata = metadata

    def getName(self):
        return self.NAME
    
    def execute(self):
        pass

    def getTour(self) -> str:
        pass

    def getCost(self) -> float:
        pass

    def getMetadata(self) -> str:
        pass
