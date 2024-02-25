from argparse import ArgumentParser

from constants import app_constants

def _add_parser_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        '-i', '--input',
        type=str,
        help='Input graph file in the specified format',
        default=app_constants.DEFAULT_INPUT_FILE,
        required=False
    )

    algorithm_choices = list(app_constants.ALGORITHMS.keys())
    parser.add_argument(
        '-a', '--algorithm',
        type=str,
        choices=algorithm_choices,
        help='Algorithm to be used',
        default=algorithm_choices[0],
        required=False
    )

    heuristic_choices = list(app_constants.HEURISTICS.keys())
    parser.add_argument(
        '-hx', '--heuristic',
        type=str,
        choices=heuristic_choices,
        help='Heuristic to be used in case of A star algorithm',
        default=heuristic_choices[0],
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