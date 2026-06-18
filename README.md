# Improved Detection of Fraud Cases for E-commerce and Bank Transactions

## Project Overview

This project develops machine learning models to detect fraudulent transactions across two different transaction streams:

1. **E-commerce Transactions (Fraud_Data.csv)** – includes user behavior, device information, transaction details, and geolocation features.
2. **Bank Credit Card Transactions (creditcard.csv)** – contains anonymized PCA-transformed transaction features.

The goal is to improve fraud detection while balancing the trade-off between false positives (legitimate transactions incorrectly flagged as fraud) and false negatives (fraudulent transactions that go undetected).

---

## Business Problem

Fraudulent transactions cause significant financial losses and damage customer trust. Traditional accuracy metrics are often misleading because fraud datasets are highly imbalanced, with fraudulent transactions representing only a small fraction of all transactions.

This project aims to:

* Detect fraudulent transactions more accurately.
* Handle severe class imbalance.
* Interpret model predictions using explainable AI techniques.
* Provide actionable business recommendations.

---

## Dataset Description

### 1. Fraud_Data.csv

Contains e-commerce transaction information including:

* user_id
* signup_time
* purchase_time
* purchase_value
* device_id
* source
* browser
* sex
* age
* ip_address
* class (target)

### 2. IpAddress_to_Country.csv

Maps IP address ranges to countries for geolocation enrichment.

### 3. creditcard.csv

Contains anonymized credit card transaction features:

* Time
* V1–V28 (PCA features)
* Amount
* Class (target)

---

## Project Structure

```text
fraud-detection/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── eda-fraud-data.ipynb
│   ├── eda-creditcard.ipynb
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   └── shap-explainability.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── config.py
│
├── models/
├── tests/
├── scripts/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Data Preprocessing

The following preprocessing steps were performed:

### Data Cleaning

* Removed duplicate records.
* Corrected data types.
* Converted timestamps into datetime format.
* Checked and handled missing values.

### Geolocation Integration

* Converted IP addresses to integer format.
* Merged Fraud_Data.csv with IpAddress_to_Country.csv.
* Added country information for fraud analysis.

### Feature Engineering

Created the following fraud-specific features:

* time_since_signup
* hour_of_day
* day_of_week
* user_transaction_count
* device_transaction_count

### Data Transformation

* One-hot encoding for categorical variables.
* Numerical feature scaling where appropriate.
* Train-test split using stratification.

### Handling Class Imbalance

SMOTE (Synthetic Minority Oversampling Technique) was applied only to the training set to avoid data leakage.

---

## Exploratory Data Analysis

EDA was performed separately for both datasets.

Key findings:

* Fraudulent transactions represent a very small percentage of total transactions.
* Fraud is associated with shorter signup-to-purchase times.
* Certain devices and IP ranges exhibit higher fraud activity.
* Transaction timing patterns provide useful fraud signals.

---

## Model Development

### Baseline Model

**Logistic Regression**

Used as an interpretable baseline model.

Evaluation Metrics:

* AUC-PR
* F1 Score
* Confusion Matrix

### Ensemble Model

**Random Forest Classifier**

Hyperparameter tuning was performed using GridSearchCV.

Parameters explored:

* n_estimators
* max_depth

---

## Model Performance

### Fraud_Data Dataset

| Model               | AUC-PR | F1 Score |
| ------------------- | ------ | -------- |
| Logistic Regression | 0.0954 | 0.1649   |
| Random Forest       | 0.7096 | 0.6959   |

### Credit Card Dataset

| Model               | AUC-PR                                    | F1 Score |
| ------------------- | ----------------------------------------- | -------- |
| Logistic Regression | 0.7206                                    | 0.2063   |
| Random Forest       | Higher-performing ensemble model selected |          |

### Cross Validation

Stratified K-Fold Cross Validation was used to assess model stability.

The Random Forest model demonstrated strong and consistent performance across folds.

---

## Model Selection

Random Forest was selected as the final model because it achieved the highest fraud detection performance based on:

* AUC-PR
* F1 Score
* Confusion Matrix analysis

The model effectively captured nonlinear relationships and complex fraud patterns.

---

## Model Explainability (SHAP)

SHAP (SHapley Additive exPlanations) was used to interpret model behavior.

### Top Fraud Drivers

1. time_since_signup
2. device_transaction_count
3. ip_address
4. lower_bound_ip_address
5. upper_bound_ip_address

### Key Findings

* Transactions occurring shortly after account creation are significantly more likely to be fraudulent.
* Devices with unusually high transaction activity show elevated fraud risk.
* IP-related features provide important geographic and network fraud signals.

### SHAP Visualizations

The project includes:

* SHAP Summary Plot
* True Positive Force Plot
* False Positive Force Plot
* False Negative Force Plot

These visualizations explain both global model behavior and individual predictions.

---

## Business Recommendations

### 1. Enhanced Verification for New Accounts

Require additional verification for transactions occurring shortly after account creation.

### 2. Device-Level Fraud Monitoring

Monitor devices exhibiting unusually high transaction frequencies.

### 3. Geolocation Risk Screening

Apply additional screening to transactions originating from suspicious IP ranges and regions.

### 4. Real-Time Fraud Scoring

Deploy the trained model in a real-time fraud detection pipeline to evaluate transactions before approval.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd fraud-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run notebooks in the following order:

1. eda-fraud-data.ipynb
2. eda-creditcard.ipynb
3. feature-engineering.ipynb
4. modeling.ipynb
5. shap-explainability.ipynb

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)
* SHAP
* Jupyter Notebook

---

## Author

Melat Dagnachew

10 Academy – Week 5 & 6 Fraud Detection Challenge

