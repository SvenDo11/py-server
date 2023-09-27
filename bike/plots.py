import plotly.express as px
import pandas as pd
from django.db.models import query
from .models import Fuel
from .colors import Color


def get_test_plot():
    fig = px.bar(x=['a', 'b', 'c'], y=[1, 4, 3])
    fig.update_layout(paper_bgcolor="#d5c4a1")
    return fig.to_html()


def fuel_base(fuel_set: query.QuerySet, y_label: str, attr: str, attr_is_function: bool = False, print_average: bool = True):
    fuel_set = fuel_set.order_by("fuel_date")
    x_ = []
    y_ = []
    for fuel in fuel_set:
        if not isinstance(fuel, Fuel):
            continue
        x_.append(fuel.fuel_date.date())
        if attr_is_function:
            y_.append(getattr(fuel, attr)())
        else:
            y_.append(getattr(fuel, attr))

    average = sum(y_) / len(y_) if len(y_) > 0 else 0

    data = pd.DataFrame(dict(Date=x_, Attr=y_))
    fig = px.line(data, x="Date", y="Attr", template="plotly_white", markers=True,
                  labels={'Date': "Date", 'Atr': y_label})
    fig.update_traces(marker=dict(color=Color.get("color2")), line=dict(color=Color.get("color10")))
    fig.update_layout(paper_bgcolor=Color.get("color-bg2"), autosize=False)

    if print_average:
        fig.add_hline(y=average, line_color=Color.get("color9"), annotation_text="Average: {:.2f}".format(average))
    return fig


def fuel_economy(fuel_set: query.QuerySet):
    fig = fuel_base(fuel_set, "Fuel Economy [L/100km]", "litre_per_100km", True)

    return fig.to_html()


def fuel_price(fuel_set: query.QuerySet):
    fig = fuel_base(fuel_set, "Fuel Price [€/L]", "cost_per_litre")
    return fig.to_html()


def fuel_odometer(fuel_set: query.QuerySet):
    fig = fuel_base(fuel_set, "Odometer [km]", "km_total", print_average=False)
    return fig.to_html()
