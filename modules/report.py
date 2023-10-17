from datetime import date
import sqlite3
import re
from datetime import date
from pathlib import Path
import pandas as pd  # pip install pandas
import plotly.express as px
import plotly.graph_objects as go
from htmltools import div, tags
from shiny import *
from shinywidgets import output_widget, register_widget, render_widget
from shiny_semantic import page_semantic
from shiny_semantic.elements import (
    button,
    header,
    icon,
    segment,
    semantic_input,
    subheader,
)
from helper.function import card, conn, df_monthly


@module.ui
def UI():
    return(
            div(
                {"class": "fifteen wide column"},
                segment(
                    header(
                        "Welcome to A-musa Data Solution",
                        subheader("""I build this dashboard using Shiny-for-python and 
                        shiny-semantic package by appsilon"""),
                        class_="big",
                    ),
                    class_="raised",
                    style_=("display: flex;" "flex-direction: column;" "justify-content: center"),
                ),
            ),
            ui.row(
                ui.column(6, card(ui.h4("Total Sales by Month"), output_widget("cearte_bar_chart"))),
                ui.column(6, card(ui.h4("Total Sales by Product"), output_widget("cearte_bar_plot"))),
            ),
            ui.row(
                ui.column(6, card(ui.h4("Top Customers by Sales"), output_widget("plot2"))),
                ui.column(6, card(ui.h4("Performance Metrics"), ui.output_table("result")))  
            ),
    ),

@module.server
def server(input, output, session):
    @output
    @render_widget
    def cearte_bar_chart():
        fig = px.bar(
            df_monthly,
            x="month_name",
            y="total_sales",
            color="total_sales",
            template="simple_white",
            text="total_sales",
        )
        
        # Set the layout
        fig.update_layout(
            title="Total Sales by Month",
            xaxis_title="Month",
            yaxis_title="Total Sales (NG)",
            yaxis_tickprefix="NG",
        )
        return go.FigureWidget(fig)

    @output
    @render_widget
    def cearte_bar_plot():
        query = '''
        SELECT p.product_name, SUM(s.total_price) as total_sales
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.product_name
        '''
        df2 = pd.read_sql_query(query, conn)
        fig = px.bar(
            df2, x="product_name", y="total_sales", template="simple_white", text="total_sales"
        )
        # Set the layout
        fig.update_layout(
            title="Total Sales by Product",
            xaxis_title="Product",
            yaxis_title="Total Sales (NG)",
            yaxis_tickprefix="NG",
        )
        return go.FigureWidget(fig)

    # Create the Plotly figure
    @output
    @render_widget
    def plot2()-> go.FigureWidget:
        # Create the Plotly figure
        # Execute the query and load results into a Pandas DataFrame
        query = '''
        SELECT c.first_name || ' ' || c.last_name as customer_name, SUM(s.total_price) as total_sales
        FROM sales s
        JOIN customers c ON s.customer_id = c.customer_id
        GROUP BY customer_name
        ORDER BY total_sales DESC
        LIMIT 10
        '''
        df1 = pd.read_sql_query(query, conn)
        fig = px.bar(
            df1, x="customer_name", y="total_sales", template="simple_white", text="total_sales"
        )

        # Set the layout
        fig.update_layout(
            title="Top Customers by Sales",
            xaxis_title="Customer",
            yaxis_title="Total Sales (NG)",
            yaxis_tickprefix="NG",
        )
        return go.FigureWidget(fig)

    @output
    @render.table
    def result():
        query = """
        SELECT 
        customers.customer_id, 
        customers.first_name || ' ' || customers.last_name as customer_name, 
        SUM(sales.total_price) as total_sales,
        CASE 
            WHEN SUM(sales.total_price) > 80000 THEN 'High Value'
            WHEN SUM(sales.total_price) > 76000 THEN 'Medium Value'
            ELSE 'Low Value'
        END as customer_segment
        FROM sales
        INNER JOIN customers ON sales.customer_id = customers.customer_id
        GROUP BY customers.customer_id
        """
        df = pd.read_sql_query(query, conn)
        ui.output_text("Table")
        return df