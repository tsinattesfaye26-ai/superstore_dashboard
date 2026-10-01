from .cleaning import get_clean_data


# ============================================================
# LOAD CLEANED DATA
# ============================================================

def get_analysis_data():
    """
    Load the cleaned Superstore dataset.
    """
    return get_clean_data()


# ============================================================
# QUESTION 1
# Which cities generate the highest total sales?
# ============================================================

def get_sales_by_city(df):

    sales_by_city = (
        df.groupby("City")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return sales_by_city


# ============================================================
# QUESTION 2
# Which cities generate the highest total profit?
# ============================================================

def get_profit_by_city(df):

    profit_by_city = (
        df.groupby("City")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return profit_by_city


# ============================================================
# QUESTION 3
# Which states generate the most sales?
# ============================================================

def get_sales_by_state(df):

    sales_by_state = (
        df.groupby("State")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return sales_by_state


# ============================================================
# QUESTION 4
# Which states generate the most profit?
# ============================================================

def get_profit_by_state(df):

    profit_by_state = (
        df.groupby("State")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return profit_by_state


# ============================================================
# QUESTION 5
# Which product categories generate the highest sales?
# ============================================================

def get_sales_by_category(df):

    sales_by_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    return sales_by_category


# ============================================================
# QUESTION 6
# Which product categories generate the highest profit?
# ============================================================

def get_profit_by_category(df):

    profit_by_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
    )

    return profit_by_category


# ============================================================
# QUESTION 7
# Which products have high sales but low or negative profit?
# ============================================================

def get_high_sales_low_profit(df):

    product_performance = (
        df.groupby("Product Name")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
        .sort_values("Sales", ascending=False)
    )

    high_sales_low_profit = product_performance[
        product_performance["Profit"] <= 0
    ]

    return high_sales_low_profit


# ============================================================
# QUESTION 8
# Which cities have high sales but low profit?
# ============================================================

def get_high_sales_low_profit_cities(df):

    city_performance = (
        df.groupby("City")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
    )

    high_sales_low_profit_cities = (
        city_performance[
            (city_performance["Sales"] > city_performance["Sales"].median())
            &
            (city_performance["Profit"] < city_performance["Profit"].median())
        ]
        .sort_values("Sales", ascending=False)
    )

    return high_sales_low_profit_cities


# ============================================================
# QUESTION 9
# What is the overall profit margin?
# ============================================================

def get_profit_margin(df):

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    if total_sales == 0:
        return 0

    profit_margin = (
        total_profit / total_sales
    ) * 100

    return profit_margin


# ============================================================
# QUESTION 10
# Which cities are unprofitable?
# ============================================================

def get_unprofitable_cities(df):

    city_performance = (
        df.groupby("City")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum")
        )
    )

    unprofitable_cities = (
        city_performance[
            city_performance["Profit"] < 0
        ]
        .sort_values("Profit")
    )

    return unprofitable_cities