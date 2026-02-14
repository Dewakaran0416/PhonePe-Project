# 📊 PhonePe Transaction Insights Dashboard

## 🔍 Overview
This project analyzes PhonePe transaction, user, and insurance data to extract business insights.  
The data was loaded into MySQL, analyzed using SQL and Python, and visualized through a Streamlit dashboard.

## 🧰 Tech Stack
- Python
- MySQL
- Pandas
- Plotly
- Streamlit

## 📂 Dataset
Source: PhonePe Pulse GitHub repository (JSON format)

## ⚙️ Process
- Extracted JSON data from PhonePe Pulse
- Transformed and loaded into MySQL tables:
  - Aggregated (Transaction, User, Insurance)
  - Map (Transaction, User, Insurance)
  - Top (Transaction, User, Insurance)

## 📊 Key Analysis
- Top states by transaction value
- Payment type distribution
- User engagement (registered users vs app opens)
- Insurance growth trends
- Top districts and pincodes

## 📈 Dashboard Features
- KPI metrics (Total transactions, users, insurance)
- Interactive bar, pie, and line charts
- State and district level insights

## 💡 Business Insights
- UPI dominates transaction volume
- Tier-2 districts show strong user growth
- Insurance adoption is low in many regions
- High-value states are suitable for premium services

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
# PhonePe-Project
PhonePe Project
