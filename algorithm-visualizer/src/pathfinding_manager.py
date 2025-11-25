import pathfinding_algorithms

ALGORITHMS = {
    "1": ("BFS", pathfinding_algorithms.bfs),
    "2": ("DFS", pathfinding_algorithms.dfs),
}

ALGORITHMS_QT = {
    "BFS": "1",
    "DFS": "2",
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))