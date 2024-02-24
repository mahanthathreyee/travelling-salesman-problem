import numpy as np
from pathlib import Path

def parse_input_matrix(file_path: Path) -> np.ndarray:
    return np.loadtxt(
        fname=file_path, 
        dtype='f',
        delimiter=' ',
        skiprows=1
    )