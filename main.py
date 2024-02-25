import pandas as pd
from pathlib import Path
from argparse import Namespace

from util import input_handler
from util import arg_parser

from core import graph
from core.algorithm_runner import AlgorithmRunner

from algorithms.algorithm_base import AlgorithmBase
from algorithms.impl.dijkstra_tsp import DijikstraTSP

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
    algorithm: AlgorithmBase = DijikstraTSP(
        args=args,
        n_cities=n_cities,
        city_graph=city_graph
    )

    runner = AlgorithmRunner(algorithm)
    runner.run()
    results.append(runner.results())

if __name__ == "__main__":
    results = []

    args, input_matrix = get_input()
    n_cities = len(input_matrix)
    city_graph = graph.construct_from_matrix(input_matrix)

    results.append(process_algorithm(args))

    print(pd.DataFrame(results).to_markdown())
