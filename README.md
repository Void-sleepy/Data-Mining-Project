# Credit Risk Prediction - Data Mining Project

This repository contains a comprehensive machine learning pipeline designed to predict credit risk (Loan Default). The project and its visualizations are structured and formatted for an IEEE academic paper, focusing on rigorous evaluation and the handling of highly imbalanced datasets.

## Overview

The goal of this project is to accurately predict whether a borrower will default on a loan (`loan_status` = 1) or not (0). Due to the highly imbalanced nature of credit risk data, standard accuracy is not a reliable metric. Therefore, the models are natively trained using class-weighting penalties and evaluated using advanced metrics well-suited for finance scopes and academic publishing.

## Models Evaluated

We implement and compare several tree-based classifiers and ensembles:
* **Decision Tree** (Gini Impurity)
* **Decision Tree** (Entropy / Information Gain)
* **Random Forest**
* **AdaBoost**
* **Gradient Boosting**
* **XGBoost**

Each model is configured to penalize false negatives for the minority class natively (e.g., `class_weight='balanced'`, `scale_pos_weight`, or balanced base estimators).

## Evaluation Metrics & Visualizations

To provide a thorough and academically rigorous comparison, each notebook outputs the following:
* **Key Metrics**: Accuracy, Macro F1 Score, Matthews Correlation Coefficient (MCC), and Scikit-Learn Classification Reports.
* **Confusion Matrix**: Test set performance breakdown (`N=5726`).
* **ROC Curve**: Receiver Operating Characteristic curve.
* **Precision-Recall Curve**: Essential for evaluating performance on the imbalanced minority class.
* **Calibration Curve (Reliability Diagram)**: Analyzes how well the predicted probabilities align with actual default frequencies.
* **Feature Importance**: Bar chart highlighting the most predictive features.
* **Tree Visualizations**: Interpretability graphs mapping decision nodes.

## Project Structure

```text
Data-Mining-Project/
├── dataset/
│   ├── credit_risk_dataset.csv    # Raw dataset
│   └── clean.csv                  # Preprocessed and cleaned dataset ready for modeling
├── model_save/                    # Serialized models exported as .pkl (Pickle) files
├── clean.ipynb                    # Data cleaning and preparation notebook
├── decision_tree.ipynb            # Decision Tree Model (Gini)
├── decision_tree_entropy.ipynb    # Decision Tree Model (Entropy)
├── random_forest.ipynb            # Random Forest Model
├── adaboost.ipynb                 # AdaBoost Ensemble
├── gradient_boosting.ipynb        # Gradient Boosting Machine
└── xgboost.ipynb                  # Extreme Gradient Boosting (XGBoost)
```

## Usage

1. **Data Preparation**: Start by running `clean.ipynb` to process `dataset/credit_risk_dataset.csv` and generate the standardized `dataset/clean.csv`.
2. **Model Training & Evaluation**: Execute any of the model notebooks (e.g., `xgboost.ipynb`). The notebooks will load the cleaned data, train the model with class weights, display all IEEE-grade visualizations, and automatically save the trained model to the `model_save/` directory as a `.pkl` file.
