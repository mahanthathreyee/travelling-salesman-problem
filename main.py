import pandas as pd
from pathlib import Path

from model.parameter import Parameter
from process_algorithm import process_heuristic

from util import input_handler
from util import arg_parser

from core import graph

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

    input_matrix = get_input(arg_parser.ARGUMENTS)
    n_cities = len(input_matrix)
    city_graph = graph.construct_from_matrix(input_matrix)

    results += process_heuristic(
        heuristic_selected=arg_parser.ARGUMENTS.heuristic,
        n_cities=n_cities,
        city_graph=city_graph,
        source_id=arg_parser.ARGUMENTS.source_id
    )
    
    print(pd.DataFrame(results).to_markdown())
