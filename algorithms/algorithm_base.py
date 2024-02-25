from abc import ABC
from argparse import Namespace

from model.node import Node

class AlgorithmBase(ABC):
    NAME = None
    args: Namespace = None
    
    n_cities: int = 0
    city_graph: list[Node] = None
    
    def __init__(self, args: Namespace, n_cities: int, city_graph: list[Node]) -> None:
        self.args = args
        self.n_cities = n_cities
        self.city_graph = city_graph

    def getName(self):
        return self.NAME
    
    def execute(self):
        pass

    def getTour(self) -> str:
        pass

    def getCost(self) -> float:
        pass
