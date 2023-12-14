import json
import plotly.subplots as sp
import plotly.graph_objects as go

# Load JSON data

with open('ManCity_MatchData.json', 'r') as json_file:
    data = json.load(json_file)
    dataKeys = data.keys()
# Define the statistics to display
statistics = ['possession_%', 'shots_on_target', 'shots', 'touches', 'passes', 'tackels', 'clearances', 'corners', 'offsides', 'yellow_cards', 'foul_conceded']

# Set up subplots
num_stats = len(statistics)
fig = sp.make_subplots(rows=len(data), cols=num_stats, subplot_titles=[f'{stat}' for matchweek in data.keys() for stat in statistics], row_titles=list(data.keys()), shared_yaxes=False)

# Define colors for Team 1 and Team 2
premier_league_teams = {
    'Arsenal': '#EF0107',                    # Red
    'Aston Villa': '#95BFE5',                # Claret and blue
    'Bournemouth': '#DA020E',               # Red
    'Brentford': '#E0003C',                  # Red
    'Brighton & Hove Albion': '#0057B8',     # Blue and white
    'Chelsea': '#034694',                    # Blue
    'Crystal Palace': '#1B458F',             # Red and blue
    'Everton': '#003399',                    # Blue
    'Fulham': '#000000',                     # Black
    'Leeds United': '#F9E300',               # Yellow
    'Leicester City': '#003090',             # Blue
    'Liverpool': '#C8102E',                  # Red
    'Manchester City': '#6CADDF',            # Sky blue
    'Manchester United': '#DA020E',          # Red
    'Newcastle United': '#000000',           # Black and white
    'Nottingham Forest': '#1C4DC2',          # Red and white
    'Southampton': '#D71920',                # Red and white
    'Tottenham Hotspur': '#FFFFFF',          # White
    'West Ham United': '#7A263A',            # Claret and blue
    'Wolverhampton Wanderers': '#FDB913'     # Gold and black
}
# Create individual graphs for each matchweek and statistic
for i, (matchweek, match_data) in enumerate(data.items()):
    team1_name = match_data['team1_name']
    team2_name = match_data['team2_name']
    if(team1_name in premier_league_teams):
        team1_color = premier_league_teams[team1_name]
    if(team2_name in premier_league_teams):
        team2_color = premier_league_teams[team2_name]

    for j, stat in enumerate(statistics):
        # Extract values for both teams
        team1_value = float(match_data['team1_stat'][stat])
        team2_value = float(match_data['team2_stat'][stat])

        # Calculate the maximum value for the y-axis
        max_y_value = max(team1_value, team2_value)

        trace_team1 = go.Bar(
            x=[team1_name],
            y=[team1_value],
            name=f'{team1_name} - {stat}',
            marker_color=team1_color,
            text= [team1_value],
            textposition='outside'
        )

        trace_team2 = go.Bar(
            x=[team2_name],
            y=[team2_value],
            name=f'{team2_name} - {stat}',
            marker_color=team2_color,
            text= [team2_value],
            textposition='outside'
        )

        fig.add_trace(trace_team1, row=i + 1, col=j + 1)
        fig.add_trace(trace_team2, row=i + 1, col=j + 1)
        fig.update_layout(plot_bgcolor='rgba(255,253,208,0.5)')
        # Set up layout for each subplot
        fig.update_xaxes(row=i + 1, col=j + 1)
        fig.update_yaxes(row=i + 1, col=j + 1, range=[0, max_y_value + (max_y_value * .1)])  # Set the y-axis range

# Update the overall layout
    fig.update_layout(
        title_text='Team Comparison Across Matchweeks',
        showlegend=False,  # Hide legend for clarity
        width=2000,
        height=1000 * len(data)
    )

# Show the plot
fig.show()
