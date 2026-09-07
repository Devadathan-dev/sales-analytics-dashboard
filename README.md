# Sales Analytics Dashboard

Interactive sales analytics dashboard built with Streamlit, Pandas, and Plotly.

## Features

- View total sales, profit, orders, and quantity as KPI cards
- Explore monthly sales trend, sales by region, sales by category, and top 10 products
- Filter data by month, region, and category
- Reset filters to restore full dataset view
- Handles empty selection with a friendly “No data found” message

## Live Demo

https://sales-analytics-dashboard-qs5edvqghjrzebj8ne6w97.streamlit.app/

## How to run locally

   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

## Tech Stack

- Streamlit
- Pandas
- Plotly Express

## Dataset

This dashboard uses a sample `sales_data.csv` file with columns such as Order Date, Region, Category, Product Name, Sales, Profit, and Quantity.
