import matplotlib.pyplot as plt
import pandas as pd

def plot_clusters(df, labels):
    df['cluster'] = labels
    plt.figure(figsize=(10, 6))
    for cluster in sorted(df['cluster'].unique()):
        subset = df[df['cluster'] == cluster]
        plt.scatter(subset.index, [cluster]*len(subset), label=f'Cluster {cluster}')
    plt.xlabel("Article Index")
    plt.ylabel("Cluster")
    plt.title("Narrative Clustering")
    plt.legend()
    plt.savefig("output/cluster_plot.png")
    plt.close()
