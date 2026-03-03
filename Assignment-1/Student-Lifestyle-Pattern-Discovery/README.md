# Student Lifestyle Pattern Discovery

This project implements an unsupervised machine learning model to discover student lifestyle patterns based on behavioral data. It uses **UMAP** for dimensionality reduction and **DBSCAN** for clustering.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [How the Algorithms Work](#how-the-algorithms-work)
- [Code Structure](#code-structure)
- [Installation and Usage](#installation-and-usage)
- [Discovered Lifestyle Patterns](#discovered-lifestyle-patterns)

## Project Overview
The goal is to analyze student behavioral data (study hours, social media usage, physical activity, sleep, etc.) to identify hidden lifestyle categories without using predefined labels.

### Target Categories:
- **Academically Intensive Students**: High study hours, low social media.
- **Balanced Lifestyle Students**: High physical activity, adequate sleep.
- **Socially Active Students**: Moderate study, moderate social, active lifestyle.
- **Digitally Addicted Students**: High gaming or social media hours.

## Dataset Description
The dataset `students-productivity-dataset.csv` contains various features for each student, including:
- **Productivity metrics**: Study hours, focus index, productivity score.
- **Digital habits**: Social media hours, gaming hours, screen time.
- **Physical/Biological**: Sleep hours, exercise minutes, caffeine intake.
- **Academic Context**: Academic level, online classes hours.

## How the Algorithms Work

### 1. UMAP (Uniform Manifold Approximation and Projection)
UMAP is used for non-linear dimensionality reduction.
- **Purpose**: It preserves both local and global structures in high-dimensional data while projecting it into a lower-dimensional space (2D).
- **Benefit**: It makes it easier for density-based clustering algorithms like DBSCAN to find clusters compared to high-dimensional raw data.

### 2. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
DBSCAN is used for unsupervised clustering.
- **Purpose**: It groups points that are closely packed together (high density) and marks points in low-density regions as outliers (noise).
- **Parameters**: 
    - `eps`: The maximum distance between two samples for one to be considered as in the neighborhood of the other.
    - `min_samples`: The number of samples in a neighborhood for a point to be considered a core point.
- **Benefit**: Unlike K-Means, DBSCAN does not require specifying the number of clusters in advance and can find clusters of arbitrary shapes.

## Code Structure

- `lifestyle_discovery.py`: The main Python script that handles data loading, preprocessing, model application, and visualization.
- `students-productivity-dataset.csv`: The source student data.
- `lifestyle_clusters.png`: Generated visualization of the clusters.
- `students_lifestyle_discovery_results.csv`: Original data with added Cluster and Lifestyle labels.

## Installation and Usage

### Prerequisites
- Python 3.x
- Libraries: `pandas`, `numpy`, `scikit-learn`, `umap-learn`, `matplotlib`, `seaborn`

### Install Dependencies
```bash
pip install pandas scikit-learn umap-learn matplotlib seaborn
```

### Run the Model
```bash
python lifestyle_discovery.py
```

## Discovered Lifestyle Patterns
The model profiles each cluster based on the mean values of its features and assigns a category:
- **Academically Intensive**: Characterized by above-average study hours.
- **Digitally Addicted**: Characterized by high gaming or social media hours.
- **Balanced Lifestyle**: Characterized by good exercise/sleep ratios.
- **Socially Active**: Students who exhibit balanced moderate behaviors across social and academic metrics.
