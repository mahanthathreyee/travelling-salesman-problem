from heuristics.heuristic_base import HeuristicBase

class Zero(HeuristicBase):
    NAME: str = 'Zero Heuristic'

    def compute_cost(self, _source_id: int, _destination_id: int) -> float:
        return 0