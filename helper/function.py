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


def card(title, *content):
    return div(
        {"class": "five wide column"},
        header(title, class_="small"),
        segment(
            *content,
            # TODO: this is not "semantic way" :D
            style=(
                "height:100%;"
                "margin:0;"
                "display:flex;"
                "gap: 0.6em;"
                "flex-direction:column;"
                "justify-content:space-around;"
                "text-align:initial;"
            ),
        ),
    )

# Define the paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
database_path = current_dir / "sales.db"

conn = sqlite3.connect(database_path)
# Execute the query and load results into a Pandas DataFrame
query = '''
SELECT sale_date, SUM(total_price) as total_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date ASC
'''
df = pd.read_sql_query(query, conn)

# Convert sale_date to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Set the sale_date column as the index
df = df.set_index('sale_date')

# Resample the data to a monthly frequency and compute the sum
df_monthly = df.resample('M').sum()

# Map the month number to short month name
df_monthly['month_name'] = df_monthly.index.strftime('%b')

