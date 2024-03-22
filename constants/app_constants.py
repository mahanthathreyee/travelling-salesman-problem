from algorithms.impl.a_star import AStar
from algorithms.algorithm_base import AlgorithmBase
from algorithms.impl.annealing import AdaptiveSimulatedAnnealing

from heuristics.impl.zero import Zero
from heuristics.impl.prims_mst import PrimsMST
from heuristics.heuristic_base import HeuristicBase

from initial_tour.initial_tour_base import InitialTourBase
from initial_tour.impl.greedy_initial import GreedyInitialTour
from neighbor_tour.impl.insertion import InsertionNeighborTour
from initial_tour.impl.insertion_initial import InsertionInitialTour

from neighbor_tour.impl.two_opt import TwoOptNeighborTour
from neighbor_tour.impl.swap_neigbor import SwapNeighborTour
from neighbor_tour.neighbor_tour_base import NeighborTourBase

INFINITY = float('inf')

DEFAULT_RANDOM_SEED = 1234
DEFAULT_INPUT_FILE = './data/input/tsp-problem-10-30-75-25-3.txt'
DEFAULT_MAX_ITERATIONS = 1_000_000

HEURISTIC_ALGORITHM = 'a_star'
SLS_ALGORITHM = 'sa'
ALGORITHMS: dict[str, AlgorithmBase] = {
    HEURISTIC_ALGORITHM: AStar,
    SLS_ALGORITHM: AdaptiveSimulatedAnnealing
}

ALL_HEURISTIC = 'all'
HEURISTICS: dict[str, HeuristicBase] = {
    'zero': Zero,
    'prims_mst': PrimsMST
}

INITIAL_TOUR: dict[str, InitialTourBase] = {
    'greedy': GreedyInitialTour,
    'insertion': InsertionInitialTour
}

NEIGHBOR_TOUR: dict[str, NeighborTourBase] = {
    'swap': SwapNeighborTour,
    'two_opt': TwoOptNeighborTour,
    'insertion': InsertionNeighborTour
}

METADATA_ALPHA = 'alpha'
METADATA_HEURISTIC = 'heuristic'
METADATA_SOURCE_ID = 'source_id'
METADATA_ALPHA_FACTOR = 'alpha_factor'
METADATA_INITIAL_TOUR = 'initial_tour'
METADATA_NEIGHBOR_TOUR = 'neighbor_tour'
METADATA_FINAL_THRESHOLD = 'final_threshold'
METADATA_INITIAL_THRESHOLD = 'initial_threshold'