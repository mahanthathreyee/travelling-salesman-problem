from heuristics.heuristic_base import HeuristicBase

class Zero(HeuristicBase):
    NAME: str = 'Zero Heuristic'

    def compute_cost(self, source_id: int, start_id: int, unmarked_nodes: set[int]) -> float:
        return 0