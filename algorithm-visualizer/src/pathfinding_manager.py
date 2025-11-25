import pathfinding_algorithms

ALGORITHMS = {
    "1": ("BFS", pathfinding_algorithms.bfs),
}

ALGORITHMS_QT = {
    "BFS": "1",
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))