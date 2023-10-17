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



@module.ui
def UI():
    return(
            div(
                {"class": "fifteen wide column"},
                segment(
                    header(
                        "Amusa Data Solution",
                        subheader("Shiny-for-python and shiny-semantic"),
                        class_="big",
                    ),
                    class_="raised",
                    style_=("display: flex;" "flex-direction: column;" "justify-content: center"),
                ),
            ),
            card(
                "Register Customers",
                div(
                    {"class": "ten wide column"},
                    segment(
                        ui.row(
                            ui.column(
                                6,
                                semantic_input(
                                    "numeric",
                                    placeholder="Numeric input with Props",
                                    type="number",
                                    value=0,
                                    min=-10,
                                    max=10,
                                    step=10,
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "error", placeholder="Error", semantic_class="massive, fluid"
                                ),
                                semantic_input(
                                    "date", placeholder="Date", type="date", semantic_class="fluid"
                                ),
                                semantic_input(
                                    "email",
                                    placeholder="Email",
                                    type="email",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "password",
                                    placeholder="Password",
                                    type="password",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "icon",
                                    placeholder="With Icon",
                                    type="users",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "value",
                                    placeholder="Pre-populated",
                                    value="Some text",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "numeric",
                                    placeholder="Numeric",
                                    type="number",
                                    semantic_class="fluid",
                                ),
                                button("btn5", "Submit", class_="primary", icon=icon("facebook")),
                            ),
                            ui.column(
                                6,
                                semantic_input(
                                    "numeric",
                                    placeholder="Numeric input with Props",
                                    type="number",
                                    value=0,
                                    min=-10,
                                    max=10,
                                    step=10,
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "error", placeholder="Error", semantic_class="massive, fluid"
                                ),
                                semantic_input(
                                    "date", placeholder="Date", type="date", semantic_class="fluid"
                                ),
                                semantic_input(
                                    "email",
                                    placeholder="Email",
                                    type="email",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "password",
                                    placeholder="Password",
                                    type="password",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "icon",
                                    placeholder="With Icon",
                                    type="users",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "value",
                                    placeholder="Pre-populated",
                                    value="Some text",
                                    semantic_class="fluid",
                                ),
                                semantic_input(
                                    "numeric",
                                    placeholder="Numeric",
                                    type="number",
                                    semantic_class="fluid",
                                ),
                                button("btn5", "Submit", class_="primary", icon=icon("facebook")),
                            ),
                        ),
                        class_="piled",
                        style_=(
                            "display: flex;"
                            "flex-direction: column;"
                            "justify-content: space-around"
                        ),  # end of calss in segment for style
                    ),  # Closing segmanent
                ),
            ),
            ),
@module.server
def server(input, output, session):
    pass