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
from helper.function import card
import modules

### Front-End Code
app_ui = page_semantic(
        ui.page_navbar(
                        ui.nav(
            "Home",
            modules.report.UI("report")
            ),
            ui.nav(
            "Report",
            modules.home.UI("home")
         ),
        bg="#454545",
        title="Market Stock Analytics",
        inverse=True,
        id="navbar_id",
        footer=ui.div(
            {"style": "width:80%;margin: 0 auto"},
        ui.tags.style("""h4 {margin-top: 3em;}"""),),
        ),
        tags.style("body{background-color:#17a2b8;} .segment{transition: all 150ms linear;}"),
        tags.script("""
            $(".segment").mouseenter(e => $(e.currentTarget).toggleClass("raised"));
            $(".segment").mouseleave(e => $(e.currentTarget).toggleClass("raised"));
            """),
        title="A-musa-pyshiny",
)

def server(input, output, session):
    modules.report.server("report")
    modules.home.server("home")
  

app = App(app_ui, server)
