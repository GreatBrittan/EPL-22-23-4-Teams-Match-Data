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
            "Aaron Ramsdale",
            "Ben White",
            "Gabriel Magalhães",
            "William Saliba",
            "Oleksandr Zinchenko",
            "Martin Ødegaard",
            "Albert Sambi Lokonga",
            "Granit Xhaka",
            "Bukayo Saka",
            "Gabriel Jesus",
            "Gabriel Martinelli"
            "Matt Turner",
            "Kieran Tierney",
            "Rob Holding",
            "Cédric Soares",
            "Takehiro Tomiyasu",
            "Emile Smith Rowe",
            "Fábio Vieira",
            "Eddie Nketiah",
            "Marquinhos"
        }

with open("playerData.json", "r", encoding="utf8") as f:
    data = json.load(f)
    Arsenal = {}
    ArsenalEvents ={}
    stuff = {}
    count = 1
    for i in data:
        if(data[i]['team1_name'] == "Arsenal" or data[i]['team2_name'] == "Arsenal"):
            cats = ["matchweek", "team1_name", "team1_stat", "team2_name", "team2_stat"]
            dogs = ["event"]
            Arsenal[count] = {}
            ArsenalEvents[count]={}
            for y in dogs:
                ArsenalEvents[count][y] = data[i][y]
            for x in cats:
                Arsenal[count][x] = data[i][x]
            count += 1
    with open('Arsenal_MatchData.json', 'w', encoding="utf8") as f:
        sorted_dict = {k: Arsenal[k] for k in sorted(Arsenal, key=lambda x: int(Arsenal[x]['matchweek'].split()[-1]))}
        json.dump(sorted_dict, f, indent=4,ensure_ascii=False)
    with open('Arsenal_EventData.json', 'w', encoding="utf8") as f:
        json.dump(ArsenalEvents, f, indent=4,ensure_ascii=False)
    for i in ArsenalEvents:
        stuff[i]= {} 
        goal_count = 1
        goal_string = f"Goal!  Arsenal {goal_count}"
        for n in sorted(ArsenalEvents[i]["event"]):
            if (goal_string in n):
                goal_count += 1
                goal_string = f"Goal!  Arsenal {goal_count}" 
                for player in players:
                    if (player in n):
                        try:
                            stuff[i][(goal_count - 1)]
                        except KeyError:
                            stuff[i][(goal_count - 1)] = n
                            break
                        else:
                            continue
    with open('Arsenal_Goals.json', 'w', encoding="utf8") as f:
        json.dump(stuff, f, indent=4,ensure_ascii=False) 
                
    
print("did it work?")