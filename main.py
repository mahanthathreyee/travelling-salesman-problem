from pathlib import Path
from util import input_handler
from util import arg_parser

DEFAULT_INPUT_FILE = './data/input/tsp-problem-10-2-75-25-1.txt'

def parse_input(input_file: str):
    graph_file = Path(DEFAULT_INPUT_FILE)
    
    if input_file:
        graph_file = Path(input_file)

    if not graph_file.exists():
        raise FileNotFoundError(f"File '{graph_file}' does not exist")

    input_handler.parse_input_matrix(graph_file)

if __name__ == "__main__":
    parser = arg_parser.build_arg_parser()
    args = parser.parse_args()

    parse_input(args.input)
