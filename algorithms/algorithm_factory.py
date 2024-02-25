from constants import app_constants

from algorithms.algorithm_base import AlgorithmBase

def get_algorithm(algorithm: str) -> AlgorithmBase:
    if algorithm not in app_constants.ALGORITHMS:
        raise ValueError('Algorithm not found')
    
    return app_constants.ALGORITHMS[algorithm]