import numpy as np

def kmeans(data, k):
    n_points = len(data)
    indices = np.random.choice(n_points, k, replace=False)
    centroids = data[indices]
    labels = np.zeros(n_points, dtype=int)
    
    yield ("init", labels, centroids)
    
    max_iterations = 100
    for _ in range(max_iterations):
        distances = np.zeros((n_points, k))
        
        # Calculamos la distancia de los puntos a cada centroide
        for i in range(k):
            distances[:, i] = np.linalg.norm(data - centroids[i], axis=1)
            
        # Buscamos el centroide más cercano
        new_labels = np.argmin(distances, axis=1)
        
        yield ("update", new_labels, centroids)
        
        new_centroids = np.zeros((k, 2))
        for i in range(k):
            points_in_cluster = data[new_labels == i]
            
            if len(points_in_cluster) > 0:
                # Calculamos nuevo centroide como la media de sus puntos
                new_centroids[i] = points_in_cluster.mean(axis=0)
            else:
                new_centroids[i] = centroids[i]
        
        yield ("update", new_labels, new_centroids)
        
        # Miramos si ya no cambia casi nada el centroide
        if np.allclose(centroids, new_centroids, 0.001):
            break
            
        centroids = new_centroids
        labels = new_labels

    yield ("done", labels, centroids)

def dbscan(data, eps, min_samples):
    n_points = len(data)
    
    # Metemos -1 a los no visitados
    labels = np.full(n_points, -1, dtype=int)
    
    cluster_id = 0
    yield ("init", labels, None)
    
    for i in range(n_points):

        if labels[i] == -1:
            neighbors = _get_neighbors(data, i, eps)
            
            yield ("check", labels, [data[i]])
            
            if len(neighbors) < min_samples:
                labels[i] = -2
                yield ("noise", labels, [data[i]])
            else: # Hemos encontrado  un centroide
                labels[i] = cluster_id
                yield from _expand_cluster(data, labels, neighbors, cluster_id, eps, min_samples)
                cluster_id += 1

    yield ("done", labels, None)

def _expand_cluster(data, labels, neighbors, cluster_id, eps, min_samples):
    i = 0
    while i < len(neighbors):
        point = neighbors[i]
            
        if labels[point] == -1 or labels[point] == -2:
            labels[point] = cluster_id
            yield ("expand", labels, [data[point]])

            new_neighbors = _get_neighbors(data, point, eps)
            if len(new_neighbors) >= min_samples:
                neighbors = np.concatenate((neighbors, new_neighbors))
        
        i += 1

def _get_neighbors(data, point, eps):
    distances = np.linalg.norm(data - data[point], axis=1)
    return np.where(distances <= eps)[0]