"""
Student Burnout Risk Prediction
-------------------------------
Assignment: Develop a model to predict burnout risk (Low, Medium, High)
Algorithms: Gradient Boosting Classifier, Artificial Neural Network (ANN)
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

# 1. Load Dataset
print("Loading dataset...")
df = pd.read_csv("students-productivity-dataset.csv")

# 2. Derive Target Variable (Burnout Risk)
# Since the original dataset only contains behavioral metrics, 
# we derive the Burnout Risk level based on a combination of:
# - Mental Health Score (Lower is higher risk)
# - Study Hours (Higher is higher potential risk/fatigue)
# - Sleep Hours (Lower is higher risk)
# - Productivity Score (Lower is higher risk)

print("Deriving 'burnout_risk' labels...")
# Heuristic score calculation
df['burnout_score'] = (
    (10 - df['mental_health_score']) * 2 + 
    (df['study_hours'] + df['self_study_hours']) * 0.5 + 
    (df['screen_time_hours'] * 0.5) - 
    (df['sleep_hours'] * 1.5) - 
    (df['productivity_score'] / 10)
)

# Splitting into Low, Medium, High categories using quantiles for balance
quantiles = df['burnout_score'].quantile([0.33, 0.67]).values
def assign_risk(score):
    if score <= quantiles[0]: return 'Low'
    elif score <= quantiles[1]: return 'Medium'
    else: return 'High'

df['burnout_risk'] = df['burnout_score'].apply(assign_risk)
print(f"Burnout Risk Distribution:\n{df['burnout_risk'].value_counts()}\n")

# 3. Preprocessing
print("Preprocessing data...")
# Drop target and helper columns from features
X = df.drop(['student_id', 'burnout_score', 'burnout_risk'], axis=1)
y = df['burnout_risk']

# Encode Categorical Features
categorical_cols = X.select_dtypes(include=['object']).columns
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# Encode Target
le_target = LabelEncoder()
y_encoded = le_target.fit_transform(y)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Scale features (especially important for the Neural Network)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Gradient Boosting Classifier
print("-" * 30)
print("ALGORITHM 1: Gradient Boosting Classifier")
gb_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_model.fit(X_train_scaled, y_train)
y_pred_gb = gb_model.predict(X_test_scaled)

print(f"Accuracy: {accuracy_score(y_test, y_pred_gb):.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred_gb, target_names=le_target.classes_))

# 5. Artificial Neural Network (ANN)
print("-" * 30)
print("ALGORITHM 2: Artificial Neural Network (MLP)")
# Using Multi-layer Perceptron (MLP) as the ANN implementation
ann_model = MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42)
ann_model.fit(X_train_scaled, y_train)
y_pred_ann = ann_model.predict(X_test_scaled)

print(f"Accuracy: {accuracy_score(y_test, y_pred_ann):.4f}")
print("Classification Report:")
print(classification_report(y_test, y_pred_ann, target_names=le_target.classes_))

print("-" * 30)
print("Process completed successfully.")
