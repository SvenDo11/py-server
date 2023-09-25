import plotly.express as px

def get_test_plot():
    fig = px.bar(x=['a', 'b', 'c'], y=[1, 4, 3])
    fig.update_layout(paper_bgcolor="#d5c4a1")
    return fig.to_html()