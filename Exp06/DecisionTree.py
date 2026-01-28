import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# -----------------------------
# 1. Realistic Dataset
# -----------------------------
data = {
    'Age': [18, 22, 25, 30, 35, 40, 45, 50, 55, 60,
            23, 27, 33, 38, 42, 47, 52, 58],
    'EstimatedSalary': [12000, 18000, 25000, 32000, 40000, 48000,
                        52000, 60000, 70000, 90000,
                        20000, 28000, 36000, 45000, 55000,
                        65000, 80000, 100000],
    'Purchased': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
                  0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Features & Target
# -----------------------------
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -----------------------------
# 4. Feature Scaling
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# 5. Train Decision Tree
# -----------------------------
model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
    min_samples_split=2,
    random_state=42
)

model.fit(X_train_scaled, y_train)

# -----------------------------
# 6. Evaluate Model
# -----------------------------
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# -----------------------------
# 7. Take User Input
# -----------------------------
print("\n--- Enter Customer Details ---")
age = int(input("Enter Age: "))
salary = int(input("Enter Estimated Salary: "))

user_data = pd.DataFrame([[age, salary]], columns=['Age', 'EstimatedSalary'])
user_data_scaled = scaler.transform(user_data)

# -----------------------------
# 8. Predict for User Input
# -----------------------------
result = model.predict(user_data_scaled)

print("\nPrediction Result:")
if result[0] == 1:
    print("Customer WILL Purchase the Product")
else:
    print("Customer will NOT Purchase the Product")

# -----------------------------
# 9. Product & Price Mapping
# -----------------------------
if result[0] == 1:
    if salary < 30000:
        product = "Basic Plan"
        price = 4999
    elif salary <= 60000:
        product = "Standard Plan"
        price = 9999
    else:
        product = "Premium Plan"
        price = 19999

    print("\nPurchase Recommendation")
    print("--------------------------")
    print(f"Product   : {product}")
    print(f"Price     : ₹{price}")
    print("Status    : Recommended to Buy")
else:
    print("\nPurchase Recommendation")
    print("Status    : Not recommended based on current data")

