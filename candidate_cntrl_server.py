from tkinter import *
from tkinter import ttk
from logic import add_candidate,delete_candidate

## this is skeleton UI for testing the logic.py functions :p
root = Tk()
root.title("Edit Candidate")
root.geometry('300x300')


candidate_label = Label(root, text="Candidate Name")
candidate_label.pack()
candidate_entry = Entry(root)
candidate_entry.pack()

def add_candidate_btn():
	c_name = candidate_entry.get()
	add_candidate(c_name)

add_button = Button(root, text="Add Candidate", command= add_candidate_btn)
add_button.pack()



delete_label = Label(root, text="Delete Candidate")
delete_label.pack()
delete_entry = Entry(root)
delete_entry.pack()

def delete_candidate_btn():
	d_name = delete_entry.get()
	delete_candidate(d_name)

delete_button = Button(root, text="Delete Candidate", command=delete_candidate_btn)
delete_button.pack()


























## the server should be able to:
## 1. Start the server
## 2. Stop the server
## 3. View the server logs
## 4. Add candidates via IO
## 5. View the list of candidates
## 6. View the list of voters




root.mainloop()