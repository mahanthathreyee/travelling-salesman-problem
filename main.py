import sys
import pandas as pd
from pathlib import Path

from constants import app_constants
from model.parameter import Parameter
from process_algorithm import process_heuristic
from process_algorithm import process_localsearch

from core import graph
from util import input_handler
from util import arg_parser

def parse_input(input_file: str):
    graph_file = Path(input_file)

    if not graph_file.exists():
        raise FileNotFoundError(f"File '{graph_file}' does not exist")

    return input_handler.parse_input_matrix(graph_file)

def get_input(args: Parameter):
    input_matrix = parse_input(args.input_file)
    pd.DataFrame(input_matrix).to_csv('temp.csv', index=False)
    return input_matrix

if __name__ == "__main__":
    results = []

    arg_parser.tsp_argument_group.main(standalone_mode=False)
    if not arg_parser.ARGUMENTS.algorithm:
        sys.exit(0)

    input_matrix = get_input(arg_parser.ARGUMENTS)
    n_cities = len(input_matrix)
    city_graph = graph.construct_from_matrix(input_matrix)

    if arg_parser.ARGUMENTS.algorithm == app_constants.HEURISTIC_ALGORITHM:
        results += process_heuristic(
            heuristic_selected=arg_parser.ARGUMENTS.heuristic,
            n_cities=n_cities,
            city_graph=city_graph,
            source_id=arg_parser.ARGUMENTS.source_id
        )
    else:
        results += process_localsearch(
            intial_tour_selected=arg_parser.ARGUMENTS.initial_tour,
            neighbor_tour_selected=arg_parser.ARGUMENTS.neighbor_tour,
            alpha=arg_parser.ARGUMENTS.alpha,
            initial_threshold=arg_parser.ARGUMENTS.initial_threshold,
            final_threshold=arg_parser.ARGUMENTS.final_threshold,
            n_cities=n_cities,
            city_graph=city_graph,
            source_id=arg_parser.ARGUMENTS.source_id
        )
    
    print(pd.DataFrame(results).to_markdown())
