import heapq

from model.node import Node
from model.state import State
from constants import app_constants

def compute_tour(source_id: int, n_cities: int, city_graph: list[Node]):
    state_space: list[State] = []

    initial_state = State(
        source_id=source_id,
        n_cities=n_cities
    )
    heapq.heappush(state_space, initial_state)

    while state_space:
        current_state = heapq.heappop(state_space)

        if not current_state.unvisited:
            print('Tour Found')
            print(f'State: {current_state}')
            return
        
        for neighbor_id in current_state.unvisited:
            neighbor_path = city_graph[current_state.current_city_id].neighbors[neighbor_id]
            
            new_cost = current_state.cost + neighbor_path.weight
            new_state = current_state.construct_new_state(
                neighbor_id=neighbor_id,
                cost=new_cost
            )

            heapq.heappush(state_space, new_state)
