# Student Burnout Risk Prediction

This project develops a machine learning model to predict student burnout risk levels (**Low, Medium, or High**) using behavioral and productivity data.

## 📁 Directory Structure

- **`students-productivity-dataset.csv`**: The raw dataset containing student habits (study hours, sleep, etc.) but no labels.
- **`students_with_target.csv`**: A version of the dataset after processing, including the derived `burnout_risk` target column.
- **`burnout_prediction.py`**: The primary Python script that executes the entire workflow (data loading -> label derivation -> preprocessing -> training -> evaluation).
- **`preprocessed_data.pkl`**: A serialized file containing the scaled features and target encoders for quick reuse.
- **`gb_results.pkl`**: Saved evaluation metrics and the trained Gradient Boosting model.

---

## 🧠 Approach & Methodology

### 1. Data Derivation (Label Creation)
Since the original dataset did not include a "Burnout Level," we derived a **Burnout Score** using several weighted factors:
- **Mental Health Score**: Decreasing mental health significantly increases risk.
- **Study & Online Hours**: Excessive study hours contribute to fatiguing levels.
- **Sleep Hours**: Lack of sleep is a primary driver of burnout.
- **Productivity & Focus**: Lower scores in these areas often correlate with high burnout.

The scores were then categorized into **Low, Medium, and High** risk levels using 33rd and 67th percentile quantiles to maintain a balanced dataset.

### 2. Data Preprocessing
- **Categorical Encoding**: Variables like `gender`, `academic_level`, and `internet_quality` were converted into numeric formats using `LabelEncoder`.
- **Feature Scaling**: All numeric inputs were standardized using `StandardScaler`. This ensures the Neural Network (ANN) can converge effectively and prevents features with large scales from dominating the model.
- **Data Splitting**: The data was split into **80% Training** and **20% Testing** sets.

---

## 🤖 Algorithms Used

### Algorithm 1: Gradient Boosting Classifier
Gradient Boosting is an ensemble method that builds multiple trees sequentially. Each new tree attempts to correct the errors of the previous ones.
- **Why it's used**: It is highly robust, handles non-linear relationships well, and is currently one of the most powerful algorithms for structured/tabular data.
- **Performance**: Achieved **~95.4% accuracy**.

### Algorithm 2: Artificial Neural Network (ANN)
We implemented a **Multi-Layer Perceptron (MLP)**, a type of feed-forward ANN. 
- **Architecture**:
    - **Hidden Layers**: Two dense layers with 64 and 32 neurons.
    - **Activation**: ReLU (Rectified Linear Unit) to handle non-linearity.
    - **Iteration**: 500 max iterations to allow deep learning from the data.
- **Why it's used**: ANNs can model extremely complex patterns and interactions between many variables that traditional models might miss.
- **Performance**: Achieved **~96.4% accuracy**.

---

## 🚀 How to Run the Project

1. Ensure you have the required libraries installed:
   ```bash
   pip install pandas numpy scikit-learn
   ```
2. Run the main script:
   ```bash
   python burnout_prediction.py
   ```
3. The results, including classification reports (Precision, Recall, F1-Score) for both models, will be printed in the console.

---

## 📊 Results Summary
Both models demonstrate high predictive power, with the **ANN** slightly outperforming the **Gradient Boosting** model. This suggests that the relationship between lifestyle habits and burnout risk is complex but highly predictable with modern machine learning techniques.
