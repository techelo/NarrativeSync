from sklearn.cluster import AgglomerativeClustering
import numpy as np

def cluster_articles(similarity_matrix, threshold=0.7):
    distance_matrix = 1 - similarity_matrix
    clustering = AgglomerativeClustering(
        affinity='precomputed',
        linkage='average',
        distance_threshold=1-threshold,
        n_clusters=None
    ).fit(distance_matrix)
    return clustering.labels_
