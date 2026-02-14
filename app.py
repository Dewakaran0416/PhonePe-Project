import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 PhonePe Transaction Insights Dashboard")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0923",
    database="phonepe"
)
def run_query(query):
    return pd.read_sql(query, conn)
col1, col2, col3 = st.columns(3)

total_txn = run_query("SELECT SUM(transaction_amount) AS total FROM aggregated_transaction")
total_users = run_query("SELECT SUM(registered_users) AS users FROM map_user")
total_ins = run_query("SELECT SUM(insurance_amount) AS ins FROM aggregated_insurance")

col1.metric("Total Transaction Amount", f"₹{int(total_txn['total'][0]):,}")
col2.metric("Total Users", f"{int(total_users['users'][0]):,}")
col3.metric("Total Insurance Amount", f"₹{int(total_ins['ins'][0]):,}")
df_state = run_query("""
SELECT state, SUM(transaction_amount) AS total
FROM aggregated_transaction
GROUP BY state
ORDER BY total DESC
LIMIT 10
""")

fig1 = px.bar(df_state, x="state", y="total", title="Top 10 States by Transaction Amount")
st.plotly_chart(fig1, use_container_width=True)
df_type = run_query("""
SELECT transaction_type, SUM(transaction_count) AS total
FROM aggregated_transaction
GROUP BY transaction_type
""")

fig2 = px.pie(df_type, names="transaction_type", values="total", title="Payment Type Distribution")
st.plotly_chart(fig2, use_container_width=True)
df_year = run_query("""
SELECT year, SUM(transaction_amount) AS total
FROM aggregated_transaction
GROUP BY year
ORDER BY year
""")

fig3 = px.line(df_year, x="year", y="total", title="Yearly Transaction Trend")
st.plotly_chart(fig3, use_container_width=True)
df_dist = run_query("""
SELECT district, SUM(registered_users) AS users
FROM map_user
GROUP BY district
ORDER BY users DESC
LIMIT 10
""")

fig4 = px.bar(df_dist, x="district", y="users", title="Top Districts by Users")
st.plotly_chart(fig4, use_container_width=True)
df_dist = run_query("""
SELECT district, SUM(registered_users) AS users
FROM map_user
GROUP BY district
ORDER BY users DESC
LIMIT 10
""")


fig5 = px.line(df_ins, x="year", y="total", title="Insurance Growth Trend")
st.plotly_chart(fig5, use_container_width=True)

