# Cell 1
import numpy as np

def k_means_clustering(points: list[tuple[float, ...]], k: int,
                       initial_centroids: list[tuple[float, ...]],
                       max_iterations: int) -> list[tuple[float, ...]]:
                           
    points = np.array(points, dtype=float)
    centroids = np.array(initial_centroids, dtype=float)   
    n_clusters = len(centroids)

    for _ in range(max_iterations):
        distance = np.zeros((n_clusters, len(points)))
        for i in range(n_clusters):
            distance[i] = np.sqrt(np.sum((points - centroids[i]) ** 2, axis=1))

        node_min = np.argmin(distance, axis=0)

        node = {i: [] for i in range(n_clusters)}          
        for p in range(len(points)):
            node[node_min[p]].append(points[p])

        for i in range(n_clusters):
            if node[i]:
                centroids[i] = np.mean(node[i], axis=0)

    return [tuple(c) for c in centroids]