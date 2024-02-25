from constants import app_constants

from heuristics.heuristic_base import HeuristicBase

def get_heuristic(heuristic: str) -> HeuristicBase:
    if heuristic not in app_constants.HEURISTICS:
        raise ValueError('Heuristic not found')
    
    return app_constants.HEURISTICS[heuristic]