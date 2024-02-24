import heapq

from model.node import Node
from constants import app_constants

def compute_shortest_path(source_id: int, destination_id: int, n_cities: int, city_graph: list[Node]):
    visited = set()
    unvisited_cities: list[tuple[int, Node]] = [(0, city_graph[source_id])]
    
    city_distances = [app_constants.INFINITY] * n_cities
    city_distances[source_id] = 0

    predecessor = [None] * n_cities

    while unvisited_cities:
        distance_to_city, city = heapq.heappop(unvisited_cities)
        
        if city.id == destination_id:
            print('Found shortest path to destination node')
            path_to_destination = reconstruct_path(predecessor, source_id, destination_id)
            print(f'Path: {path_to_destination}')
            print(f'Predecessors: {predecessor}')
            return

        if city in visited: 
            continue
        visited.add(city.id)

        for neighbor_path in city.neighbors:
            explore_neighbors(neighbor_path, visited, unvisited_cities, city_distances, predecessor, distance_to_city, city)

def explore_neighbors(neighbor_path, visited, unvisited_cities, city_distances, predecessor, distance_to_city, city):
    if neighbor_path.destination_id in visited:
        return

    new_distance_to_neighbor = distance_to_city + neighbor_path.weight
    if new_distance_to_neighbor < city_distances[neighbor_path.destination_id]:
        city_distances[neighbor_path.destination_id] = new_distance_to_neighbor
        predecessor[neighbor_path.destination_id] = city.id
            
        heapq.heappush(
            unvisited_cities, 
            (new_distance_to_neighbor, neighbor_path.destination_node)
        )

def reconstruct_path(predecessor, source_id, destination_id):
    path = []
    city_id = destination_id
    
    while city_id != None:
        path.append(city_id)
        city_id = predecessor[city_id]
    path.reverse()
    
    return path if path[0] == source_id else []