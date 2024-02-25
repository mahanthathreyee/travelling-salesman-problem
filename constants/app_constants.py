from algorithms.algorithm_base import AlgorithmBase
from algorithms.impl.a_star import AStar

from heuristics.heuristic_base import HeuristicBase
from heuristics.impl.zero import Zero
from heuristics.impl.prims_mst import PrimsMMST

INFINITY = float('inf')

DEFAULT_INPUT_FILE = './data/input/tsp-problem-10-30-75-25-3.txt'

ALGORITHMS: dict[str, AlgorithmBase] = {
    'a_star': AStar
}

HEURISTICS: dict[str, HeuristicBase] = {
    'zero': Zero,
    'prims_mst': PrimsMMST
}
