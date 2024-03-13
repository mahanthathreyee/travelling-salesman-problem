from constants import app_constants

from initial_tour.initial_tour_base import InitialTourBase

def get_initial_tour(initial_tour: str) -> InitialTourBase:
    if initial_tour not in app_constants.INITIAL_TOUR:
        raise ValueError('Initial tour option not found')
    
    return app_constants.INITIAL_TOUR[initial_tour]