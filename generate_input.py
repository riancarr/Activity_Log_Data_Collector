
#file used to display a UI which generates a list of users and games
#the list is in the form of a .txt file, which is then read in by generate_stats and used as input
#this input is in the form of dictionaries which fill up for stat collection purposes

#STEP 1: get user input
import tkinter as tk

#function to add players to the list
def add_player():
    input_text = user_input.get()
    if input_text:
        player_list.insert(tk.END, input_text)
        user_input.delete(0, tk.END)  # Clear the input field

#create the main window
root = tk.Tk()
root.title("Enter name of Player.")

#create list of players
player_list = tk.Listbox(root)
player_list.pack()

#create input field
user_input = tk.Entry(root)
user_input.pack()

#create button to add input to list
add_button = tk.Button(root, text="Add", command=add_player)
add_button.pack()

#run the file
root.mainloop()





#STEP 2: sanatise input (all lowercase and append comma)

#STEP3: write into file (maybe add option to read and append to previous file in the future)