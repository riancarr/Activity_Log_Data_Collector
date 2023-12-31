
import numpy as np
import re
import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt


def sort_dict(dictionary, column):
    sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1][column], reverse=True)}
    return sorted_dict


#open the file and read it
file = open('2022 Full Log.txt', 'r')
lines = file.readlines()

without_line_breaks = []
days_gone = []
thoughts_of_the_days = []

#session counters
sessions = {
    "donal": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "ronan": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "shane": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "killian": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "jaymes": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "matthew": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "corey": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "aziz": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "myself": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "cousinjames": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "ava": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "cianscan": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "cian": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "einne": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "ciara": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "luna": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "niko": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "tony": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "luke": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    },
    "oisin": {
        "cs": 0,
        "wingman": 0,
        "geoguessr": 0,
        "scrabble": 0,
        "boggle": 0,
        "mario strikers charged football": 0,
        "wii sports resort": 0,
        "wii sports": 0,
        "rhythm heaven fever": 0,
        "ocho": 0,
        "binding of isaac": 0,
        "mario and sonic at the olympic games": 0,
        "family game night": 0,
        "rocket league": 0,
        "apex legends": 0,
        "human fall flat": 0,
        "chivalry 2": 0,
        "fortnite": 0,
        "valorant": 0,
        "lego star wars tss": 0,
        "south park the stick of truth": 0,
        "overwatch": 0,
        "overwatch 2": 0,
        "tabletop simulator": 0,
        "fall guys": 0,
        "nintendo switch sports": 0,
        "minecraft": 0,
        "smackdown vs raw 2006": 0,
        "burnout 3": 0,
        "left 4 dead 2": 0,
        "the forest": 0,
        "cod mw2": 0,
        "house of ashes": 0,
        "project zomboid": 0,
        "codenames": 0,
        "gartic phone": 0,
        "scrabble": 0,
        "total": 0
    }
}

#game names disctionary (to copy and paste per person)
games_counters_total = {
    "cs": 0,
    "wingman": 0,
    "geoguessr": 0,
    "scrabble": 0,
    "boggle": 0,
    "mario strikers charged football": 0,
    "wii sports resort": 0,
    "wii sports": 0,
    "rhythm heaven fever": 0,
    "ocho": 0,
    "binding of isaac": 0,
    "mario and sonic at the olympic games": 0,
    "family game night": 0,
    "rocket league": 0,
    "apex legends": 0,
    "human fall flat": 0,
    "chivalry 2": 0,
    "fortnite": 0,
    "valorant": 0,
    "lego star wars tss": 0,
    "south park the stick of truth": 0,
    "overwatch": 0,
    "overwatch 2": 0,
    "tabletop simulator": 0,
    "fall guys": 0,
    "nintendo switch sports": 0,
    "minecraft": 0,
    "smackdown vs raw 2006": 0,
    "burnout 3": 0,
    "left 4 dead 2": 0,
    "the forest": 0,
    "cod mw2": 0,
    "house of ashes": 0,
    "project zomboid": 0,
    "codenames": 0,
    "gartic phone": 0,
    "scrabble": 0
}


#list of boyos and games
played_with = ["donal,", "ronan,", "shane,", "killian,", "jaymes,", "matthew,", "corey,", "aziz,", "myself,", "cousinjames,", "ava,", "cianscan,", "cian,", "einne,", "ciara,", "luna,", "niko,", "tony,", "luke,", "oisin,"]
games_played = ["cs(", "wingman(", "geoguessr(", "scrabble(", "boggle(", "mario strikers charged football(", "wii sports resort(", "wii sports(", "rhythm heaven fever(", "ocho(", "binding of isaac(", "mario and sonic at the olympic games(", "family game night(", "rocket league(", "apex legends(", "human fall flat(", "chivalry 2(", "fortnite(", "valorant(", "lego star wars tss(", "south park the stick of truth(", "overwatch(", "overwatch 2(", "tabletop simulator(", "fall guys(", "nintendo switch sports(", "minecraft(", "smackdown vs raw 2006(", "burnout 3(", "left 4 dead 2(", "the forest(", "cod mw2(", "house of ashes(", "project zomboid(", "codenames(", "gartic phone(", "scrabble("]

#remove the blank lines
for entry in lines:
    if(entry != '\n'):
        without_line_breaks.append(entry.split("\n")[0])

#loop through games and boyos to count their playcounts in every game
for game in games_played:
    for boyo in played_with:
        for entry in without_line_breaks:
            if (boyo in str(entry) and game in str(entry)):
                sessions[boyo.split(",")[0]][game.split("(")[0]] += 1
                sessions[boyo.split(",")[0]]["total"] += 1
    for entry in without_line_breaks:
        if game in str(entry):
            games_counters_total[game.split("(")[0]] += 1
        if 'thoughts of the day:' in str(entry):
            thoughts_of_the_days.append(entry.split(':')[1])



#sort the data in the sessions dictionary
sessions = sort_dict(sessions, 'total')

#sort items in the games counter dictionary
items = list(games_counters_total.items())
games_counters_total = sorted(items, key=lambda x: x[1], reverse=True)


print(sessions)
print(games_counters_total)
print(len(thoughts_of_the_days))



#excel stuff
#turn dictionaries into dataframes
df = pd.DataFrame.from_dict(sessions, orient='index')
df2 = pd.DataFrame(games_counters_total)

writer = pd.ExcelWriter('template.xlsx', engine='xlsxwriter')

#output dataframes to excel file
df.to_excel(writer, sheet_name='BoyoTotals')
df2.to_excel(writer, sheet_name='GameTotals', index=False)


workbook = writer.book
worksheet = writer.sheets['GameTotals']


writer.save()




