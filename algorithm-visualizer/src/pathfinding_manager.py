import pathfinding_algorithms

ALGORITHMS = {
    "1": ("BFS", pathfinding_algorithms.bfs),
    "2": ("DFS", pathfinding_algorithms.dfs),
    "3": ("A*",  pathfinding_algorithms.a_star),
    "4": ("GreedyBFS", pathfinding_algorithms.greedy_bfs),
}

ALGORITHMS_QT = {
    "BFS": "1",
    "DFS": "2",
    "A*":  "3",
    "GreedyBFS": "4",
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))