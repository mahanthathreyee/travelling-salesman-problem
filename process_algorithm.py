from typing import Any

from constants import app_constants

from algorithms import algorithm_factory
from algorithms.algorithm_base import AlgorithmBase

from heuristics import heuristic_factory
from heuristics.heuristic_base import HeuristicBase

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
            'source_id': source_id,
            'heuristic': heuristic
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