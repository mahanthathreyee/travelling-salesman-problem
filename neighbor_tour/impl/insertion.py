import random

from model.state import State

from neighbor_tour.neighbor_tour_base import NeighborTourBase

class InsertionNeighborTour(NeighborTourBase):
    NAME: str = 'Insertion'

    def generate_neighbor_tour(self, current_state: State) -> State:
        tour = current_state.path.copy()
        
        if len(tour) <= 2:
            return current_state
        
        i = random.sample(tour, 1)
        city_id_i = tour[i]
        del tour[i]
        j = random.sample(tour, 1)
        tour.insert(j, city_id_i)

        new_state = State(
            source_id=tour[0],
            n_cities=self.n_cities,
            branch_state=True
        )
        new_state.path = tour

        return new_state
