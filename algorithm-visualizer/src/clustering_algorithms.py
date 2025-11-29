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

def hierarchical(data, k):
    n_points = len(data)

    # Inicializamos cada punto como un cluster
    labels = np.arange(n_points)
    clusters = {}
    for i in range(n_points):
        clusters[i] = [i]
    
    yield ("init", labels, None)
    
    current_k = n_points
    
    while current_k > k:
        min_dist = float('inf')
        merge = (-1, -1)
        
        active_ids = list(clusters.keys())
        
        # Para cada cluster buscamos el mas cercano y los fusionamos
        for i in range(len(active_ids)):
            id1 = active_ids[i]
            points1 = data[clusters[id1]]
            c1 = np.mean(points1, axis=0)
            
            for j in range(i + 1, len(active_ids)):
                id2 = active_ids[j]
                points2 = data[clusters[id2]]
                c2 = np.mean(points2, axis=0)
                
                dist = np.linalg.norm(c1 - c2)
                
                if dist < min_dist:
                    min_dist = dist
                    merge = (id1, id2)
        
        id_keep, id_remove = merge

        c1 = np.mean(data[clusters[id_keep]], axis=0)
        c2 = np.mean(data[clusters[id_remove]], axis=0)
        fusion_centers = [c1, c2]
        
        yield ("update", labels, fusion_centers)
        
        clusters[id_keep].extend(clusters[id_remove])
        
        for i in range(len(labels)):
            if labels[i] == id_remove:            
                labels[i] = id_keep

        del clusters[id_remove]
        current_k -= 1
        
        yield ("update", labels, fusion_centers)

    yield ("done", labels, None)

def mean_shift(data, bandwidth):
    n_points = len(data)
    
    # Cada punto es un centroide
    centroids = np.copy(data)
    labels = np.zeros(n_points, dtype=int)
    yield ("init", labels, centroids)
    
    max_iterations = 100
    for _ in range(max_iterations):
        new_centroids = np.copy(centroids)
        
        # Buscamos los vecinos que están dentro del radio y movemos el centroide hacia los vecinos
        for i in range(n_points):
            dist = np.linalg.norm(data - centroids[i], axis=1)
            points_within = data[dist < bandwidth]
        
            if len(points_within) > 0:
                new_centroids[i] = np.mean(points_within, axis=0)
    
        yield ("update", labels, new_centroids)
        
        # Miramos si ya no cambia casi nada el centroide
        if np.allclose(centroids, new_centroids, 0.001):
            break
            
        centroids = new_centroids

    unique_centroids = []
    final_labels = np.zeros(n_points, dtype=int)
    
    # Buscamos el grupo de cada centroide y se lo asignamos
    for i in range(n_points):
        my_centroid = centroids[i]
        found_group = False
        
        for group_id, group_center in enumerate(unique_centroids):
            if np.linalg.norm(my_centroid - group_center) < 1.0:
                final_labels[i] = group_id
                found_group = True
                break
        
        if not found_group:
            unique_centroids.append(my_centroid)
            final_labels[i] = len(unique_centroids) - 1
            
    yield ("done", final_labels, np.array(unique_centroids))