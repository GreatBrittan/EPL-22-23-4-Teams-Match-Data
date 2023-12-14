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
            "Ederson",
            "John Stones",
            "Nathan Aké",
            "Manuel Akanji",
            "Rico Lewis",
            "Rodri",
            "Kevin De Bruyne",
            "Bernardo Silva",
            "Erling Haaland",
            "Jack Grealish",
            "Riyad Mahrez"
            "Stefan Ortega",
            "Kyle Walker",
            "João Cancelo",
            "Kalvin Phillips",
            "Ilkay Gündogan",
            "Sergio Gómez",
            "Phil Foden",
            "Cole Palmer",
            "Julián Álvarez"
        }

with open("playerData.json", "r", encoding="utf8") as f:
    data = json.load(f)
    manCity = {}
    manCityEvents ={}
    stuff = {}
    count = 1
    for i in data:
        if(data[i]['team1_name'] == "Manchester City" or data[i]['team2_name'] == "Manchester City"):
            cats = ["matchweek", "team1_name", "team1_stat", "team2_name", "team2_stat"]
            dogs = ["event"]
            manCity[count] = {}
            manCityEvents[count]={}
            for y in dogs:
                manCityEvents[count][y] = data[i][y]
            for x in cats:
                manCity[count][x] = data[i][x]
            count += 1
    with open('ManCity_MatchData.json', 'w', encoding="utf8") as f:
        sorted_dict = {k: manCity[k] for k in sorted(manCity, key=lambda x: int(manCity[x]['matchweek'].split()[-1]))}
        json.dump(sorted_dict, f, indent=4,ensure_ascii=False)
    with open('ManCity_EventData.json', 'w', encoding="utf8") as f:
        json.dump(manCityEvents, f, indent=4,ensure_ascii=False)
    for i in manCityEvents:
        stuff[i]= {} 
        goal_count = 1
        goal_string = f"Goal!  Manchester City {goal_count}"
        for n in sorted(manCityEvents[i]["event"]):
            if (goal_string in n):
                goal_count += 1
                goal_string = f"Goal!  Manchester City {goal_count}" 
                for player in players:
                    if (player in n):
                        try:
                            stuff[i][(goal_count - 1)]
                        except KeyError:
                            stuff[i][(goal_count - 1)] = n
                            break
                        else:
                            continue
    with open('Goals.json', 'w', encoding="utf8") as f:
        json.dump(stuff, f, indent=4,ensure_ascii=False) 
                
    
print("did it work?")