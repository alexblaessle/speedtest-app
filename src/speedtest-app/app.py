import pandas as pd
import logging
from dash import Dash, html, dcc, Input, Output, State, callback
import plotly.express as px

__data_csv__ = "speed_test_results.csv"

logging.getLogger().setLevel(logging.INFO)


def load_data(fn=None):

    if not fn:
        fn = __data_csv__

    df = pd.read_csv(fn)
    df = df.melt(id_vars=["timestamp"])

    logging.info(f"Loaded {fn}.")
    return df


def update_plot(df, variables):

    fig = px.line(
        df[df["variable"].str.contains(variables)],
        x="timestamp",
        y="value",
        color="variable",
    )
    return fig


app = Dash()

app.layout = [
    html.Button("Refresh", id="btn_refresh", n_clicks=0),
    html.Div(children="Download/Upload speed"),
    dcc.Graph(figure={}, id="plot_speed_line"),
    html.Div(children="Ping"),
    dcc.Graph(figure={}, id="plot_ping_line"),
]


@callback(
    Output(component_id="plot_speed_line", component_property="figure"),
    Output(component_id="plot_ping_line", component_property="figure"),
    Input(component_id="btn_refresh", component_property="n_clicks"),
)
def update_graphs(n_clicks):
    if n_clicks > -1:
        print("Updating")
        df = load_data()
        fig_speed = update_plot(df, "(download)|(upload)")
        fig_ping = update_plot(df, "ping")

        return fig_speed, fig_ping


if __name__ == "__main__":
    app.run(debug=True)
