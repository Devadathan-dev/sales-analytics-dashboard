import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")

st.title("Sales Analytics Dashboard")
st.subheader("Sales Data Preview")

try:
    df = pd.read_csv("sales_data.csv")
except FileNotFoundError:
    st.error("sales_data.csv could not be found.")
    st.stop()
    
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

st.sidebar.header("Filter Data")

filtered_df = df.copy()

if "month_filter" not in st.session_state:
    st.session_state.month_filter = []
if "region_filter" not in st.session_state:
    st.session_state.region_filter = []
if "category_filter" not in st.session_state:
    st.session_state.category_filter = []

def reset_filters():
    st.session_state.month_filter = []
    st.session_state.region_filter = []
    st.session_state.category_filter = []

month_filter = st.sidebar.multiselect("Select Month", df["Month"].unique(), key="month_filter")
region_filter = st.sidebar.multiselect("Select Region", df["Region"].unique(), key="region_filter")
category_filter = st.sidebar.multiselect("Select Category", df["Category"].unique(), key="category_filter")


if month_filter:
    filtered_df = filtered_df[filtered_df["Month"].isin(month_filter)]

if region_filter:
    filtered_df = filtered_df[filtered_df["Region"].isin(region_filter)]

if category_filter:
    filtered_df = filtered_df[filtered_df["Category"].isin(category_filter)]                                        

if filtered_df.empty:
    st.warning("No data found for the selected filters")
    st.stop()

st.sidebar.button("Reset Filters", on_click=reset_filters)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Sales", f"₹{filtered_df['Sales'].sum():,.0f}")
kpi2.metric("Total Profit", f"₹{filtered_df['Profit'].sum():,.0f}")
kpi3.metric("Total Orders", filtered_df.shape[0])
kpi4.metric("Total Quantity", filtered_df["Quantity"].sum())

monthly_sales = filtered_df.groupby("Month", as_index=False)["Sales"].sum()
fig = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)
st.plotly_chart(fig, width="stretch")


region_sales = filtered_df.groupby("Region", as_index=False)["Sales"].sum()
fig_region = px.bar(region_sales, x="Region", y="Sales", title="Sales by Region")
st.plotly_chart(fig_region, width="stretch")

category_sales = filtered_df.groupby("Category", as_index=False)["Sales"].sum()
fig_category = px.pie(category_sales, names="Category", values="Sales",  title="Sales by Category")
st.plotly_chart(fig_category, width="stretch")

top_products = filtered_df.groupby("Product", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False).head(10)

fig_products = px.bar(top_products, x="Sales", y="Product", orientation="h", title="Top 10 Products by Sales")
st.plotly_chart(fig_products, width="stretch")

st.write("Dataset shape:", filtered_df.shape)
st.write("Filtered Data")
st.dataframe(filtered_df)
