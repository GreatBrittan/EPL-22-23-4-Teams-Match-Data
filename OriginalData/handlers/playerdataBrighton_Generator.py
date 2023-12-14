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
            "Robert Sánchez",
            "Adam Webster",
            "Lewis Dunk",
            "Joël Veltman",
            "Solly March",
            "Alexis Mac Allister",
            "Moisés Caicedo",
            "Pervis Estupiñán",
            "Leandro Trossard",
            "Pascal Groß",
            "Danny Welbeck",
            "Jason Steele",
            "Tariq Lamptey",
            "Levi Colwill",
            "Adam Lallana",
            "Kaoru Mitoma",
            "Billy Gilmour",
            "Jeremy Sarmiento",
            "Julio Enciso",
            "Deniz Undav"
        }

with open("playerData.json", "r", encoding="utf8") as f:
    data = json.load(f)
    Brighton = {}
    BrightonEvents ={}
    stuff = {}
    count = 1
    for i in data:
        if(data[i]['team1_name'] == "Brighton and Hove Albion" or data[i]['team2_name'] == "Brighton and Hove Albion"):
            cats = ["matchweek", "team1_name", "team1_stat", "team2_name", "team2_stat"]
            dogs = ["event"]
            Brighton[count] = {}
            BrightonEvents[count]={}
            for y in dogs:
                BrightonEvents[count][y] = data[i][y]
            for x in cats:
                Brighton[count][x] = data[i][x]
            count += 1
    with open('Brighton_MatchData.json', 'w', encoding="utf8") as f:
        sorted_dict = {k: Brighton[k] for k in sorted(Brighton, key=lambda x: int(Brighton[x]['matchweek'].split()[-1]))}
        json.dump(sorted_dict, f, indent=4,ensure_ascii=False)
    with open('Brighton_EventData.json', 'w', encoding="utf8") as f:
        json.dump(BrightonEvents, f, indent=4,ensure_ascii=False)
    for i in BrightonEvents:
        stuff[i]= {} 
        goal_count = 1
        goal_string = f"Goal!  Brighton and Hove Albion {goal_count}"
        for n in sorted(BrightonEvents[i]["event"]):
            if (goal_string in n):
                goal_count += 1
                goal_string = f"Goal!  Brighton and Hove Albion {goal_count}" 
                for player in players:
                    if (player in n):
                        try:
                            stuff[i][(goal_count - 1)]
                        except KeyError:
                            stuff[i][(goal_count - 1)] = n
                            break
                        else:
                            continue
    with open('Brighton_Goals.json', 'w', encoding="utf8") as f:
        json.dump(stuff, f, indent=4,ensure_ascii=False) 
                
    
print("did it work?")