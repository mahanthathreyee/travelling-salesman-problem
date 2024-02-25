from argparse import ArgumentParser

DEFAULT_INPUT_FILE = './data/input/tsp-problem-10-30-75-25-1.txt'

def _add_parser_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        '-i', '--input',
        type=str,
        help='Input graph file in the specified format',
        default=DEFAULT_INPUT_FILE,
        required=False
    )

    parser.add_argument(
        '-s', '--source-id',
        type=int,
        help='Source node ID range 0 to n-1',
        default=0,
        required=False
    )

def build_arg_parser() -> ArgumentParser:
    parser = ArgumentParser()
    _add_parser_arguments(parser=parser)
    return parser