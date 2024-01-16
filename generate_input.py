
#file used to display a UI which generates a list of users and games
#the list is in the form of a .txt file, which is then read in by generate_stats and used as input
#this input is in the form of dictionaries which fill up for stat collection purposes

#STEP 1: get user input
# import tkinter as tk
#
# #function to add players to the list
# def add_player():
#     input_text = user_input.get()
#     if input_text:
#         player_list.insert(tk.END, input_text)
#         user_input.delete(0, tk.END)  # Clear the input field
#
# #create the main window
# root = tk.Tk()
# root.title("Enter name of Player.")
#
# #create list of players
# player_list = tk.Listbox(root)
# player_list.pack()
#
# #create input field
# user_input = tk.Entry(root)
# user_input.pack()
#
# #create button to add input to list
# add_button = tk.Button(root, text="Add", command=add_player)
# add_button.pack()

#run the file
#root.mainloop()

#STEP 2: sanatise input (all lowercase and append comma)
#STEP3: write into file (maybe add option to read and append to previous file in the future)


#goal is to generate a list of people the user has played with
import numpy as np
import re
import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt

#open the file and read it
file = open('2022 Full Log.txt', 'r')
lines = file.readlines()


#remove the blank lines
without_line_breaks = []
for entry in lines:
    if(entry != '\n'):
        without_line_breaks.append(entry.split("\n")[0])


#generate list of played with players (for filtering and pasting)
player_pattern = r',\s*(\w+)'
game_pattern = r'[^-]([^:]+?\()'

players_list = []
games_list = []

for entry in without_line_breaks:
    if not entry.startswith('- thoughts of the day') and ':(' not in entry:
        found_players = re.findall(player_pattern, entry)
        players_list.extend(found_players)

        found_games = re.findall(game_pattern, entry)
        #Check if the length of the captured text is less than or equal to 8 words. This removes a LOT of full sentences that arent games
        valid_games = [game for game in found_games if len(re.findall(r'\b\w+\b', game)) <= 8]

        games_list.extend(valid_games)

#Convert the lists into sets to get unique values
unique_players_set = set(players_list)
unique_games_set = set(games_list)

#output file to text for filtering manually
#TODO: maybe have the above commented out code read this txt file and generate a bunch of checkboxes to be used to populate the variable in generate_stats
players_output_filename = 'unfiltered_players_list.txt'
games_output_filename = 'unique_games.txt'

with open(players_output_filename, 'w') as players_output_file:
    players_output_file.write('#Copy and Paste the following line onto line 869 of generate_stats.py\n#Remove any words that arent the names of people youve played with\nplayed_with = [' + str(unique_players_set) + ']')
with open(games_output_filename, 'w') as games_output_file:
    games_output_file.write('#Copy and Paste the following line onto line 870 of generate_stats.py\n#Remove any lines that arent explicitly games youve played\ngames_played = [' + str(unique_games_set) + ']')

print("Players list: " + str(unique_players_set))






