from argparse import ArgumentParser

def _add_parser_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        '-i', '--input',
        type=str,
        help='Input graph file in the specified format',
        required=False
    )

def build_arg_parser() -> ArgumentParser:
    parser = ArgumentParser()
    _add_parser_arguments(parser=parser)
    return parser