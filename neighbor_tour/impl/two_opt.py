import random

from model.state import State

from neighbor_tour.neighbor_tour_base import NeighborTourBase

class TwoOptNeighborTour(NeighborTourBase):
    NAME: str = 'Two Opt'

    def generate_neighbor_tour(self, current_state: State) -> State:
        tour = current_state.path.copy()
        
        if len(tour) <= 2:
            return current_state
        
        i, j = random.sample(tour, 2)
        tour[i:j] = tour[i:j][::-1]

        new_state = State(
            source_id=tour[0],
            n_cities=self.n_cities,
            branch_state=True
        )
        new_state.path = tour

        return new_state
