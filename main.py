from pathlib import Path

from util import input_handler
from util import arg_parser

from core import graph
from core import dijkstra

DEFAULT_INPUT_FILE = './data/input/tsp-problem-10-30-75-25-1.txt'

def parse_input(input_file: str):
    graph_file = Path(DEFAULT_INPUT_FILE)
    
    if input_file:
        graph_file = Path(input_file)

    if not graph_file.exists():
        raise FileNotFoundError(f"File '{graph_file}' does not exist")

    return input_handler.parse_input_matrix(graph_file)

if __name__ == "__main__":
    parser = arg_parser.build_arg_parser()
    args = parser.parse_args()

    input_matrix = parse_input(args.input)
    
    import pandas as pd
    pd.DataFrame(input_matrix).to_csv('temp.csv', index=False)
    
    n_cities = len(input_matrix)
    cities = graph.construct_from_matrix(input_matrix)

    dijkstra.compute_shortest_path(
        source_id=0,
        destination_id=3,
        n_cities=n_cities,
        city_graph=cities
    )