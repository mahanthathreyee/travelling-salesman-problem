import os
import numpy as np
from tqdm import tqdm
from core import graph
import process_algorithm
from main import parse_input
from itertools import product
from constants import app_constants

parameters = {
    'intial_tour_selected': list(app_constants.INITIAL_TOUR.keys()),
    'neighbor_tour_selected': list(app_constants.NEIGHBOR_TOUR.keys()),
    'alpha': [1],
    'alpha_factor': [0.0001],
    'initial_threshold': [10_000],
    'final_threshold': [1],
    'source_id': [0]
}

base_data_path = 'data/input/competition/'

def combination_to_kwargs(keys, combination):
    return dict(zip(keys, combination))

def process_file(input_file: str):
    results = []

    input_matrix = parse_input(input_file)
    n_cities = len(input_matrix)
    city_graph = graph.construct_from_matrix(input_matrix)

    param_combinations = list(product(*parameters.values()))
    
    for combination in param_combinations:
        # print(f'Running combination: {combination}')
        kwargs = combination_to_kwargs(parameters.keys(), combination)
        result = process_algorithm.process_localsearch(
            n_cities=n_cities, city_graph=city_graph,
            **kwargs
        )
        results.append({
            'Tour': result[0]['Tour'],
            'Tour Length': n_cities,
            'Elapsed Time': result[0]['Elapsed Time']
        })
        
    return results

for data_instance in sorted(os.listdir(base_data_path), key=lambda x: int(x.split('-')[1])):
    print(f'Instance: {data_instance}')
    final_results = []
    for data_file in tqdm(os.listdir(base_data_path + '/' + data_instance)):
        relative_data_file = base_data_path + '/' + data_instance +'/' + data_file
        final_results += process_file(relative_data_file)

    avg_elapsed = np.mean([d["Elapsed Time"] for d in final_results])
    print(f'{data_instance.split("-")[1]}, ' 
        + f'{avg_elapsed}'
    )
