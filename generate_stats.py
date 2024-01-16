
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


#list of boyos and games
played_with = ['donal', 'corey', 'cianscan', 'ava', 'ronan', 'matthew',  'tony', 'jaymes', 'cousinjames', 'dylan', 'shane', 'sophie',  'oisin', 'conall', 'myself', 'aziz', 'killian', 'einne', 'edel']
games_played = ["cs", "wingman", "geoguessr", "scrabble", "boggle", "mario strikers charged football", "wii sports resort", "wii sports", "rhythm heaven fever", "ocho", "binding of isaac", "mario and sonic at the olympic games", "family game night", "rocket league", "apex legends", "human fall flat", "chivalry 2", "fortnite", "valorant", "lego star wars tss", "south park the stick of truth", "overwatch", "overwatch 2", "tabletop simulator", "fall guys", "nintendo switch sports", "minecraft", "smackdown vs raw 2006", "burnout 3", "left 4 dead 2", "the forest", "cod mw2", "house of ashes", "project zomboid", "codenames", "gartic phone", "scrabble", "total"]

sessions = {}
games_counters_total = {}

for name in played_with:
    sessions[name] = {}
    for game in games_played:
        sessions[name][game] = 0
for game in games_played:
    games_counters_total[game] = 0


#remove the blank lines
for entry in lines:
    if(entry != '\n'):
        without_line_breaks.append(entry.split("\n")[0])


#loop through games and boyos to count their playcounts in every game
for game in games_played:
    for boyo in played_with:
        for entry in without_line_breaks:
            if (str(boyo + ',') in str(entry) and str(game + '(') in str(entry)):
                sessions[boyo][game] += 1
                sessions[boyo]["total"] += 1
    for entry in without_line_breaks:
        if str(game + '(') in str(entry):
            games_counters_total[game] += 1
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


writer.close()




