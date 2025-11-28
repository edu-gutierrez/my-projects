import clustering_algorithms

ALGORITHMS = {
    "1": ("KMeans", clustering_algorithms.kmeans),
}

ALGORITHMS_QT = {
    "KMeans": "1",
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))