from constants import app_constants

from initial_tour.initial_tour_base import InitialTourBase

class InsertionInitialTour(InitialTourBase):
    NAME: str = 'Insertion Initial Tour'

    def create_initial_tour(self, source_id: int) -> list[int]:
        tour = [source_id]
        visited = set([source_id])

        while len(visited) < self.n_cities:
            next_node_index = -1
            shortest_next_node = None
            shortest_next_distance = app_constants.INFINITY

            unvisited = set(range(self.n_cities)).difference(visited)

            for next_city_id in unvisited:
                for city_i in tour:
                    city_j = (city_i + 1) % len(tour)

                    if city_i == city_j:
                        distance = self.city_graph[city_i].neighbors[next_city_id].weight
                    else:
                        distance = self.city_graph[city_i].neighbors[next_city_id].weight   \
                               + self.city_graph[next_city_id].neighbors[city_j].weight \
                               - self.city_graph[city_i].neighbors[city_j].weight
                        
                    if distance < shortest_next_distance:
                        next_node_index = city_i + 1
                        shortest_next_distance = distance
                        shortest_next_node = next_city_id

            tour.insert(next_node_index, shortest_next_node)
            visited.add(shortest_next_node)

        print('Tour created')
        return tour
