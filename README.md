# Activity_Log_Data_Collector
This script was designed to work with my own personal logs/diaries which are very specifically formatted to work with this script. As such, the following is a guide on that formatting. 

The script counts and organises 3 things:
1. Number of times playing with [persons name]
2. Number of times playing [certain game]
3. Miscellanous 'thoughts of the day'


For people names to be counted, they must be typed in the txt file as 'name,' or 'name)' (excluding the single quotes). This is so it doesn't count EVERY mention of the person as a time playing games with them. 
EXAMPLE: john,	OR	john) 

For game names to be counted, they must be typed in the txt file as 'gamename(' (excluding the single quotes)
EXAMPLE: chess(	

For a single person, named Mary, playing a game of chess with you, that would look as follows => chess(mary)
For multiple people playing a game of monopoly with you, that would look like this => monopoly(john, jack, stephen, mary)

For a compilation/stream of consciousness representation of your thoughts across the year, you need a seperate line with the phrase 'thoughts of the day:' followed by any number of sentences/words so long as they are on the same line 
EXAMPLE: thoughts of the day: mary is really good at chess but also WOW i hate monopoly! I dont know why we play it because it's just not a fun board game especially since jack insists on following the rules perfectly which defeats the whole 'game' part of it. i should talk to them about it. 

Every entry should be on a seperate line to be counted properly.

The input is taken from a .txt file located in the same directory as the script. 
The output of the data collection is sent to a Microsoft Excel (.xlsx) file where the tables are organised in descending order.


THIS IS A WORK IN PROGRESS
- At the moment, there is a LOT of hardcoded values specific to my own logs. 
- There's also a LOT of repeated code. 
- The process of using it will be streamlined in the future to include a UI that should make it usable for everyone. This is simply the starting point :) 