import tkinter as tk
from client import send_to_server
from logic import get_candidate, background_color
import threading
import json
import hashlib
from tkinter import *
from tkinter import messagebox
import socket
import hashlib
import uuid




def show_frame(frame): ## for showing the frame
    frame.tkraise()

def on_vote_button_click():
    vote = user_choice.get()
    print(vote)
    send_to_server(vote)


root = tk.Tk()
root.title("Voting System - Voter")
root.geometry("400x350")
root.configure(bg=background_color) 

candidates = get_candidate()
if not candidates:
    messagebox.showerror("Error", "No candidates available to vote for!")
    root.quit()
    

title_label = Label(root, text="Vote for Your Candidate", font=('Helvetica', 16, 'bold'), bg=background_color, fg="#333333")
title_label.pack(pady=20)

candidate_label = Label(root, text="Select a candidate", font=('Helvetica', 12), bg=background_color, fg="#333333")
candidate_label.pack(pady=10)

candidate_var = StringVar(root)
candidate_var.set(candidates[0])  

candidate_menu = OptionMenu(root, candidate_var, *candidates)
candidate_menu.config(font=('Helvetica', 12), width=20)
candidate_menu.pack(pady=10)


vote_button = Button(root, text="Vote", font=('Helvetica', 14, 'bold'), bg="#AA5486", fg="white", height=2,
                    width=20, command=lambda: send_to_server(candidate_var.get()))
vote_button.pack(pady=20)

# Footer label (Credits or instructions)
footer_label = Label(root, text="Voting System - Powered by Socket Programming", font=('Helvetica', 8), bg=background_color, fg="#888888")
footer_label.pack(side=BOTTOM, pady=10)

root.mainloop()




# references:
## https://python-course.eu/tkinter/radio-buttons-in-tkinter.php#:~:text=A%20radio%20button%2C%20sometimes%20called,text%20in%20a%20single%20font.