# Principal Component Analysis (PCA) Implementation

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Step 1: Create Dataset
data = {
    'Internal': [45, 50, 48, 60, 55],
    'Assignment': [30, 28, 35, 40, 38],
    'Attendance': [98, 99, 100, 76, 89],
    'FinalExam': [85, 87, 96, 69, 88]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)

# Step 2: Standardize the Data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

print("\nStandardized Data:\n", scaled_data)

# Step 3: Apply PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

# Step 4: Create DataFrame for Principal Components
pca_df = pd.DataFrame(
    data=principal_components,
    columns=['Principal Component 1', 'Principal Component 2']
)

print("\nPrincipal Components:\n", pca_df)

# Step 5: Display Explained Variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Variance Retained:")
print(np.sum(pca.explained_variance_ratio_))
