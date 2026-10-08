# E-Commerce Customer Churn and Sales Trend Analysis

A Python analysis project using Pandas and NumPy to evaluate e-commerce sales performance, category revenue distributions, and customer retention metrics.

## Overview

This project analyzes transactional e-commerce data to identify revenue trends, category performance, and customer churn risks using Recency, Frequency, and Monetary segmentation.

## Features

- **Date Feature Extraction:** Parses transaction dates to extract monthly and quarterly periods.
- **Revenue Calculations:** Computes total transaction revenue from quantity and price metrics.
- **Pivot Table Aggregations:** Summarizes revenue trends by month and product category.
- **RFM Customer Segmentation:** Categorizes buyers by purchase recency, transaction frequency, and total spend.
- **Churn Identification:** Flags customers with no purchases in over 90 days as potential churn risks.

## Tech Stack

- Python
- Pandas
- NumPy

## How to Run

Execute the script in Google Colab or locally via command line:

```bash
python customer_churn_sales_trend.py
