import tkinter as tk
from logic import add_candidate, delete_candidate, count_votes, background_color, text_color
from server import start_server, shutdown_server
import threading
import sys
import signal


def show_frame(frame): ## for showing the frame
    frame.tkraise()

def delete_candidate_btn(delete_entry, vote_count_text): #for deleting the candidate
    candidate = delete_entry.get()
    delete_entry.delete(0, tk.END)
    delete_candidate(candidate)
    update_vote_count(vote_count_text)

def add_candidate_btn(add_entry, vote_count_text): #for adding the candidate
    candidate = add_entry.get()
    add_entry.delete(0, tk.END)
    add_candidate(candidate)
    update_vote_count(vote_count_text)

def update_vote_count(vote_count_text): #for updating the vote count
    vote_counts = count_votes()
    vote_count_text.delete(1.0, tk.END)  ## for clearing the text box
    for candidate, count in vote_counts.items():
        vote_count_text.insert(tk.END, f"{candidate}: {count}\n")
    print(vote_counts)

def initialize_vote_count(vote_count_text): #for initializing the vote count
    vote_counts = count_votes()
    vote_count_text.delete(1.0, tk.END)  ## for clearing the text box
    for candidate in vote_counts.keys():
        vote_count_text.insert(tk.END, f"{candidate}: 0\n")




# GUI

root = tk.Tk()
root.title("Control Server")
root.geometry('700x700')
root.config(bg=background_color)

title_label = tk.Label(root, text="Admin Control Panel", font=("Arial", 18, "bold"), bg=background_color, fg="#69247C")
title_label.pack(pady=20)

# Control Page
control_frame = tk.Frame(root, bg=background_color)
control_frame.pack(pady=10)

# Deleting and adding candidates
delete_label = tk.Label(control_frame, text="Delete Candidate", font=("Arial", 12), bg=background_color, fg="#374375")
delete_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
delete_entry = tk.Entry(control_frame, font=("Arial", 12), width=30)
delete_entry.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(control_frame, text="Delete Candidate", command=lambda: delete_candidate_btn(delete_entry, vote_count_text), font=("Arial", 12, "bold"), bg="#895159", fg="white", width=20, relief="raised", bd=2)
delete_button.grid(row=0, column=2, padx=5, pady=5)

add_label = tk.Label(control_frame, text="Add Candidate", font=("Arial", 12), bg=background_color, fg="#374375")
add_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
add_entry = tk.Entry(control_frame, font=("Arial", 12), width=30)
add_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(control_frame, text="Add Candidate", command=lambda: add_candidate_btn(add_entry, vote_count_text), font=("Arial", 12, "bold"), bg="#BABDE2", fg="white", width=20, relief="raised", bd=2)
add_button.grid(row=1, column=2, padx=5, pady=5)

# Start Server Section
start_button = tk.Button(root, text="Start Server", command=lambda: threading.Thread(target=start_server).start(), font=("Arial", 12, "bold"), bg="#A888B5", fg="white", width=20, relief="raised", bd=2)
start_button.pack(pady=10)

end_button = tk.Button(root, text="End Server", command=lambda: threading.Thread(target=shutdown_server).start(), font=("Arial", 12, "bold"), bg="#8174A0", fg="white", width=20, relief="raised", bd=2)
end_button.pack(pady=10)

# Vote Count Section
vote_count_frame = tk.Frame(root, bg=background_color)
vote_count_frame.pack(pady=10)

vote_count_label = tk.Label(vote_count_frame, text="Vote Count", font=("Arial", 12), bg=background_color, fg="#374375")
vote_count_label.grid(row=0, column=0, padx=5, pady=5)

vote_count_text = tk.Text(vote_count_frame, height=10, width=30, font=("Arial", 12))
vote_count_text.grid(row=1, column=0, padx=5, pady=5)

refresh_button = tk.Button(vote_count_frame, text="Refresh", command=lambda: update_vote_count(vote_count_text), font=("Arial", 12, "bold"), bg="#AA5486", fg="white", width=20, relief="raised", bd=2)
refresh_button.grid(row=2, column=0, padx=5, pady=5)

initialize_vote_count(vote_count_text)

root.mainloop()
