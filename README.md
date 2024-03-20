# Traveling Salesman Problem Solver

## Project Overview

This project offers a solution to the Traveling Salesman Problem (TSP), for the course project CS 271A Intro to Artificial Intelligence.

### Key Features:
- **Heuristic Solutions**: Leverages A* algorithm with customizable heuristics.
- **Local Search Optimization**: Implements Adaptive Simulated Annealing for fine-tuning solutions.
- **Modular Design**: Easily extendable for experimenting with new algorithms or heuristics.

## Getting Started

Before diving into the usage of this project, please ensure you meet the following prerequisites:

- **Python 3.x** installed on your machine.

It is highly recommended to use a virtual environment for this project to isolate its dependencies from your global Python setup.

### Setting Up Your Environment

1. **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment:**
    - **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    - **Unix or MacOS:**
        ```bash
        source venv/bin/activate
        ```

3. **Install Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Example

**Heuristic (A Star)**
```bash
python3 main.py data/input/tsp-problem-10-30-75-25-1.txt \
    heuristic                                            \
    --heuristic prims_mst                                \
    --initial-tour greedy                                \
    --source-id 1
```

**Local Search (Adaptive Simulated Annealing)**
```bash
python3 main.py data/input/tsp-problem-10-30-75-25-1.txt \
    localsearch                                          \
    --initial-tour greedy                                \
    --neighbor-tour swap                                 \
    --alpha 1                                            \
    --alpha-factor 0.0001                                \
    --initial-threshold 10000                            \
    --final-threshold 1                                  \
    --source-id 1
```

## Usage Guide

Run the TSP solver by navigating to the project directory in your terminal and executing the following command:

```bash
python3 main.py [OPTIONS]
```

Replace `[OPTIONS]` with the specific options or commands tailored to your TSP problem. The tables below detail the main commands and options available for ease of use and clarity.

### Heuristic (A Star)

**Command Structure:**
```bash
Usage: main.py [OPTIONS] INPUT_FILE heuristic [ARGS]...
```

**Options Table:**

| Option                   | Description                                                  | Values                                | Required |
|--------------------------|--------------------------------------------------------------|---------------------------------------|:--------:|
| `-h, --heuristic`        | Heuristic algorithm for A* algorithm.                        | `zero`, `prims_mst`            |   Yes    |
| `-i, --initial-tour`     | Initial tour generation strategy.                            | `greedy`, `insertion`                 |   Yes    |
| `-s, --source-id INTEGER`| Start node ID for A*.                                        | Integer (default: 0)                  |    No    |
| `--help`                 | Show help message and exit.                                  |                                       |    No    |

### Localsearch (Adaptive Simulated Annealing)

**Command Structure:**
```bash
Usage: main.py [OPTIONS] INPUT_FILE localsearch [ARGS]...
```

**Options Table:**

| Option                          | Description                                                   | Values                                  | Required |
|---------------------------------|---------------------------------------------------------------|-----------------------------------------|:--------:|
| `-i, --initial-tour`            | Initial tour generation strategy for SA.                      | `greedy`, `insertion`                   |   Yes    |
| `-nb, --neighbor-tour`          | Neighbor tour generation algorithm for SA.                    | `swap`, `two_opt`, `insertion`          |   Yes    |
| `-a, --alpha FLOAT`             | Cooling rate for SA.                                          | Float                                   |   Yes    |
| `-af, --alpha-factor FLOAT RANGE`| Factor adjusting the cooling rate for SA.                    | Float (0<=x<=1)                         |   Yes    |
| `-ti, --initial-threshold FLOAT`| Initial threshold for SA.                                     | Float                                   |   Yes    |
| `-tf, --final-threshold FLOAT`  | Final threshold for SA.                                       | Float                                   |   Yes    |
| `-s, --source-id INTEGER`       | Starting node ID for SA.                                      | Integer (default: 0)                    |    No    |
| `--help`                        | Show help message and exit.                                   |                                         |    No    |
