# 📊 Customer Churn Prediction & Customer Lifetime Value (LTV) Engine

> **An End-to-End Data Analytics, Machine Learning, API Development, Dashboarding, and Docker Deployment Project**

---

# 🚀 Customer Churn Prediction & Customer Lifetime Value (LTV) Engine

## 📌 Project Overview

Customer retention has become one of the biggest challenges in the telecommunications industry. Acquiring a new customer costs significantly more than retaining an existing one. Therefore, businesses need intelligent systems capable of identifying customers who are likely to leave while also estimating the future value each customer will bring to the organization.

This project presents a complete **end-to-end Machine Learning and Data Analytics solution** that predicts customer churn risk and estimates **Customer Lifetime Value (LTV)** using historical telecom customer data.

The project follows an industry-standard Data Science workflow starting from raw data collection to deployment of a production-ready REST API using **FastAPI**, interactive business dashboards using **Metabase**, and containerization with **Docker**.

The objective is not only to build accurate machine learning models but also to demonstrate how those models can be integrated into real-world business applications.

---

# 🎯 Business Problem

Telecommunication companies lose millions of dollars every year because customers discontinue their services.

Business teams often struggle to answer questions like:

* Which customers are likely to churn?
* Which customers generate the highest lifetime revenue?
* Which customers should receive retention offers?
* How can customer segmentation improve business decisions?

Traditional reporting systems provide historical insights but fail to predict future customer behavior.

This project solves these problems using predictive analytics and machine learning.

---

# 🎯 Project Objectives

The primary objectives of this project are:

* Build an end-to-end Machine Learning pipeline.
* Analyze telecom customer behavior.
* Predict customer churn probability.
* Predict Customer Lifetime Value (LTV).
* Develop production-ready REST APIs.
* Create interactive business dashboards.
* Deploy the solution using Docker.
* Follow an industry-standard Data Science workflow.

---

# ⭐ Key Features

* 📊 Complete Data Analytics Pipeline
* 🧹 Data Cleaning & Preprocessing
* 📈 Exploratory Data Analysis (EDA)
* ⚙️ Feature Engineering
* 🤖 Customer Churn Prediction
* 💰 Customer Lifetime Value Prediction
* 📉 Explainable AI using SHAP
* 🚀 FastAPI REST API
* 📦 Batch CSV Prediction
* 📊 Interactive Metabase Dashboard
* 🐳 Docker Containerization
* 🔄 Production Ready Workflow
* 💻 Git & GitHub Version Control

---

# 🏗 Project Architecture

```text
                         IBM Telco Customer Churn Dataset
                                        │
                                        ▼
                           Data Cleaning & Preprocessing
                                        │
                                        ▼
                          Exploratory Data Analysis (EDA)
                                        │
                                        ▼
                             Feature Engineering
                                        │
                                        ▼
                  Customer Churn Prediction (Classification)
                                        │
                                        ▼
                 Customer Lifetime Value Prediction (Regression)
                                        │
                                        ▼
                         Model Serialization (.pkl Files)
                                        │
                                        ▼
                          FastAPI REST API Development
                                        │
                                        ▼
                        Batch Prediction & Single Prediction
                                        │
                                        ▼
                          Metabase Business Dashboard
                                        │
                                        ▼
                           Docker Container Deployment
```

---

# 🔄 Project Workflow

```text
Raw Dataset
      │
      ▼
Load Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Models
      │
      ▼
Model Evaluation
      │
      ▼
Customer Lifetime Value Prediction
      │
      ▼
FastAPI REST API
      │
      ▼
Swagger Documentation
      │
      ▼
Metabase Dashboard
      │
      ▼
Docker Deployment
```

---

# 📂 Dataset Information

**Dataset Name**

IBM Telco Customer Churn Dataset

The dataset contains information about telecom customers including:

* Customer Demographics
* Contract Information
* Internet Services
* Billing Details
* Payment Methods
* Customer Tenure
* Monthly Charges
* Total Charges
* Churn Status

### Dataset Statistics

* Total Records: **7043**
* Features: **21 Original Columns**
* Engineered Features Added
* Classification Target:

  * Churn
* Regression Target:

  * Customer Lifetime Value (LTV)

---

# 🧹 Data Preprocessing

Before building the machine learning models, several preprocessing techniques were applied.

### Data Cleaning

* Removed missing values
* Converted TotalCharges into numeric format
* Handled blank records
* Removed duplicate records

### Data Transformation

* Label Encoding
* Feature Scaling
* Numerical Conversion
* Boolean Conversion

### Data Validation

* Null Value Detection
* Data Type Verification
* Outlier Checking

---

# 📊 Exploratory Data Analysis (EDA)

Several exploratory analyses were performed to understand customer behavior.

The analysis included:

* Customer Distribution
* Churn Distribution
* Monthly Charges Analysis
* Total Charges Analysis
* Contract Type Analysis
* Internet Service Analysis
* Payment Method Analysis
* Senior Citizen Analysis
* Gender Analysis
* Correlation Analysis

These visualizations helped identify the major factors influencing customer churn.

---

# ⚙️ Feature Engineering

To improve prediction accuracy, several business-driven features were created.

### Engineered Features

### ContractRisk

Measures the customer's contractual risk level.

### RevenuePerMonth

Average revenue generated by the customer every month.

### ChargeRatio

Ratio between total charges and monthly charges.

### HighValueCustomer

Identifies premium customers based on revenue.

These engineered features significantly improved the predictive capability of the machine learning models.

---

# 💻 Technology Stack

## Programming Language

* Python

## Database

* PostgreSQL

## Machine Learning

* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* SHAP

## API Development

* FastAPI
* Uvicorn

## Dashboard

* Metabase

## Deployment

* Docker

## Version Control

* Git
* GitHub

## Development Tools

* VS Code
* Jupyter Notebook
* Swagger UI

---

# 📁 Project Structure

```text
customer-churn-analysis/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── feature_columns.pkl
├── scaler.pkl
├── linear_regression_ltv.pkl
├── random_forest_ltv.pkl
│
├── screenshots/
│   ├── swagger_ui.png
│   ├── prediction_api.png
│   ├── batch_prediction.png
│   ├── metabase_dashboard.png
│   └── docker_container.png
│
├── week1_*
├── week2_*
├── week3_*
├── week4_*
│
├── README.md
└── Telco-Customer-Churn.csv
```

---

# 📅 Development Timeline

The project was completed in four structured phases.

### ✅ Week 1

* Data Collection
* PostgreSQL Integration
* Data Cleaning
* Exploratory Data Analysis
* Baseline Report

### ✅ Week 2

* Feature Engineering
* Logistic Regression
* Random Forest
* XGBoost
* SHAP Explainability

### ✅ Week 3

* Customer Lifetime Value Prediction
* Linear Regression
* Random Forest Regression
* Model Serialization

### ✅ Week 4

* FastAPI Development
* Batch Prediction API
* Metabase Dashboard
* Docker Deployment
* GitHub Documentation

# 🤖 Machine Learning Models

The project uses both **classification** and **regression** algorithms to solve two different business problems.

---

# 1️⃣ Customer Churn Prediction

Customer churn prediction is a **binary classification problem**, where the model predicts whether a customer is likely to leave the telecom service.

Target Variable:

```text
Churn

0 → Customer Will Stay
1 → Customer Will Churn
```

The following machine learning models were trained and evaluated:

---

## Logistic Regression

Logistic Regression was used as the baseline classification model.

### Advantages

* Simple
* Fast
* Easy to Interpret
* Good Baseline Performance

---

## Random Forest Classifier

Random Forest combines multiple decision trees to improve prediction accuracy.

### Advantages

* Handles Non-linear Data
* Reduces Overfitting
* Better Generalization

---

## XGBoost Classifier

XGBoost was implemented as the final classification model due to its superior predictive capability.

### Advantages

* High Accuracy
* Faster Training
* Handles Complex Relationships
* Excellent Feature Importance Analysis

---

# 📈 Model Comparison

The classification models were compared based on overall predictive performance.

| Model               | Purpose                    |
| ------------------- | -------------------------- |
| Logistic Regression | Baseline Model             |
| Random Forest       | Ensemble Learning          |
| XGBoost             | Final Classification Model |

---

# 🔍 Explainable AI (SHAP)

To understand how the machine learning model makes predictions, **SHAP (SHapley Additive Explanations)** was used.

SHAP helps identify:

* Most Important Features
* Feature Contribution
* Model Transparency
* Business Interpretation

Top influential features included:

* Contract Risk
* Monthly Charges
* Total Charges
* Tenure
* Revenue Per Month

---

# 💰 Customer Lifetime Value Prediction

Customer Lifetime Value (LTV) prediction is treated as a **regression problem**.

Instead of predicting churn, regression models estimate how much revenue a customer is expected to generate over time.

---

## Linear Regression

Linear Regression served as the baseline regression model.

### Advantages

* Simple
* Fast
* Easy Interpretation

---

## Random Forest Regressor

Random Forest Regression was selected as the final regression model because it captures complex customer behavior more effectively.

### Advantages

* Higher Prediction Accuracy
* Handles Non-linear Relationships
* Robust Against Outliers

---

# 📦 Model Serialization

After training, the models were saved for deployment.

Saved Files:

```text
linear_regression_ltv.pkl

random_forest_ltv.pkl

feature_columns.pkl

scaler.pkl
```

These files are loaded automatically by the FastAPI application during runtime.

---

# 🌐 REST API Development

A production-ready REST API was developed using **FastAPI**.

FastAPI provides:

* High Performance
* Automatic Validation
* Interactive Swagger Documentation
* JSON Response Support

---

# 📌 API Endpoints

## Home Endpoint

```http
GET /
```

Purpose:

Checks whether the API is running successfully.

Example Response

```json
{
    "message":"Customer Lifetime Value Prediction API Running"
}
```

---

# Single Prediction Endpoint

```http
POST /predict
```

Purpose:

Predict Customer Lifetime Value for a single customer.

Input:

JSON

Example

```json
{
  "SeniorCitizen":0,
  "Partner":1,
  "Dependents":0,
  "tenure":12,
  "PhoneService":1,
  "PaperlessBilling":1,
  "MonthlyCharges":75.5,
  "TotalCharges":900,
  "ContractRisk":1,
  "HighValueCustomer":0,
  "RevenuePerMonth":75.5,
  "ChargeRatio":12,
  "Churn":0
}
```

Response

```json
{
   "Predicted_LTV":20.62
}
```

---

# Batch Prediction Endpoint

```http
POST /batch_predict
```

Purpose:

Upload an entire CSV file and receive predictions for every customer.

Supported Format

CSV

Output

CSV with Predicted LTV Column

---

# 📖 Swagger Documentation

FastAPI automatically generates API documentation.

Access Swagger UI:

```text
http://localhost:8000/docs
```

Features

* Interactive API Testing
* JSON Validation
* Request & Response Examples
* Live Endpoint Testing

---

# 🐳 Docker Deployment

To ensure portability and consistency, the complete application was containerized using Docker.

---

## Build Docker Image

```bash
docker build -t churn-api .
```

---

## Run Docker Container

```bash
docker run -d -p 8000:8000 --name churn-container churn-api
```

---

## Check Running Containers

```bash
docker ps
```

---

## View Container Logs

```bash
docker logs churn-container
```

---

# 📊 Business Intelligence Dashboard

Interactive dashboards were developed using **Metabase** to provide business users with valuable insights.

The dashboard enables decision-makers to analyze customer behavior without writing SQL queries.

---

# Dashboard Features

The dashboard contains multiple visualizations including:

* Total Customers
* Churn Rate
* Monthly Charges Distribution
* Contract Type Distribution
* Internet Service Analysis
* Payment Method Distribution
* Senior Citizen Analysis
* Gender Distribution
* Revenue Insights
* Customer Segmentation

These visualizations help stakeholders identify high-risk customer groups and improve retention strategies.

---

# 📷 Project Screenshots

## 1️⃣ Swagger UI

Interactive API documentation generated automatically by FastAPI.

```text
screenshots/swagger_ui.png
```

---

## 2️⃣ Customer Lifetime Value Prediction API

Demonstrates successful prediction using the `/predict` endpoint.

```text
screenshots/prediction_api.png
```

---

## 3️⃣ Batch Prediction API

Shows batch CSV upload and prediction generation using `/batch_predict`.

```text
screenshots/batch_prediction.png
```

---

## 4️⃣ Metabase Dashboard

Business dashboard displaying customer insights and KPIs.

```text
screenshots/metabase_dashboard.png
```

---

## 5️⃣ Docker Container

Docker Desktop showing the running FastAPI application container.

```text
screenshots/docker_container.png
```

---

# 📊 Business Benefits

This solution enables telecom companies to:

* Predict customer churn before it occurs.
* Identify high-value customers.
* Improve customer retention strategies.
* Optimize marketing campaigns.
* Reduce customer acquisition costs.
* Increase overall profitability.

# 💻 Installation Guide

Follow the steps below to set up the project on your local machine.

---

# 📋 Prerequisites

Make sure the following software is installed:

* Python 3.11+
* PostgreSQL
* Docker Desktop
* Git
* Visual Studio Code

---

# 📥 Clone the Repository

```bash
git clone https://github.com/nikhilrana2005/customer-churn-analysis.git
```

Navigate to the project folder:

```bash
cd customer-churn-analysis
```

---

# 🐍 Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually

```bash
pip install fastapi uvicorn pandas numpy scikit-learn joblib xgboost shap python-multipart
```

---

# ▶️ Run FastAPI Application

```bash
uvicorn app:app --reload
```

The API will start on:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t churn-api .
```

---

## Run Docker Container

```bash
docker run -d -p 8000:8000 --name churn-container churn-api
```

---

## Verify Running Container

```bash
docker ps
```

---

## Stop Container

```bash
docker stop churn-container
```

---

## Remove Container

```bash
docker rm churn-container
```

---

# 📂 Important Project Files

| File                      | Description             |
| ------------------------- | ----------------------- |
| app.py                    | FastAPI Application     |
| Dockerfile                | Docker Configuration    |
| feature_columns.pkl       | Feature Order           |
| scaler.pkl                | Feature Scaler          |
| linear_regression_ltv.pkl | Linear Regression Model |
| random_forest_ltv.pkl     | Random Forest LTV Model |
| Telco-Customer-Churn.csv  | Original Dataset        |
| README.md                 | Project Documentation   |

---

# 📊 Project Results

The project successfully demonstrates an end-to-end analytics workflow.

### Achievements

* Successfully loaded telecom customer dataset.
* Performed complete Exploratory Data Analysis (EDA).
* Created business-oriented engineered features.
* Built Customer Churn Prediction models.
* Built Customer Lifetime Value prediction models.
* Saved trained machine learning models.
* Developed REST APIs using FastAPI.
* Implemented Batch CSV Prediction.
* Built interactive dashboards using Metabase.
* Containerized the application using Docker.
* Published the complete project on GitHub.

---

# 📚 Skills Demonstrated

This project demonstrates practical experience in:

### Data Analytics

* Data Cleaning
* Data Wrangling
* Exploratory Data Analysis
* Feature Engineering

### Machine Learning

* Classification
* Regression
* Model Evaluation
* Explainable AI (SHAP)

### Backend Development

* FastAPI
* REST API Development
* JSON Request Handling

### Deployment

* Docker
* API Deployment
* Containerization

### Database

* PostgreSQL

### Business Intelligence

* Metabase Dashboard
* Business Reporting
* KPI Visualization

### Version Control

* Git
* GitHub

---

# 🎓 Learning Outcomes

During this project, the following concepts were learned and implemented:

* End-to-End Data Science Workflow
* Customer Churn Prediction
* Customer Lifetime Value Prediction
* Feature Engineering
* Machine Learning Model Building
* Model Serialization
* Explainable AI
* REST API Development
* Interactive API Documentation
* Docker Deployment
* Dashboard Development
* Production-Level Project Organization

---

# 🚀 Future Enhancements

Future improvements planned for this project include:

* User Authentication using JWT
* Role-Based Access Control
* Streamlit Frontend
* Power BI Dashboard Integration
* AWS Cloud Deployment
* Azure Deployment
* CI/CD Pipeline using GitHub Actions
* Kubernetes Deployment
* Model Monitoring
* Automatic Model Retraining
* Real-Time Prediction Service
* Database Integration for Prediction Storage

---

# 💼 Business Applications

This solution can be used by:

* Telecommunications Companies
* Banking Sector
* Insurance Companies
* Subscription-Based Businesses
* SaaS Companies
* E-Commerce Platforms

The predictive insights help organizations:

* Reduce Customer Churn
* Improve Customer Retention
* Increase Customer Satisfaction
* Optimize Marketing Campaigns
* Improve Revenue Forecasting
* Identify High-Value Customers

---

# 🌟 Highlights

* ✔ End-to-End Machine Learning Project
* ✔ Industry-Level Folder Structure
* ✔ Production-Ready REST API
* ✔ Dockerized Application
* ✔ Interactive Swagger Documentation
* ✔ Business Dashboard
* ✔ GitHub Portfolio Ready
* ✔ Real-World Business Use Case

---

# 👨‍💻 Author

## Nikhil Rana

**Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer**

### Connect with Me

* **GitHub:** https://github.com/nikhilrana2005
* **LinkedIn:** *(Add your LinkedIn Profile URL)*

---

# 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Submit a Pull Request.

---

# 📄 License

This project is developed for **educational, learning, and portfolio purposes**.

Feel free to use and modify the project for learning and personal development.

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates me to build more real-world Data Analytics and Machine Learning projects.

---

# 🎉 Conclusion

The **Customer Churn Prediction & Customer Lifetime Value (LTV) Engine** demonstrates a complete end-to-end Data Analytics and Machine Learning workflow—from raw data processing and feature engineering to predictive modeling, REST API development, business intelligence dashboards, and Docker-based deployment.

This project showcases practical skills in **Python, PostgreSQL, Machine Learning, FastAPI, Metabase, Docker, Git, and GitHub**, making it a strong portfolio project that reflects industry-standard practices and real-world business problem solving.

# 👨‍💻 About the Author

## Nikhil Rana

**Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer**

I am a passionate Data Analyst with a strong interest in Data Analytics, Machine Learning, Business Intelligence, and AI-driven solutions. I enjoy transforming raw data into meaningful insights and developing end-to-end data-driven applications that solve real-world business problems.

This project reflects my practical skills in:

* 📊 Data Analytics
* 🤖 Machine Learning
* 🐍 Python Programming
* ⚡ FastAPI
* 🗄 PostgreSQL
* 📈 Data Visualization
* 📊 Metabase Dashboarding
* 🐳 Docker
* 🌐 Git & GitHub

I am continuously learning modern technologies and building real-world projects to strengthen my expertise in Data Analytics and Machine Learning.

---

## 📬 Connect with Me

**👤 Name:** Nikhil Rana

**💻 GitHub:** https://github.com/nikhilrana2005

**🔗 LinkedIn:** www.linkedin.com/in/nikhilrana4410

**📧 Email:** nr5887253@gmail.com

---

# ⭐ Thank You

Thank you for taking the time to explore this project.

If you found this repository helpful or interesting, please consider giving it a ⭐ **Star** on GitHub. Your support motivates me to continue building impactful Data Analytics and Machine Learning projects.

I welcome feedback, suggestions, and collaboration opportunities. Feel free to connect with me to discuss data analytics, machine learning, or exciting project ideas.

**Happy Coding! 🚀**
