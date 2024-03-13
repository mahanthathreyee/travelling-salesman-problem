import click

from constants import app_constants
from model.parameter import Parameter

ARGUMENTS: Parameter = Parameter()

#region Heuristic Command
@click.command()
@click.option(
    '--heuristic', '-h', 
    type=click.Choice(app_constants.HEURISTICS.keys()), 
    help="Heuristic algorithm to use for A_star algorithm",
    required=True)
@click.option(
    '--source-id', '-s', 
    type=click.INT, default=0,
    help="Start node ID for A_star (doesn't affect final result)")
def heuristic(heuristic: str, source_id: int):
    ARGUMENTS.algorithm = app_constants.HEURISTIC_ALGORITHM
    ARGUMENTS.heuristic = heuristic
    ARGUMENTS.source_id = source_id
#endregion

#region Local search Command
@click.command()
@click.option(
    '--initial-tour', '-i', 
    type=click.Choice(app_constants.INITIAL_TOUR.keys()), 
    help="Initial tour generation algorithn for SA",
    required=True)
@click.option(
    '--neighbor-tour', '-nb', 
    type=click.Choice(app_constants.NEIGHBOR_TOUR.keys()), 
    help="Neighbor tour generation algorithn for SA",
    required=True)
@click.option(
    '--alpha', '-a', 
    type=click.FLOAT, 
    help="Cooling rate for SA",
    required=True)
@click.option(
    '--threshold', '-t', 
    type=click.FLOAT, 
    help="Final threshold rate for SA",
    required=True)
@click.option(
    '--source-id', '-s', 
    type=click.INT, default=0,
    help="Start node ID for SA (doesn't affect final result)")
def localsearch(initial_tour: str, neighbor_tour: str, alpha: float, threshold: float, source_id: int):
    ARGUMENTS.algorithm = app_constants.SLS_ALGORITHM
    ARGUMENTS.initial_tour = initial_tour
    ARGUMENTS.neighbor_tour = neighbor_tour
    ARGUMENTS.alpha = alpha
    ARGUMENTS.threshold = threshold
    ARGUMENTS.source_id = source_id
#endregion

#region Help Command (Default)
@click.command(no_args_is_help=True)
def help():
    pass
#endregion

#region Group all commands
@click.group()
@click.argument(
    'INPUT_FILE',
    type=click.Path(exists=True),
    required=True)
def tsp_argument_group(input_file):
    ARGUMENTS.input_file = input_file

tsp_argument_group.add_command(heuristic)
tsp_argument_group.add_command(localsearch)
tsp_argument_group.add_command(help)
# endregion
