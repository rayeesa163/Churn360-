Customer360: End-to-End Customer Insight & Retention System
🚀 Customer360 is a complete analytics and AI-powered system that helps businesses understand, predict, and improve customer retention.

It combines data analysis, machine learning, and interactive dashboards (Tableau/Power BI) to deliver actionable insights into churn, retention, and customer lifetime value (LTV).

📌 Features
✅ Data Warehouse: Clean and structured customer data (Telco Churn dataset).

✅ Exploratory Analysis: Understand customer demographics, services, and churn behavior.

✅ Power BI/Tableau Dashboards:

Retention Rate

Churn Rate

Customer Lifetime Value (LTV)

Churn by Contract Type & Payment Method

High-Risk Customer Identification

✅ Machine Learning Model (Python):

Churn prediction using Logistic Regression

Achieved ~79% accuracy

Probability-based risk scoring for customers

✅ Actionable Insights: Recommendations for reducing churn.

📂 Project Structure
bash
Copy
Edit
Customer360/
│── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv   # Raw dataset
│   └── Customer360_with_predictions.csv       # Data with ML predictions
│
│── notebooks/
│   └── 01_explore_data.ipynb                  # Data exploration
│   └── 02_model_churn.ipynb                   # Churn prediction model
│
│── dashboard/
│   └── Tableau_Dashboard.twbx                 # Tableau Dashboard (interactive)
│   └── PowerBI_Dashboard.pbix                 # Power BI Dashboard (optional)
│
│── README.md                                  # Project documentation
🛠️ Tech Stack
Data Analysis: Python (Pandas, Numpy, Matplotlib, Seaborn)

Machine Learning: Scikit-learn (Logistic Regression, train-test split, evaluation)

Visualization: Tableau / Power BI

Dataset: Telco Customer Churn Dataset (IBM Sample)

📊 Dashboards
KPIs
Retention Rate

Churn Rate

High-Risk Customers (%)

Average Lifetime Value (LTV)

Visuals
Churn by Contract Type

Churn by Payment Method

High-Risk Customer Table (Top 10)

Predicted Churn Probability Distribution

🤖 Machine Learning (Churn Prediction)
Model: Logistic Regression

Accuracy: ~79%

Output: Probability of churn per customer (0–1)

Threshold: Customers with probability > 0.6 are tagged as High Risk

📢 Insights & Recommendations
Customers on Month-to-Month contracts and using Electronic Check payments have the highest churn risk.

Businesses should:

Offer incentives for longer-term contracts

Promote secure payment methods (Credit card, Auto-pay)

Provide loyalty benefits for high-value customers

🚀 How to Run
1️⃣ Clone Repo
bash
Copy
Edit
git clone https://github.com/yourusername/Customer360.git
cd Customer360
2️⃣ Run Analysis + ML Model
bash
Copy
Edit
jupyter notebook notebooks/01_explore_data.ipynb
jupyter notebook notebooks/02_model_churn.ipynb
3️⃣ Open Dashboard
Tableau → Load Tableau_Dashboard.twbx



📌 Project Impact
✔ Helps businesses understand churn drivers
✔ Provides early warning system for high-risk customers
✔ Improves customer retention & revenue

