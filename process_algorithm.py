from typing import Any

from constants import app_constants

from algorithms import algorithm_factory
from algorithms.algorithm_base import AlgorithmBase

from heuristics import heuristic_factory
from heuristics.heuristic_base import HeuristicBase

from initial_tour import initial_tour_factory
from initial_tour.initial_tour_base import InitialTourBase

from neighbor_tour import neighbor_tour_factory
from neighbor_tour.neighbor_tour_base import NeighborTourBase

from model.node import Node
from core.algorithm_runner import AlgorithmRunner

def process_algorithm(algorithm: str, n_cities: int, city_graph: list[Node], metadata: dict[str, Any]):
    algorithm: AlgorithmBase = algorithm_factory.get_algorithm(algorithm)
    algorithm = algorithm(
        n_cities=n_cities,
        city_graph=city_graph,
        metadata=metadata
    )

    runner = AlgorithmRunner(algorithm)
    runner.run()
    return runner.results()

def process_heuristic(heuristic_selected: str, n_cities: int, city_graph: list[Node], source_id: int):
    if heuristic_selected == app_constants.ALL_HEURISTIC:
        heuristic_selected = filter(
            lambda key: key != app_constants.ALL_HEURISTIC, 
            list(app_constants.HEURISTICS.keys())
        )
    else:
        heuristic_selected = [heuristic_selected]

    results = []
    for heuristic_key in heuristic_selected:
        heuristic: HeuristicBase = heuristic_factory.get_heuristic(heuristic_key)
        heuristic = heuristic(
            n_cities=n_cities, 
            city_graph=city_graph
        )

        metadata = {
            app_constants.METADATA_SOURCE_ID: source_id,
            app_constants.METADATA_HEURISTIC: heuristic
        }

        results.append(
            process_algorithm(
                algorithm=app_constants.HEURISTIC_ALGORITHM,
                n_cities=n_cities,
                city_graph=city_graph,
                metadata=metadata
            )
        )

    return results

def process_localsearch(intial_tour_selected: str, neighbor_tour_selected: int, alpha: float, alpha_factor: float, initial_threshold: float, final_threshold: float, n_cities:int, city_graph: list[Node], source_id: int):
    results = []

    initial_tour: InitialTourBase = initial_tour_factory.get_initial_tour(intial_tour_selected)
    initial_tour = initial_tour(
        n_cities=n_cities, 
        city_graph=city_graph
    )

    neighbor_tour: NeighborTourBase = neighbor_tour_factory.get_neighbor_tour(neighbor_tour_selected)
    neighbor_tour = neighbor_tour(
        n_cities=n_cities, 
        city_graph=city_graph
    )

    metadata = {
        app_constants.METADATA_SOURCE_ID: source_id,
        app_constants.METADATA_INITIAL_TOUR: initial_tour,
        app_constants.METADATA_NEIGHBOR_TOUR: neighbor_tour,
        app_constants.METADATA_ALPHA: alpha,
        app_constants.METADATA_ALPHA_FACTOR: alpha_factor,
        app_constants.METADATA_INITIAL_THRESHOLD: initial_threshold,
        app_constants.METADATA_FINAL_THRESHOLD: final_threshold
    }

    results.append(
        process_algorithm(
            algorithm=app_constants.SLS_ALGORITHM,
            n_cities=n_cities,
            city_graph=city_graph,
            metadata=metadata
        )
    )

    return results
