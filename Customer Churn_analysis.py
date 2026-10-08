import pandas as pd
import numpy as np

# 1. Create E-Commerce Sales Dataset
data = {
    'OrderID': range(101, 121),
    'CustomerID': [1001, 1002, 1001, 1003, 1004, 1002, 1005, 1001, 1006, 1003,
                   1007, 1004, 1002, 1008, 1005, 1001, 1009, 1003, 1006, 1010],
    'OrderDate': pd.to_datetime([
        '2025-01-15', '2025-01-18', '2025-02-10', '2025-02-14', '2025-03-01',
        '2025-03-05', '2025-03-20', '2025-04-02', '2025-04-11', '2025-05-04',
        '2025-05-18', '2025-06-01', '2025-06-15', '2025-07-01', '2025-07-22',
        '2025-08-05', '2025-08-19', '2025-09-02', '2025-09-14', '2025-10-01'
    ]),
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing',
                 'Electronics', 'Home', 'Clothing', 'Electronics', 'Home',
                 'Clothing', 'Electronics', 'Clothing', 'Home', 'Electronics',
                 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home'],
    'Quantity': [2, 5, 1, 3, 4, 1, 2, 6, 1, 2, 3, 1, 2, 4, 1, 3, 2, 1, 5, 1],
    'UnitPrice': [1500, 800, 12000, 2500, 600, 25000, 3000, 750, 45000, 1800,
                  950, 18000, 1100, 3200, 15000, 850, 2200, 30000, 650, 4000]
}

df = pd.DataFrame(data)

# 2. Feature Engineering and Date Extraction
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.strftime('%Y-%m')
df['Quarter'] = df['OrderDate'].dt.to_period('Q')

print("=== DATASET OVERVIEW ===")
print(df.head())

# 3. Pivot Tables and Trend Calculations
print("\n=== MONTHLY REVENUE TREND ===")
monthly_trend = df.pivot_table(index='Month', values='TotalSales', aggfunc=['sum', 'count'])
monthly_trend.columns = ['Total Revenue', 'Order Count']
print(monthly_trend)

print("\n=== REVENUE BY PRODUCT CATEGORY ===")
category_summary = df.pivot_table(index='Category', values='TotalSales', aggfunc=['sum', 'mean', 'count'])
category_summary.columns = ['Total Revenue', 'Average Order Value', 'Order Count']
print(category_summary)

# 4. Customer Segmentation and Churn Analysis
snapshot_date = df['OrderDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'OrderDate': lambda x: (snapshot_date - x.max()).days,
    'OrderID': 'count',
    'TotalSales': 'sum'
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Categorize customer status based on purchase recency
rfm['Status'] = np.where(rfm['Recency'] > 90, 'Churn Risk', 'Active')

print("\n=== CUSTOMER RFM AND CHURN ANALYSIS ===")
print(rfm)

print("\n=== CHURN SUMMARY ===")
churn_summary = rfm.groupby('Status').agg({'CustomerID': 'count', 'Monetary': 'mean'})
churn_summary.columns = ['Customer Count', 'Average Revenue']
print(churn_summary)

# 5. Actionable Business Recommendations
print("\n=== ACTIONABLE BUSINESS RECOMMENDATIONS ===")
print("1. Target Churn Risk customers with re-engagement email discounts.")
print("2. Focus promotional budgets on high-revenue categories like Electronics.")
print("3. Launch VIP rewards for repeat buyers with high Monetary value.")