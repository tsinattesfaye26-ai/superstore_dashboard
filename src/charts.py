
import plotly.express as px


# ============================================================
# DASHBOARD COLORS
# ============================================================

DARK_BROWN = "#5C3A21"
BROWN = "#8B5E3C"
LIGHT_BROWN = "#F5EDE5"
WHITE = "#FFFFFF"
TEXT_BROWN = "#3E2C23"


# ============================================================
# COMMON CHART STYLE
# ============================================================

def style_chart(fig):

    fig.update_layout(
        # White chart background
        paper_bgcolor=WHITE,
        plot_bgcolor=WHITE,

        # Text
        font=dict(
            color=TEXT_BROWN,
            family="Arial"
        ),

        # Title
        title_font=dict(
            color=DARK_BROWN,
            size=20
        ),

        # X axis
        xaxis=dict(
            title_font=dict(color=DARK_BROWN),
            tickfont=dict(color=TEXT_BROWN),
            gridcolor=LIGHT_BROWN,
            linecolor=DARK_BROWN
        ),

        # Y axis
        yaxis=dict(
            title_font=dict(color=DARK_BROWN),
            tickfont=dict(color=TEXT_BROWN),
            gridcolor=LIGHT_BROWN,
            linecolor=DARK_BROWN
        ),

        # Legend
        legend=dict(
            font=dict(color=TEXT_BROWN)
        ),

        # Space around chart
        margin=dict(
            l=40,
            r=40,
            t=70,
            b=40
        )
    )

    return fig


# ============================================================
# QUESTION 1
# Which cities generate the highest total sales?
# ============================================================

def sales_by_city_chart(data):

    data = data.head(10).reset_index()

    fig = px.bar(
        data,
        x="Sales",
        y="City",
        orientation="h",
        title="Top 10 Cities by Sales",
        text_auto=".2s"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return style_chart(fig)


# ============================================================
# QUESTION 2
# Which cities generate the highest total profit?
# ============================================================

def profit_by_city_chart(data):

    data = data.head(10).reset_index()

    fig = px.bar(
        data,
        x="Profit",
        y="City",
        orientation="h",
        title="Top 10 Cities by Profit",
        text_auto=".2s"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return style_chart(fig)


# ============================================================
# QUESTION 3
# Which states generate the most sales?
# ============================================================

def sales_by_state_chart(data):

    data = data.head(10).reset_index()

    fig = px.bar(
        data,
        x="Sales",
        y="State",
        orientation="h",
        title="Top 10 States by Sales",
        text_auto=".2s"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return style_chart(fig)


# ============================================================
# QUESTION 4
# Which states generate the most profit?
# ============================================================

def profit_by_state_chart(data):

    data = data.head(10).reset_index()

    fig = px.bar(
        data,
        x="Profit",
        y="State",
        orientation="h",
        title="Top 10 States by Profit",
        text_auto=".2s"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return style_chart(fig)


# ============================================================
# QUESTION 5
# Which product categories generate the highest sales?
# ============================================================

def sales_by_category_chart(data):

    data = data.reset_index()

    fig = px.bar(
        data,
        x="Category",
        y="Sales",
        title="Sales by Category",
        text_auto=".2s"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    return style_chart(fig)


# ============================================================
# QUESTION 6
# Which product categories generate the highest profit?
# ============================================================

def profit_by_category_chart(data):

    data = data.reset_index()

    fig = px.bar(
        data,
        x="Category",
        y="Profit",
        title="Profit by Category",
        text_auto=".2s"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    return style_chart(fig)


# ============================================================
# QUESTION 7
# Which products have high sales but low or negative profit?
# ============================================================

def high_sales_low_profit_chart(data):

    data = data.head(10).reset_index()

    fig = px.scatter(
        data,
        x="Sales",
        y="Profit",
        hover_name="Product Name",
        size="Sales",
        title="High-Sales Products with Low or Negative Profit"
    )

    fig.update_traces(
        marker=dict(
            color=DARK_BROWN,
            line=dict(
                color=WHITE,
                width=1
            )
        )
    )

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color=BROWN
    )

    return style_chart(fig)


# ============================================================
# QUESTION 8
# Which cities have high sales but low profit?
# ============================================================

def high_sales_low_profit_cities_chart(data):

    data = data.head(10).reset_index()

    fig = px.scatter(
        data,
        x="Sales",
        y="Profit",
        hover_name="City",
        size="Sales",
        title="High-Sales but Low-Profit Cities"
    )

    fig.update_traces(
        marker=dict(
            color=DARK_BROWN,
            line=dict(
                color=WHITE,
                width=1
            )
        )
    )

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color=BROWN
    )

    return style_chart(fig)


# ============================================================
# QUESTION 9
# What is the overall profit margin?
# ============================================================

def category_margin_chart(data):

    data = (
        data
        .reset_index()
        .sort_values("Profit Margin (%)")
    )

    fig = px.bar(
        data,
        x="Profit Margin (%)",
        y="Category",
        orientation="h",
        title="Profit Margin by Category",
        text_auto=".2f"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    return style_chart(fig)


# ============================================================
# QUESTION 10
# Which cities are unprofitable?
# ============================================================

def unprofitable_cities_chart(data):

    data = data.head(10).reset_index()

    fig = px.bar(
        data,
        x="Profit",
        y="City",
        orientation="h",
        title="Most Unprofitable Cities",
        text_auto=".2s"
    )

    fig.update_traces(
        marker_color=DARK_BROWN
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    return style_chart(fig)