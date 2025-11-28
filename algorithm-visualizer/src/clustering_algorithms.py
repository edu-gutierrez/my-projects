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