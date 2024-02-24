import numpy as np

from model.node import Node
from model.edge import Edge

def generate_nodes(n_cities: int) -> list[Node]:
    nodes = [None] * n_cities

    for i in range(n_cities):
        nodes[i] = Node(id=i)

    return nodes

def construct_city_edges(city: Node, neighbor_weights: np.ndarray, n_cities: int, cities: list[Node]) -> list[Node]:
    city_edges: list[Node] = [None] * (n_cities)

    for i, neighbor in enumerate(cities):
        city_edges[i] = Edge(
            weight=neighbor_weights[i].item(),
            source=city,
            destination=neighbor
        )

    return city_edges

def construct_from_matrix(city_weights: np.ndarray) -> list[Node]:
    n_cities = len(city_weights)
    cities = generate_nodes(n_cities)

    for i, city in enumerate(cities):
        city.neighbors = construct_city_edges(
            city=city,
            neighbor_weights=city_weights[i],
            n_cities=n_cities,
            cities=cities
        )
    
    return cities