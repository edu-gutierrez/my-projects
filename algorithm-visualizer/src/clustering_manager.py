import clustering_algorithms

ALGORITHMS = {
    "1": ("KMeans", clustering_algorithms.kmeans),
    "2": ("DBSCAN", clustering_algorithms.dbscan),
    "3": ("Hierarchical", clustering_algorithms.hierarchical),
    "4": ("Mean Shift", clustering_algorithms.mean_shift),
}

ALGORITHMS_QT = {
    "KMeans": "1",
    "DBSCAN": "2",
    "Hierarchical": "3",
    "Mean Shift": "4",
}

def get_algorithm(choice: str):
    return ALGORITHMS.get(choice, (None, None))