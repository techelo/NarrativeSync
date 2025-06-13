import yaml
from src.collector import fetch_rss_feed
from src.parser import normalize_articles, compute_similarity
from src.clustering import cluster_articles
from src.visualizer import plot_clusters
import pandas as pd

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    all_articles = []
    for feed_url in config["rss_feeds"]:
        try:
            articles = fetch_rss_feed(feed_url)
            all_articles.extend(articles)
        except Exception as e:
            print(f"Error fetching {feed_url}: {e}")

    df = normalize_articles(all_articles)
    similarity_matrix = compute_similarity(df)
    labels = cluster_articles(similarity_matrix)
    plot_clusters(df, labels)
    df["cluster"] = labels
    df.to_csv("output/clustered_articles.csv", index=False)
    print("Analysis complete. Results saved in output/.")

if __name__ == "__main__":
    main()
