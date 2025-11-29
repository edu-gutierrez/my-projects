import clustering_algorithms

ALGORITHMS = {
    "1": ("KMeans", clustering_algorithms.kmeans),
    "2": ("DBSCAN", clustering_algorithms.dbscan),
}

ALGORITHMS_QT = {
    "KMeans": "1",
    "DBSCAN": "2",
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))