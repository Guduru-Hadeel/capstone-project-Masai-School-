# 📊 Analytics & Machine Learning Pipeline Module

This module handles data cleaning, feature engineering, and predictive modeling using the classic **Titanic Dataset**. It implements both classification models (to predict survival) and regression models (to predict ticket fares).

## 🚀 Features & Workflow Split

### 🟢 1. Data Preprocessing & Feature Engineering
* **Missing Value Imputation:** Automatically handles missing values by filling null entries in `age` and `fare` with their statistical median scores.
* **Dimensionality Reduction:** Drops sparse or redundant categorical variables (`deck` and `embarked`) to minimize model noise.
* **Categorical Encoding:** Converts qualitative data (`sex`, `embark_town`, `who`, `class`, and `alive`) into numerical formats using One-Hot Encoding (`pd.get_dummies`) with dummy variable trap protection.
* **Feature Scaling:** Standardizes features via `StandardScaler` to bring numerical values onto a uniform scale, improving gradient convergence.

### 🔵 2. Classification Pipeline (Survival Prediction)
Evaluates three distinct machine learning models to classify whether a passenger survived:
* **Logistic Regression:** Serves as a strong linear baseline algorithm.
* **Decision Tree Classifier:** Captures non-linear relationships and feature breakdowns.
* **Random Forest Classifier:** Uses ensemble learning to reduce overfitting and boost predictive accuracy.
* **Evaluation Metrics:** Outputs comprehensive confusion matrices and structural classification reports tracking precision, recall, and F1-scores.

### 🔴 3. Regression Pipeline (Fare Prediction Side-Task)
* Trains an independent ensemble model (**Random Forest Regressor**) to predict ticket prices (`fare`) based on remaining historical passenger data variables.
* Evaluates regression success criteria via **Mean Absolute Error (MAE)**, **Root Mean Squared Error (RMSE)**, and the **Coefficient of Determination (R² Score)**.

---

## 🛠️ Installation & Execution

1. **Install Core Tooling Stack:**  
   Ensure your machine learning and numerical analysis dependencies are fully installed:
   ```bash
   pip install seaborn scikit-learn matplotlib pandas numpy
   ```

2. **Run the Analytical Pipeline:**  
   Run the notebook or target python file to trigger training and output validation logs:
   ```bash
   python analytics_pipeline.py
   ```

---

## 📦 Extracted Data Artifacts
* **`titanic.csv`**: A local raw snapshot file generated during execution to save a clean physical copy of the original Seaborn dataset package records.
*
