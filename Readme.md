# 📊 Telco Customer Churn Analysis

## 🚀 Project Overview

Customer churn is one of the biggest challenges for telecom companies. This project aims to analyze customer behavior, identify churn patterns, engineer meaningful features, and build machine learning models capable of predicting customer churn.

The project follows a structured 4-week roadmap covering data analysis, feature engineering, machine learning, dashboard development, and deployment.

---

# 🎯 Project Objectives

* Analyze customer churn behavior
* Identify factors influencing churn
* Perform feature engineering
* Build predictive machine learning models
* Generate business insights and recommendations
* Develop an interactive Power BI dashboard
* Support customer retention strategies

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* PostgreSQL
* Scikit-Learn
* XGBoost
* SHAP
* Power BI
* Git & GitHub

---

# 📅 Week 1: Data Understanding & Exploratory Data Analysis (EDA)

## Objectives

* Understand dataset structure
* Clean and preprocess data
* Perform exploratory data analysis
* Identify churn patterns
* Generate initial business insights

## Tasks Completed

### Day 1

* PostgreSQL installation
* Database creation
* Dataset loading
* Database connectivity setup

### Day 2

* Data quality assessment
* Missing value identification
* Data type validation

### Day 3

* Data cleaning
* Handling missing values
* Data transformation

### Day 4

* Exploratory Data Analysis
* Statistical summaries
* Distribution analysis

### Day 5

* Churn analysis
* Customer segmentation
* Service usage analysis

### Day 6

* Encoding categorical variables
* Data preparation for ML

### Day 7

* Week 1 report preparation
* Business insights generation

---

## Key Insights from Week 1

* Customer churn rate is approximately 26.6%.
* Customers with month-to-month contracts show higher churn rates.
* Fiber Optic internet users tend to churn more frequently.
* Electronic Check payment users exhibit higher churn behavior.
* Customers with shorter tenure are more likely to leave.
* Additional services such as Online Security and Tech Support reduce churn probability.

---

# 📅 Week 2: Feature Engineering & Machine Learning

## Objectives

* Create meaningful business features
* Train predictive models
* Evaluate model performance
* Identify churn drivers

---

## Day 1: Feature Engineering

Created:

* RevenuePerMonth
* ChargeRatio
* HighValueCustomer

Outcome:
Enhanced customer profiling and spending analysis.

---

## Day 2: Customer Segmentation

Created:

* TenureGroup
* ContractRisk
* CustomerLifetimeValue

Outcome:
Improved customer segmentation and risk assessment.

---

## Day 3: Advanced Feature Engineering

Created:

* ChargesPerTenure
* ServiceUsageScore
* RiskCategory

Outcome:
Prepared final machine-learning-ready dataset.

Final Dataset Shape:

```text
7032 Rows × 43 Features
```

---

## Day 4: Logistic Regression

### Results

Accuracy: 80.38%

Confusion Matrix:

```text
[[916 117]
 [159 215]]
```

Key Finding:

* Best performing model among all tested models.

---

## Day 5: Random Forest

### Results

Accuracy: 78.54%

Confusion Matrix:

```text
[[918 115]
 [187 187]]
```

Key Finding:

* Good performance but lower than Logistic Regression.

---

## Day 6: XGBoost

### Results

Accuracy: 78.75%

Confusion Matrix:

```text
[[911 122]
 [177 197]]
```

Top Features:

* ContractRisk
* InternetService_Fiber optic
* Contract_Two year
* Contract_One year
* tenure
* OnlineSecurity_Yes
* PaymentMethod_Electronic check

---

## Day 7: Model Comparison

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 80.38%   |
| Random Forest       | 78.54%   |
| XGBoost             | 78.75%   |

### Best Model

🏆 Logistic Regression

Reason:

* Highest Accuracy
* Highest Recall
* Highest F1 Score

---

# 📈 Business Insights

### Major Churn Drivers

1. Contract Type
2. Internet Service Type
3. Customer Tenure
4. Payment Method
5. Online Security Services
6. Technical Support Services

### Recommendations

* Promote long-term contracts.
* Improve retention strategies for Fiber Optic users.
* Encourage Auto-Pay payment methods.
* Offer bundled security and support services.
* Focus on retaining new customers during early tenure periods.

---

# 📂 Project Structure

```text
customer-churn-analysis/
│
├── data/
├── week1/
├── week2/
│
├── week2_day1_feature_engineering.py
├── week2_day2_feature_engineering.py
├── week2_day3_feature_engineering.py
│
├── week2_day4_logistic_regression.py
├── week2_day5_random_forest.py
├── week2_day6_xgboost.py
│
├── week2_final_report.txt
├── README.md
│
└── requirements.txt
```

---

# 📌 Current Progress

✅ Week 1 Completed

✅ Week 2 Completed

🚀 Week 3: Power BI Dashboard Development (Next Phase)

---

## 👨‍💻 Author

**Nikhil Rana**

BCA Student | Data Analytics Enthusiast | Machine Learning Learner

GitHub:
https://github.com/nikhilrana2005
