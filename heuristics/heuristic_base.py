from abc import ABC
from argparse import Namespace

class HeuristicBase(ABC):
    NAME: str = None
    args: Namespace = None

    def __init__(self) -> None:
        super().__init__()

    def get_name(self) -> str:
        return self.NAME
    
    def compute_cost(self, source_id: int, destination_id: int) -> float:
        pass
