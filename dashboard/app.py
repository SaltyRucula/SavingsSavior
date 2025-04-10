from nicegui import ui
import pandas as pd
import numpy as np
import plotly.graph_objects as go

np.random.seed(42)
years = np.arange(2020, 2026)
monthly_profits = pd.DataFrame(
    {year: np.random.randint(50000, 150000, size=12) for year in years}
)
asset_types = ["Active", "Passive"]
asset_values = np.random.randint(100000, 1000000, size=len(asset_types))
total_asset_value = asset_values.sum()
yearly_total_profits = monthly_profits.sum().values
all_time_start_value = 1000000
all_time_end_value = all_time_start_value + yearly_total_profits.sum()


class Card(ui.card):
    def __init__(self, title, content):
        super().__init__()
        self.classes("w-full p-4")
        with self:
            (ui.label(title).classes("text-h6 text-center text-weight-bold"),)
            (ui.label(content).classes("text-h4 text-center"),)


# --- Helper Functions for Plotting ---
def create_pie_chart(labels, values, title):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
    fig.update_layout(title_text=title, title_x=0.5)
    return fig


def create_bar_chart(x, y, title, y_title):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title_text=title, title_x=0.5, yaxis_title=y_title)
    return fig


def create_indicator(value, title, color="primary"):
    return Card(title, value).classes("w-full p-4")


# --- Dashboard Layout ---
@ui.page("/")
def home():
    ui.markdown("# Asset Performance Dashboard").classes("text-h3 text-center")

    with ui.row().classes("w-full justify-around"):
        # Asset Share
        asset_share_fig = create_pie_chart(
            labels=asset_types, values=asset_values, title="Asset Share (%)"
        )
        ui.plotly(asset_share_fig).classes("md:w-1/3 w-full")

        # Yearly Profits
        yearly_profits_fig = create_bar_chart(
            x=years.astype(str),
            y=yearly_total_profits,
            title="Yearly Profits ($)",
            y_title="Profit ($)",
        )
        ui.plotly(yearly_profits_fig).classes("md:w-1/3 w-full")

        # All Time Performance
        all_time_performance = (
            (all_time_end_value - all_time_start_value) / all_time_start_value
        ) * 100
        color = "positive" if all_time_performance >= 0 else "negative"
        indicator_all_time = create_indicator(
            f"{all_time_performance:.2f}%", "All Time Performance (%)", color=color
        )
        with ui.column().classes("md:w-1/4 w-full"):
            indicator_all_time

    with ui.row().classes("w-full justify-around items-center mt-4"):
        # Average Profit per Day
        total_days = (
            pd.to_datetime("today") - pd.to_datetime(years[0], format="%Y")
        ).days
        average_profit_per_day = yearly_total_profits.sum() / total_days
        indicator_avg_daily = create_indicator(
            f"${average_profit_per_day:.2f}", "Average Profit per Day ($)"
        )
        with ui.column().classes("md:w-1/4 w-full"):
            indicator_avg_daily

        # Active vs Passive Assets
        active_passive_fig = create_pie_chart(
            labels=asset_types, values=asset_values, title="Active vs Passive Assets"
        )
        ui.plotly(active_passive_fig).classes("md:w-1/3 w-full")


ui.run(dark=False, port=8000, reload=True, favicon="🆖", title="dashboard")
