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



# 📅 Week 3: Customer Lifetime Value (LTV) Prediction & FastAPI Deployment

## Objectives

* Prepare Customer Lifetime Value (LTV) dataset
* Build regression models for LTV prediction
* Evaluate regression performance
* Deploy trained model using FastAPI
* Develop REST APIs for single and batch predictions
* Create API documentation using Swagger UI

---

## Day 1: Customer Lifetime Value (LTV) Preparation

### Tasks Completed

* Created Customer Lifetime Value (LTV) target variable
* Prepared regression-ready dataset
* Verified data quality
* Saved processed dataset for model training

### Dataset Summary

**Rows:** 7032

**Features:** 44

---

## Day 2: Linear Regression Model

### Results

| Metric   | Value  |
| -------- | ------ |
| MAE      | 0.00   |
| RMSE     | 0.00   |
| R² Score | 1.0000 |

### Outcome

* Successfully trained a Linear Regression model for Customer Lifetime Value prediction.
* Generated prediction results and saved the trained model.

---

## Day 3: Random Forest Regression

### Results

| Metric   | Value  |
| -------- | ------ |
| MAE      | 1.19   |
| RMSE     | 2.17   |
| R² Score | 1.0000 |

### Outcome

* Built a Random Forest Regression model.
* Compared regression performance with Linear Regression.
* Saved trained model using Joblib.
* Generated prediction dataset for evaluation.

---

## Day 4: FastAPI Project Setup

### Tasks Completed

* Installed FastAPI
* Installed Uvicorn
* Created REST API application
* Loaded trained Machine Learning model
* Verified API functionality
* Configured Swagger Documentation

### Deliverables

* FastAPI application
* Interactive API documentation
* Model loading system

---

## Day 5: Single Customer Prediction API

### Features Implemented

* Created `/predict` endpoint
* Accepted customer information through JSON
* Performed Customer Lifetime Value prediction
* Returned prediction as JSON response
* Tested successfully using Swagger UI

### Sample API Response

```json
{
    "Predicted_LTV": 20.62
}
```

---

## Day 6: Batch Prediction API

### Features Implemented

* Created `/batch_predict` endpoint
* CSV file upload support
* Batch prediction for multiple customers
* Generated prediction output file
* Successfully processed all 7032 customer records

### Output

* batch_predictions.csv

---

## Day 7: API Testing & Deployment Readiness

### Tasks Completed

* Tested all REST API endpoints
* Added file validation
* Added exception handling
* Enabled downloadable CSV output
* Completed API documentation
* Verified end-to-end workflow

### API Endpoints

| Method | Endpoint       | Description                        |
| ------ | -------------- | ---------------------------------- |
| GET    | /              | API Health Check                   |
| POST   | /predict       | Predict LTV for a Single Customer  |
| POST   | /batch_predict | Predict LTV for Multiple Customers |

---

# 📈 Week 3 Business Impact

The Customer Lifetime Value prediction system enables businesses to estimate the future value of each customer, helping management prioritize retention efforts and marketing investments.

### Benefits

* Identify high-value customers
* Improve customer retention strategy
* Support personalized marketing campaigns
* Estimate future customer revenue
* Automate prediction through REST APIs
* Enable integration with web and dashboard applications

---

# 🚀 Week 3 Achievements

✅ Customer Lifetime Value Dataset Created

✅ Linear Regression Model Developed

✅ Random Forest Regression Model Developed

✅ FastAPI REST API Built

✅ Single Customer Prediction API

✅ Batch Prediction API

✅ Swagger Documentation

✅ Model Deployment Ready






---

# 📅 Week 4: Docker Containerization, GitHub Integration & Deployment

## Objectives

- Containerize the FastAPI application using Docker
- Build and manage Docker images
- Run the application inside Docker containers
- Test API endpoints through Swagger UI
- Version control using Git & GitHub
- Prepare the project for deployment

---

## Day 1: Docker Setup

### Tasks Completed

- Installed Docker Desktop
- Configured Docker Engine
- Verified Docker installation
- Pulled the official Python Docker image

---

## Day 2: Dockerfile Creation

### Tasks Completed

- Created Dockerfile
- Configured Python runtime
- Installed project dependencies
- Exposed FastAPI port

---

## Day 3: Docker Image Build

### Tasks Completed

- Built Docker Image
- Verified image creation
- Managed Docker images

Image Name:

```
churn-api
```

---

## Day 4: Docker Container Execution

### Tasks Completed

- Created Docker container
- Mapped application port
- Successfully launched FastAPI inside Docker

Container Status:

✅ Running Successfully

---

## Day 5: API Testing using Swagger

### Tasks Completed

Successfully tested

- GET /
- POST /predict
- POST /batch_predict

Swagger URL

```
http://localhost:8000/docs
```

Example Response

```json
{
    "Predicted_LTV": 20.62
}
```

---

## Day 6: Git & GitHub Integration

### Tasks Completed

- Initialized Git Repository
- Added project files
- Created commits
- Connected Remote Repository
- Successfully pushed project to GitHub

Repository

https://github.com/nikhilrana2005/customer-churn-analysis

---

## Day 7: Project Completion

### Final Deliverables

✅ Customer Churn Analysis

✅ Customer Churn Prediction Model

✅ Customer Lifetime Value Prediction

✅ Feature Engineering Pipeline

✅ FastAPI REST API

✅ Batch Prediction API

✅ Swagger Documentation

✅ Docker Containerization

✅ Git Version Control

✅ GitHub Repository

---

# 📊 Final Project Outcome

This project demonstrates an end-to-end Machine Learning workflow covering data preprocessing, exploratory data analysis, feature engineering, predictive modeling, REST API development, Docker containerization, and version control.

The solution enables telecom businesses to:

- Predict customer churn
- Estimate customer lifetime value
- Automate predictions using REST APIs
- Support customer retention strategies
- Deploy machine learning models in production-ready environments

---

# 🎯 Skills Demonstrated

- Python Programming
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning
- Regression & Classification
- FastAPI
- REST API Development
- Docker
- Git & GitHub
- PostgreSQL
- Power BI
- Business Analytics

---

# 🏆 Project Status

# ✅ Project Completed Successfully

**Duration:** 4 Weeks

**Status:** Production Ready

**Deployment:** Docker

**API Documentation:** Swagger UI

**Repository:** GitHub

---


# 📌 Project Status

✅ Week 1 Completed

✅ Week 2 Completed

✅ Week 3 Completed

✅ Week 4 Completed

🎉 Project Successfully Completed


## 👨‍💻 Author

**Nikhil Rana**

BCA Graduate | Aspiring Data Analyst | Machine Learning Enthusiast

**GitHub:** https://github.com/nikhilrana2005

**LinkedIn:** *  www.linkedin.com/in/nikhilrana4410

t
