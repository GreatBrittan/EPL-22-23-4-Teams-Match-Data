import json
import plotly.subplots as sp
import plotly.graph_objects as go

# Load JSON data
def getManCityData(seqBreak):
    with open('Match_Data/ManCity_MatchData.json', 'r') as json_file:
        data = json.load(json_file)
        dataKeys = list(data.keys())
    # Specify the matchweek to plot
    selected_matchweek = dataKeys[seqBreak]  # Replace 'MatchweekX' with the desired matchweek

    # Define the statistics to display
    statistics = ['possession_%', 'shots_on_target', 'shots', 'touches', 'passes', 'tackels', 'clearances', 'corners', 'offsides', 'yellow_cards', 'foul_conceded']

    # Set up subplots
    num_stats = len(statistics)
    fig = sp.make_subplots(rows=1, cols=num_stats, subplot_titles=[f'{stat}' for stat in statistics], shared_yaxes=False)

    # Define colors for Team 1 and Team 2
    premier_league_teams = {
        'Arsenal': '#EF0107',                    
        'Aston Villa': '#670E36',                
        'Bournemouth': '#B50E12',               
        'Brentford': '#F0B323',                  
        'Brighton and Hove Albion': '#0057B8',    
        'Chelsea': '#034694',                   
        'Crystal Palace': '#A7A5A6',           
        'Everton': '#b7d993',                  
        'Fulham': '#000000',                    
        'Leeds United': '#e3da81',              
        'Leicester': '#5b0090',             
        'Liverpool': '#00B2A9',                  
        'Manchester City': '#6CADDF',            
        'Manchester United': '#DA291C',          
        'Newcastle United': '#241F20',           
        'Nottingham Forest': '#e84d7b',         
        'Southampton': '#a36c6e',                
        'Tottenham Hotspur': '#FFFFFF',          
        'West Ham United': '#7A263A',            
        'Wolverhampton Wanderers': '#ba8c1a'     
    }

    # Create individual graphs for the specified matchweek and statistic
    match_data = data[selected_matchweek]
    team1_name = match_data['team1_name']
    team2_name = match_data['team2_name']
    if team1_name in premier_league_teams:
        team1_color = premier_league_teams[team1_name]
    if team2_name in premier_league_teams:
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
            text=[team1_value],
            textposition='outside'
        )

        trace_team2 = go.Bar(
            x=[team2_name],
            y=[team2_value],
            name=f'{team2_name} - {stat}',
            marker_color=team2_color,
            text=[team2_value],
            textposition='outside'
        )

        fig.add_trace(trace_team1, row=1, col=j + 1)
        fig.add_trace(trace_team2, row=1, col=j + 1)
        fig.update_layout(plot_bgcolor='rgba(255,253,208,0.5)')
        # Set up layout for each subplot
        fig.update_xaxes(row=1, col=j + 1)
        fig.update_yaxes(row=1, col=j + 1, range=[0, max_y_value + (max_y_value * .1)])  # Set the y-axis range

    # Update the overall layout
    fig.update_layout(
        title_text=f'Team Comparison for Matchweek #{seqBreak}                                                                    {team1_name} vs {team2_name}',
        showlegend=False,  # Hide legend for clarity
        width=1800,
        height=1000
    )

    # Show the plot
    return fig


def getArsenalData(seqBreak):
    with open('Match_Data/Arsenal_MatchData.json', 'r') as json_file:
        data = json.load(json_file)
        dataKeys = list(data.keys())
    # Specify the matchweek to plot
    selected_matchweek = dataKeys[seqBreak]  # Replace 'MatchweekX' with the desired matchweek

    # Define the statistics to display
    statistics = ['possession_%', 'shots_on_target', 'shots', 'touches', 'passes', 'tackels', 'clearances', 'corners', 'offsides', 'yellow_cards', 'foul_conceded']

    # Set up subplots
    num_stats = len(statistics)
    fig = sp.make_subplots(rows=1, cols=num_stats, subplot_titles=[f'{stat}' for stat in statistics], shared_yaxes=False)

    # Define colors for Team 1 and Team 2
    premier_league_teams = {
        'Arsenal': '#EF0107',                    
        'Aston Villa': '#670E36',                
        'Bournemouth': '#B50E12',               
        'Brentford': '#F0B323',                  
        'Brighton and Hove Albion': '#0057B8',    
        'Chelsea': '#034694',                   
        'Crystal Palace': '#A7A5A6',           
        'Everton': '#b7d993',                  
        'Fulham': '#000000',                    
        'Leeds United': '#e3da81',              
        'Leicester': '#5b0090',             
        'Liverpool': '#00B2A9',                  
        'Manchester City': '#6CADDF',            
        'Manchester United': '#DA291C',          
        'Newcastle United': '#241F20',           
        'Nottingham Forest': '#e84d7b',         
        'Southampton': '#a36c6e',                
        'Tottenham Hotspur': '#FFFFFF',          
        'West Ham United': '#7A263A',            
        'Wolverhampton Wanderers': '#ba8c1a'     
    }

    # Create individual graphs for the specified matchweek and statistic
    match_data = data[selected_matchweek]
    team1_name = match_data['team1_name']
    team2_name = match_data['team2_name']
    if team1_name in premier_league_teams:
        team1_color = premier_league_teams[team1_name]
    if team2_name in premier_league_teams:
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
            text=[team1_value],
            textposition='outside'
        )

        trace_team2 = go.Bar(
            x=[team2_name],
            y=[team2_value],
            name=f'{team2_name} - {stat}',
            marker_color=team2_color,
            text=[team2_value],
            textposition='outside'
        )

        fig.add_trace(trace_team1, row=1, col=j + 1)
        fig.add_trace(trace_team2, row=1, col=j + 1)
        fig.update_layout(plot_bgcolor='rgba(255,253,208,0.5)')
        # Set up layout for each subplot
        fig.update_xaxes(row=1, col=j + 1)
        fig.update_yaxes(row=1, col=j + 1, range=[0, max_y_value + (max_y_value * .1)])  # Set the y-axis range

    # Update the overall layout
    fig.update_layout(
        title_text=f'Team Comparison for Matchweek #{seqBreak}                                                                      {team1_name} vs {team2_name}',
        showlegend=False,  # Hide legend for clarity
        width=1800,
        height=1000
    )

    # Show the plot
    return fig

def getBrightonData(seqBreak):
    with open('Match_Data/Brighton_MatchData.json', 'r') as json_file:
        data = json.load(json_file)
        dataKeys = list(data.keys())
    # Specify the matchweek to plot
    selected_matchweek = dataKeys[seqBreak]  # Replace 'MatchweekX' with the desired matchweek

    # Define the statistics to display
    statistics = ['possession_%', 'shots_on_target', 'shots', 'touches', 'passes', 'tackels', 'clearances', 'corners', 'offsides', 'yellow_cards', 'foul_conceded']

    # Set up subplots
    num_stats = len(statistics)
    fig = sp.make_subplots(rows=1, cols=num_stats, subplot_titles=[f'{stat}' for stat in statistics], shared_yaxes=False)

    # Define colors for Team 1 and Team 2
    premier_league_teams = {
        'Arsenal': '#EF0107',                    
        'Aston Villa': '#670E36',                
        'Bournemouth': '#B50E12',               
        'Brentford': '#F0B323',                  
        'Brighton and Hove Albion': '#0057B8',    
        'Chelsea': '#034694',                   
        'Crystal Palace': '#A7A5A6',           
        'Everton': '#b7d993',                  
        'Fulham': '#000000',                    
        'Leeds United': '#e3da81',              
        'Leicester': '#5b0090',             
        'Liverpool': '#00B2A9',                  
        'Manchester City': '#6CADDF',            
        'Manchester United': '#DA291C',          
        'Newcastle United': '#241F20',           
        'Nottingham Forest': '#e84d7b',         
        'Southampton': '#a36c6e',                
        'Tottenham Hotspur': '#FFFFFF',          
        'West Ham United': '#7A263A',            
        'Wolverhampton Wanderers': '#ba8c1a'     
    }

    # Create individual graphs for the specified matchweek and statistic
    match_data = data[selected_matchweek]
    team1_name = match_data['team1_name']
    team2_name = match_data['team2_name']
    if team1_name in premier_league_teams:
        team1_color = premier_league_teams[team1_name]
    if team2_name in premier_league_teams:
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
            text=[team1_value],
            textposition='outside'
        )

        trace_team2 = go.Bar(
            x=[team2_name],
            y=[team2_value],
            name=f'{team2_name} - {stat}',
            marker_color=team2_color,
            text=[team2_value],
            textposition='outside'
        )

        fig.add_trace(trace_team1, row=1, col=j + 1)
        fig.add_trace(trace_team2, row=1, col=j + 1)
        fig.update_layout(plot_bgcolor='rgba(255,253,208,0.5)')
        # Set up layout for each subplot
        fig.update_xaxes(row=1, col=j + 1)
        fig.update_yaxes(row=1, col=j + 1, range=[0, max_y_value + (max_y_value * .1)])  # Set the y-axis range

    # Update the overall layout
    fig.update_layout(
        title_text=f'Team Comparison for Matchweek #{seqBreak}                                                                      {team1_name} vs {team2_name}',
        showlegend=False,  # Hide legend for clarity
        width=1800,
        height=1000
    )

    # Show the plot
    return fig

def getNewcastleData(seqBreak):
    with open('Match_Data/Newcastle_MatchData.json', 'r') as json_file:
        data = json.load(json_file)
        dataKeys = list(data.keys())
    # Specify the matchweek to plot
    selected_matchweek = dataKeys[seqBreak]  # Replace 'MatchweekX' with the desired matchweek

    # Define the statistics to display
    statistics = ['possession_%', 'shots_on_target', 'shots', 'touches', 'passes', 'tackels', 'clearances', 'corners', 'offsides', 'yellow_cards', 'foul_conceded']

    # Set up subplots
    num_stats = len(statistics)
    fig = sp.make_subplots(rows=1, cols=num_stats, subplot_titles=[f'{stat}' for stat in statistics], shared_yaxes=False)

    # Define colors for Team 1 and Team 2
    premier_league_teams = {
        'Arsenal': '#EF0107',                    
        'Aston Villa': '#670E36',                
        'Bournemouth': '#B50E12',               
        'Brentford': '#F0B323',                  
        'Brighton and Hove Albion': '#0057B8',    
        'Chelsea': '#034694',                   
        'Crystal Palace': '#A7A5A6',           
        'Everton': '#b7d993',                  
        'Fulham': '#000000',                    
        'Leeds United': '#e3da81',              
        'Leicester': '#5b0090',             
        'Liverpool': '#00B2A9',                  
        'Manchester City': '#6CADDF',            
        'Manchester United': '#DA291C',          
        'Newcastle United': '#241F20',           
        'Nottingham Forest': '#e84d7b',         
        'Southampton': '#a36c6e',                
        'Tottenham Hotspur': '#FFFFFF',          
        'West Ham United': '#7A263A',            
        'Wolverhampton Wanderers': '#ba8c1a'     
    }

    # Create individual graphs for the specified matchweek and statistic
    match_data = data[selected_matchweek]
    team1_name = match_data['team1_name']
    team2_name = match_data['team2_name']
    if team1_name in premier_league_teams:
        team1_color = premier_league_teams[team1_name]
    if team2_name in premier_league_teams:
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
            text=[team1_value],
            textposition='outside'
        )

        trace_team2 = go.Bar(
            x=[team2_name],
            y=[team2_value],
            name=f'{team2_name} - {stat}',
            marker_color=team2_color,
            text=[team2_value],
            textposition='outside'
        )

        fig.add_trace(trace_team1, row=1, col=j + 1)
        fig.add_trace(trace_team2, row=1, col=j + 1)
        fig.update_layout(plot_bgcolor='rgba(255,253,208,0.5)')
        # Set up layout for each subplot
        fig.update_xaxes(row=1, col=j + 1)
        fig.update_yaxes(row=1, col=j + 1, range=[0, max_y_value + (max_y_value * .1)])  # Set the y-axis range

    # Update the overall layout
    fig.update_layout(
        title_text=f'Team Comparison for Matchweek #{seqBreak}                                                                      {team1_name} vs {team2_name}',
        showlegend=False,  # Hide legend for clarity
        width=1800,
        height=1000
    )

    # Show the plot
    return fig