# Diabetes Prediction System using Machine Learning

## Project Overview

This project implements a Diabetes Prediction System using Machine Learning techniques on the Pima Indians Diabetes Dataset.

The system compares two classification algorithms:

- Logistic Regression
- Decision Tree Classifier

The project includes:
- Data preprocessing
- Missing value handling
- Feature scaling
- Model training
- Performance evaluation
- Visualization
- Confusion matrix analysis

---

# Dataset

Dataset File:
- `diabetes.csv`

Target Variable:
- `Outcome`
  - 0 = Non-Diabetic
  - 1 = Diabetic

Input Features:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

---

# Project Workflow

## Step 1 — Data Loading

The dataset is loaded using Pandas.

```python
df = pd.read_csv("diabetes.csv")
