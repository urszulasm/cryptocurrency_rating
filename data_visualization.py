import plotly.express as px
from pandas import DataFrame


def visualize_absolut_price(df: DataFrame) -> None:

    # plot absolute closing prices in line chart
    fig = px.line(df, title='Absolut closing prices')
    fig.show()


def visualize_daily_returns(df: DataFrame) -> None:

    # plot daily returns in line chart
    fig = px.line(df, title='Percentage daily returns')
    fig.show()


def visualize_cumulative_returns(df: DataFrame) -> None:

    # plot cumulative daily returns in line chart
    fig = px.line(df, title='Cumulative daily return')
    fig.show()
