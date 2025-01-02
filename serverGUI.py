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

## deleting and adding candidates
delete_label = tk.Label(root, text="Delete Candidate")
delete_label.pack()
delete_entry = tk.Entry(root)
delete_entry.pack()

delete_button = tk.Button(root, text="Delete Candidate", command=lambda: delete_candidate_btn(delete_entry, vote_count_text))
delete_button.pack()

add_label = tk.Label(root, text="Add Candidate")
add_label.pack()
add_entry = tk.Entry(root)
add_entry.pack()

add_button = tk.Button(root, text="Add Candidate", command=lambda: add_candidate_btn(add_entry, vote_count_text))
add_button.pack()


# Start Server Section
# added threading so it doesnt block the main thread [UI]
start_button = tk.Button(root, text="Start Server", command=lambda: threading.Thread(target=start_server).start())
start_button.pack()


# Vote Count Section
vote_count_label = tk.Label(root, text="Vote Count")
vote_count_label.pack()

vote_count_text = tk.Text(root, height=10, width=30)
vote_count_text.pack()

refresh_button = tk.Button(root, text="Refresh", command=lambda: update_vote_count(vote_count_text))
refresh_button.pack()

initialize_vote_count(vote_count_text)

show_frame(root)
root.mainloop()


