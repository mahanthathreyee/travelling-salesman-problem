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
def heuristic(heuristic, source_id):
    ARGUMENTS.algorithm = 'a_star'
    ARGUMENTS.heuristic = heuristic
    ARGUMENTS.source_id = source_id
#endregion

#region Local search Command
@click.command()
@click.option('--algorithm', '-a')
def localsearch(algorithm):
    return algorithm
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
