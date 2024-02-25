import pandas as pd
from pathlib import Path
from argparse import Namespace

from util import input_handler
from util import arg_parser

from constants import app_constants

from core import graph
from core.algorithm_runner import AlgorithmRunner

from algorithms import algorithm_factory
from algorithms.algorithm_base import AlgorithmBase

from heuristics import heuristic_factory
from heuristics.heuristic_base import HeuristicBase

def parse_input(input_file: str):
    graph_file = Path(input_file)

    if not graph_file.exists():
        raise FileNotFoundError(f"File '{graph_file}' does not exist")

    return input_handler.parse_input_matrix(graph_file)

def get_input():
    parser = arg_parser.build_arg_parser()
    args = parser.parse_args()
    input_matrix = parse_input(args.input)
    
    pd.DataFrame(input_matrix).to_csv('temp.csv', index=False)

    return args, input_matrix

def process_algorithm(args: Namespace):
    heuristic: HeuristicBase = heuristic_factory.get_heuristic(args.heuristic)
    heuristic = heuristic(
        n_cities=n_cities, 
        city_graph=city_graph
    )

    algorithm: AlgorithmBase = algorithm_factory.get_algorithm(args.algorithm)
    algorithm = algorithm(
        n_cities=n_cities,
        city_graph=city_graph,
        metadata={
            'source_id': args.source_id,
            'heuristic': heuristic
        }
    )

    runner = AlgorithmRunner(algorithm)
    runner.run()
    results.append(runner.results())

if __name__ == "__main__":
    results = []

    args, input_matrix = get_input()
    n_cities = len(input_matrix)
    city_graph = graph.construct_from_matrix(input_matrix)

    process_algorithm(args)
    print(pd.DataFrame(results).to_markdown())
