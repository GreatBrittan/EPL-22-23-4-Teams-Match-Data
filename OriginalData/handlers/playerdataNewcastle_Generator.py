import json
import numpy as np
from bokeh.io import curdoc, output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Slider
from bokeh.layouts import layout
from bokeh.palettes import Category20_10
from bokeh.transform import factor_cmap
from bokeh.models import HoverTool
players = {
            "Nick Pope",
            "Kieran Trippier",
            "Sven Botman",
            "Fabian Schär",
            "Dan Burn",
            "Joe Willock",
            "Sean Longstaff",
            "Bruno Guimarães",
            "Joelinton",
            "Chris Wood",
            "Miguel Almirón",
            "Karl Darlow",
            "Jamaal Lascelles",
            "Jamal Lewis",
            "Javier Manquillo",
            "Matt Ritchie",
            "Jacob Murphy",
            "Elliot Anderson",
            "Callum Wilson",
            "Allan Saint-Maximin"
        }

with open("playerData.json", "r", encoding="utf8") as f:
    data = json.load(f)
    Newcastle = {}
    NewcastleEvents ={}
    stuff = {}
    count = 1
    for i in data:
        if(data[i]['team1_name'] == "Newcastle United" or data[i]['team2_name'] == "Newcastle United"):
            cats = ["matchweek", "team1_name", "team1_stat", "team2_name", "team2_stat"]
            dogs = ["event"]
            Newcastle[count] = {}
            NewcastleEvents[count]={}
            for y in dogs:
                NewcastleEvents[count][y] = data[i][y]
            for x in cats:
                Newcastle[count][x] = data[i][x]
            count += 1
    with open('Newcastle_MatchData.json', 'w', encoding="utf8") as f:
        sorted_dict = {k: Newcastle[k] for k in sorted(Newcastle, key=lambda x: int(Newcastle[x]['matchweek'].split()[-1]))}
        json.dump(sorted_dict, f, indent=4,ensure_ascii=False)
    with open('Newcastle_EventData.json', 'w', encoding="utf8") as f:
        json.dump(NewcastleEvents, f, indent=4,ensure_ascii=False)
    for i in NewcastleEvents:
        stuff[i]= {} 
        goal_count = 1
        goal_string = f"Goal!  Newcastle United {goal_count}"
        for n in sorted(NewcastleEvents[i]["event"]):
            if (goal_string in n):
                goal_count += 1
                goal_string = f"Goal!  Newcastle United {goal_count}" 
                for player in players:
                    if (player in n):
                        try:
                            stuff[i][(goal_count - 1)]
                        except KeyError:
                            stuff[i][(goal_count - 1)] = n
                            break
                        else:
                            continue
    with open('Newcastle_Goals.json', 'w', encoding="utf8") as f:
        json.dump(stuff, f, indent=4,ensure_ascii=False) 
                
    
print("did it work?")