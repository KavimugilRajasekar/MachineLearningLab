import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import umap
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

def load_and_preprocess_data(filepath):
    """Loads the dataset and performs preprocessing."""
    df = pd.read_csv(filepath)
    
    # Selecting numerical features relevant for lifestyle patterns
    numerical_features = [
        'study_hours', 'self_study_hours', 'online_classes_hours', 
        'social_media_hours', 'gaming_hours', 'sleep_hours', 
        'screen_time_hours', 'exercise_minutes', 'caffeine_intake_mg', 
        'mental_health_score', 'focus_index', 'productivity_score'
    ]
    
    X = df[numerical_features]
    
    # Scaling features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return df, X_scaled, numerical_features

def apply_umap(X_scaled):
    """Reduces dimensionality using UMAP for visualization and clustering."""
    reducer = umap.UMAP(n_neighbors=15, min_dist=0.1, n_components=2, random_state=42)
    embedding = reducer.fit_transform(X_scaled)
    return embedding

def apply_dbscan(embedding, eps=0.5, min_samples=5):
    """Clusters the data using DBSCAN on the UMAP embedding."""
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit_predict(embedding)
    return clusters

def profile_clusters(df, clusters, features):
    """Analyzes each cluster to identify lifestyle patterns."""
    df['Cluster'] = clusters
    
    # Remove noise for profiling (-1 in DBSCAN)
    profile_df = df[df['Cluster'] != -1]
    
    cluster_stats = profile_df.groupby('Cluster')[features].mean()
    
    # Logic to map clusters to categories based on feature means
    # This is a heuristic and might need adjustment based on data distribution
    category_map = {}
    for cluster in cluster_stats.index:
        stats = cluster_stats.loc[cluster]
        
        if stats['study_hours'] > cluster_stats['study_hours'].mean() and stats['social_media_hours'] < cluster_stats['social_media_hours'].mean():
            category_map[cluster] = "Academically Intensive"
        elif stats['gaming_hours'] > cluster_stats['gaming_hours'].mean() or stats['social_media_hours'] > cluster_stats['social_media_hours'].mean():
            category_map[cluster] = "Digitally Addicted"
        elif stats['exercise_minutes'] > cluster_stats['exercise_minutes'].mean() and stats['sleep_hours'] > 6:
            category_map[cluster] = "Balanced Lifestyle"
        else:
            category_map[cluster] = "Socially Active" # Default / Fallback
            
    df['Lifestyle_Category'] = df['Cluster'].map(category_map).fillna("Uncategorized (Noise)")
    return df, cluster_stats, category_map

def visualize_clusters(embedding, categories, output_path):
    """Plots the UMAP embedding colored by the discovered lifestyle categories."""
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x=embedding[:, 0], y=embedding[:, 1], hue=categories, palette='viridis', s=60, alpha=0.7)
    plt.title('Student Lifestyle Clusters (UMAP + DBSCAN)', fontsize=15)
    plt.xlabel('UMAP Component 1')
    plt.ylabel('UMAP Component 2')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    filepath = "students-productivity-dataset.csv"
    print("Step 1: Loading and preprocessing data...")
    df, X_scaled, features = load_and_preprocess_data(filepath)
    
    print("Step 2: Reducing dimensionality with UMAP...")
    embedding = apply_umap(X_scaled)
    
    print("Step 3: Discovering patterns with DBSCAN...")
    # These parameters might need tuning based on the UMAP output density
    clusters = apply_dbscan(embedding, eps=0.4, min_samples=10)
    
    print("Step 4: Profiling lifestyle categories...")
    df, stats, cat_map = profile_clusters(df, clusters, features)
    
    print("\nDiscovered Lifestyle Categories Mapping:")
    for cluster, label in cat_map.items():
        print(f"Cluster {cluster}: {label}")
    
    print("\nCluster Statistics (Mean):")
    print(stats)
    
    print("\nStep 5: Generating visualization...")
    visualize_clusters(embedding, df['Lifestyle_Category'], 'lifestyle_clusters.png')
    
    # Save the results
    df.to_csv("students_lifestyle_discovery_results.csv", index=False)
    print("\nResults saved to 'students_lifestyle_discovery_results.csv'")
    print("Visualization saved to 'lifestyle_clusters.png'")

if __name__ == "__main__":
    main()
