import tkinter as tk
from logic import add_candidate, delete_candidate, count_votes
from server import start_server
import threading



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
root.geometry('400x400')

# Control Page

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

## deleting and adding candidates
delete_label = tk.Label(control_frame, text="Delete Candidate")
delete_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
delete_entry = tk.Entry(control_frame)
delete_entry.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(control_frame, text="Delete Candidate", command=lambda: delete_candidate_btn(delete_entry, vote_count_text))
delete_button.grid(row=0, column=2, padx=5, pady=5)

add_label = tk.Label(control_frame, text="Add Candidate")
add_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
add_entry = tk.Entry(control_frame)
add_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(control_frame, text="Add Candidate", command=lambda: add_candidate_btn(add_entry, vote_count_text))
add_button.grid(row=1, column=2, padx=5, pady=5)

# Start Server Section
# added threading so it doesnt block the main thread [UI]
start_button = tk.Button(root, text="Start Server", command=lambda: threading.Thread(target=start_server).start())
start_button.pack(pady=10)

# Vote Count Section
vote_count_frame = tk.Frame(root)
vote_count_frame.pack(pady=10)

vote_count_label = tk.Label(vote_count_frame, text="Vote Count")
vote_count_label.grid(row=0, column=0, padx=5, pady=5)

vote_count_text = tk.Text(vote_count_frame, height=10, width=30)
vote_count_text.grid(row=1, column=0, padx=5, pady=5)

refresh_button = tk.Button(vote_count_frame, text="Refresh", command=lambda: update_vote_count(vote_count_text))
refresh_button.grid(row=2, column=0, padx=5, pady=5)

initialize_vote_count(vote_count_text)

show_frame(root)
root.mainloop()


