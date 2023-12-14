from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import layout
import json

# Load data from external JSON file
with open('ManCity_MatchData.json', 'r') as file:
    data = json.load(file)

matches = data

# Prepare data for the first matchweek
matchweek = "1"
team1_stats = matches[matchweek]["team1_stat"]
team2_stats = matches[matchweek]["team2_stat"]

# Create a Bokeh data source
source = ColumnDataSource(data=dict(
    x=list(team1_stats.keys()),
    team1=[float(val) for val in team1_stats.values()],
    team2=[float(val) for val in team2_stats.values()]
))

# Create a figure
p = figure(x_range=list(team1_stats.keys()), height=350, title="Match Statistics",
           toolbar_location=None, tools="", y_axis_label="Percentage")

# Create line plots for team1 and team2
team1_line = p.line(x='x', y='team1', source=source, legend_label="Team 1", line_width=2, line_color="blue")
team2_line = p.line(x='x', y='team2', source=source, legend_label="Team 2", line_width=2, line_color="red")

# Set up callback function for the slider
def update_plot(attr, old, new):
    matchweek = str(new)
    team1_stats = matches[matchweek]["team1_stat"]
    team2_stats = matches[matchweek]["team2_stat"]

    # Update the data source
    source.data = dict(
        x=list(team1_stats.keys()),
        team1=[float(val) for val in team1_stats.values()],
        team2=[float(val) for val in team2_stats.values()]
    )

# Create a slider
slider = Slider(start=1, end=len(matches), value=1, step=1, title="Matchweek")
slider.on_change('value', update_plot)

# Create layout
layout = layout([
    [slider],
    [p],
], sizing_mode='stretch_width')

# Add layout to the current document
curdoc().add_root(layout)
