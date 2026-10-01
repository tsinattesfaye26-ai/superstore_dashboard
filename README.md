
# 📊 Superstore Sales Dashboard

An interactive data analytics dashboard built with Python, Streamlit, Pandas, and Plotly to analyze sales performance, profitability, product categories, cities, and states.

## 📌 Project Overview

This project explores the Sample Superstore dataset to identify sales trends, profitability patterns, and areas that may require business attention.

Users can interact with the dashboard using filters for state, city, category, and customer segment.

## 🎯 Business Questions

The dashboard answers the following 10 business questions:

1. Which cities generate the highest total sales?
2. Which cities generate the highest total profit?
3. Which states generate the most sales?
4. Which states generate the most profit?
5. Which product categories generate the highest sales?
6. Which product categories generate the highest profit?
7. Which products have high sales but low or negative profit?
8. Which cities have high sales but low profit?
9. What is the overall profit margin?
10. Which cities are unprofitable?

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Excel / XLSX dataset

## 📂 Project Structure

```text
superstore_dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── raw/
│       └── Sample_Superstore.xlsx
│
└── src/
    ├── __init__.py
    ├── analysis.py
    └── charts.py
```

## ✨ Features

- Interactive dashboard
- Sales and profit KPIs
- State, city, category, and segment filters
- Sales and profit comparisons
- Product profitability analysis
- City and state performance analysis
- Profit margin calculations
- Identification of unprofitable cities
- Interactive Plotly charts
- Filtered dataset preview
- Empty-result handling

## 🚀 Installation and Setup

### 1. Clone or download the project

Download the project folder to your computer.

### 2. Open the project folder

Open the folder in Visual Studio Code.

### 3. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 5. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 6. Run the dashboard

```powershell
python -m streamlit run app.py
```

The dashboard will open in your web browser.

## 📈 Key Performance Indicators

The dashboard displays:

- Total Sales
- Total Profit
- Profit Margin
- Total Orders
- Total Customers

## 📊 Analysis and Visualization

The dashboard includes visualizations for:

- Sales by city
- Profit by city
- Sales by state
- Profit by state
- Sales by category
- Profit by category
- High-sales, low-profit products
- High-sales, low-profit cities
- Profit margins by category
- Unprofitable cities

## 📁 Dataset

The project uses the Sample Superstore Excel dataset.

Place the dataset in:

`data/raw/Sample_Superstore.xlsx`

Make sure the file path in the data-loading code matches this location.

## 🎓 Learning Objectives

This project demonstrates practical skills in:

- Data cleaning and preparation
- Exploratory data analysis
- Business performance analysis
- Data visualization
- Python modular programming
- Interactive dashboard development
- Business insight communication

## 👩‍💻 Author

Created as a data analytics portfolio project.

## 📄 License

This project is intended for educational and portfolio purposes.