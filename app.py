
import streamlit as st

from src.analysis import (
    get_analysis_data,
    get_sales_by_city,
    get_profit_by_city,
    get_sales_by_state,
    get_profit_by_state,
    get_sales_by_category,
    get_profit_by_category,
    get_high_sales_low_profit,
    get_high_sales_low_profit_cities,
    get_profit_margin,
    get_unprofitable_cities
)

from src.charts import (
    sales_by_city_chart,
    profit_by_city_chart,
    sales_by_state_chart,
    profit_by_state_chart,
    sales_by_category_chart,
    profit_by_category_chart,
    high_sales_low_profit_chart,
    high_sales_low_profit_cities_chart,
    category_margin_chart,
    unprofitable_cities_chart
)


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Superstore Dashboard",
    page_icon="⬢",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return get_analysis_data()


df = load_data()


# ============================================================
# CHECK WHETHER DATA IS AVAILABLE
# ============================================================

if df is None or df.empty:
    st.error(
        "No data is available. Please check your dataset "
        "and the get_analysis_data() function in analysis.py."
    )
    st.stop()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.title("Dashboard Filters")
st.sidebar.markdown("### Filter the data")


# State filter
states = sorted(df["State"].dropna().unique())

selected_states = st.sidebar.multiselect(
    "Select State",
    states
)


# City options depend on selected states
if selected_states:
    available_cities = sorted(
        df[df["State"].isin(selected_states)]["City"]
        .dropna()
        .unique()
    )
else:
    available_cities = sorted(
        df["City"].dropna().unique()
    )


selected_cities = st.sidebar.multiselect(
    "Select City",
    available_cities
)


# Category filter
categories = sorted(
    df["Category"].dropna().unique()
)

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories
)


# Segment filter
segments = sorted(
    df["Segment"].dropna().unique()
)

selected_segments = st.sidebar.multiselect(
    "Select Segment",
    segments
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


# Filter by state
if selected_states:
    filtered_df = filtered_df[
        filtered_df["State"].isin(selected_states)
    ]


# Filter by city
if selected_cities:
    filtered_df = filtered_df[
        filtered_df["City"].isin(selected_cities)
    ]


# Filter by category
if selected_categories:
    filtered_df = filtered_df[
        filtered_df["Category"].isin(selected_categories)
    ]


# Filter by segment
if selected_segments:
    filtered_df = filtered_df[
        filtered_df["Segment"].isin(selected_segments)
    ]


# ============================================================
# PAGE TITLE
# ============================================================

st.title("📊 Superstore Sales Dashboard")

st.markdown(
    "Analysis of sales, profit, products, "
    "cities, states and categories."
)

st.divider()


# ============================================================
# HANDLE EMPTY FILTERED RESULTS
# ============================================================

if filtered_df.empty:
    st.warning(
        "No data matches your selected filters. "
        "Please change or clear one or more filters "
        "in the sidebar."
    )

    st.info(
        "Your dashboard will display the KPIs and charts "
        "when matching data becomes available."
    )

    st.stop()


# ============================================================
# KEY PERFORMANCE INDICATORS
# ============================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

profit_margin = get_profit_margin(filtered_df)

total_orders = filtered_df["Order ID"].nunique()

total_customers = filtered_df["Customer ID"].nunique()


col1, col2, col3, col4, col5 = st.columns(5)


col1.metric(
    "Total Sales",
    f"${total_sales:,.0f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "Profit Margin",
    f"{profit_margin:.2f}%"
)

col4.metric(
    "Orders",
    f"{total_orders:,}"
)

col5.metric(
    "Customers",
    f"{total_customers:,}"
)


st.divider()


# ============================================================
# QUESTION 1
# Which cities generate the highest total sales?
# ============================================================

st.header("Top Cities by Sales")

sales_city = get_sales_by_city(filtered_df)

if sales_city is not None and not sales_city.empty:
    st.plotly_chart(
        sales_by_city_chart(sales_city),
        width="stretch"
    )
else:
    st.info("No city sales data is available for these filters.")


# ============================================================
# QUESTION 2
# Which cities generate the highest total profit?
# ============================================================

st.header("Top Cities by Profit")

profit_city = get_profit_by_city(filtered_df)

if profit_city is not None and not profit_city.empty:
    st.plotly_chart(
        profit_by_city_chart(profit_city),
        width="stretch"
    )
else:
    st.info("No city profit data is available for these filters.")


# ============================================================
# QUESTION 3
# Which states generate the most sales?
# ============================================================

st.header("Top States by Sales")

sales_state = get_sales_by_state(filtered_df)

if sales_state is not None and not sales_state.empty:
    st.plotly_chart(
        sales_by_state_chart(sales_state),
        width="stretch"
    )
else:
    st.info("No state sales data is available for these filters.")


# ============================================================
# QUESTION 4
# Which states generate the most profit?
# ============================================================

st.header("Top States by Profit")

profit_state = get_profit_by_state(filtered_df)

if profit_state is not None and not profit_state.empty:
    st.plotly_chart(
        profit_by_state_chart(profit_state),
        width="stretch"
    )
else:
    st.info("No state profit data is available for these filters.")


# ============================================================
# QUESTION 5
# Which product categories generate the highest sales?
# ============================================================

st.header("Sales by Category")

sales_category = get_sales_by_category(filtered_df)

if sales_category is not None and not sales_category.empty:
    st.plotly_chart(
        sales_by_category_chart(sales_category),
        width="stretch"
    )
else:
    st.info("No category sales data is available for these filters.")


# ============================================================
# QUESTION 6
# Which product categories generate the highest profit?
# ============================================================

st.header("Profit by Category")

profit_category = get_profit_by_category(filtered_df)

if profit_category is not None and not profit_category.empty:
    st.plotly_chart(
        profit_by_category_chart(profit_category),
        width="stretch"
    )
else:
    st.info("No category profit data is available for these filters.")


# ============================================================
# QUESTION 7
# Which products have high sales but low or negative profit?
# ============================================================

st.header("High Sales but Low Profit Products")

high_sales_low_profit = get_high_sales_low_profit(
    filtered_df
)

if (
    high_sales_low_profit is not None
    and not high_sales_low_profit.empty
):
    st.plotly_chart(
        high_sales_low_profit_chart(
            high_sales_low_profit
        ),
        width="stretch"
    )
else:
    st.info(
        "No high-sales, low-profit products were found "
        "for these filters."
    )


# ============================================================
# QUESTION 8
# Which cities have high sales but low profit?
# ============================================================

st.header("High Sales but Low Profit Cities")

high_sales_low_profit_cities = (
    get_high_sales_low_profit_cities(
        filtered_df
    )
)

if (
    high_sales_low_profit_cities is not None
    and not high_sales_low_profit_cities.empty
):
    st.plotly_chart(
        high_sales_low_profit_cities_chart(
            high_sales_low_profit_cities
        ),
        width="stretch"
    )
else:
    st.info(
        "No high-sales, low-profit cities were found "
        "for these filters."
    )


# ============================================================
# QUESTION 9
# What is the overall profit margin?
# ============================================================

st.header("Profit Margin")

st.metric(
    "Overall Profit Margin",
    f"{profit_margin:.2f}%"
)


# Calculate category margins
category_margin = (
    filtered_df
    .groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

# Avoid division by zero
category_margin["Profit Margin (%)"] = (
    category_margin["Profit"]
    .div(category_margin["Sales"].replace(0, float("nan")))
    * 100
)

category_margin = category_margin.dropna(
    subset=["Profit Margin (%)"]
)

if not category_margin.empty:
    st.plotly_chart(
        category_margin_chart(category_margin),
        width="stretch"
    )
else:
    st.info(
        "Category profit margins cannot be calculated "
        "because there are no nonzero category sales."
    )


# ============================================================
# QUESTION 10
# Which cities are unprofitable?
# ============================================================

st.header("Unprofitable Cities")

unprofitable_cities = get_unprofitable_cities(
    filtered_df
)

if (
    unprofitable_cities is not None
    and not unprofitable_cities.empty
):
    st.plotly_chart(
        unprofitable_cities_chart(
            unprofitable_cities
        ),
        width="stretch"
    )
else:
    st.info("No unprofitable cities were found for these filters.")


# ============================================================
# FILTERED DATA
# ============================================================

st.divider()

st.header("Filtered Data")

with st.expander("Show the filtered dataset"):
    st.dataframe(
        filtered_df,
        width="stretch"
    )