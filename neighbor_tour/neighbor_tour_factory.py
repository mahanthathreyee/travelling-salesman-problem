from constants import app_constants

from neighbor_tour.neighbor_tour_base import NeighborTourBase

def get_neighbor_tour(neighbor_tour: str) -> NeighborTourBase:
    if neighbor_tour not in app_constants.NEIGHBOR_TOUR:
        raise ValueError('Neighbor tour option not found')
    
    return app_constants.NEIGHBOR_TOUR[neighbor_tour]