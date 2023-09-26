import plotly.express as px
import pandas as pd
from django.db.models import query
from .models import Fuel
from .colors import Color


def get_test_plot():
    fig = px.bar(x=['a', 'b', 'c'], y=[1, 4, 3])
    fig.update_layout(paper_bgcolor="#d5c4a1")
    return fig.to_html()


def fuel_economy(fuel_set: query.QuerySet):
    fuel_set = fuel_set.order_by("fuel_date")
    x_ = []
    y_ = []
    for fuel in fuel_set:
        if not isinstance(fuel, Fuel):
            continue
        x_.append(fuel.fuel_date.date())
        y_.append(fuel.litre_per_100km())
    average = sum(y_) / len(y_) if len(y_) > 0 else 0

    data = pd.DataFrame(dict(Date=x_, Fuel_Economy=y_))
    fig = px.line(data, x="Date", y="Fuel_Economy", template="plotly_white", markers=True,
                  labels={'Date': "Date", 'Fuel_Economy': "Fuel Economy [L/100km]"})
    fig.update_traces(marker=dict(color=Color.get("color2")), line=dict(color=Color.get("color10")))
    fig.update_layout(paper_bgcolor=Color.get("color-bg2"))

    fig.add_hline(y=average, line_color=Color.get("color9"), annotation_text="Average: {:.2f}".format(average))
    return fig.to_html()
