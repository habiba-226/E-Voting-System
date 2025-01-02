import tkinter as tk
from client import send_to_server
from logic import get_candidate


def show_frame(frame): ## for showing the frame
    frame.tkraise()

def on_vote_button_click():
    vote = user_choice.get()
    print(vote)
    send_to_server(vote)

root = tk.Tk()
root.title("Control Server")
root.geometry('400x400')
#root.geometry('200x100')

## radio buttons for the candidates


tk.Label(root, 
        text="""Choose a Candidate (★‿★):""",
        justify = tk.LEFT,
        padx = 20).pack()



candidates = get_candidate()
user_choice = tk.StringVar()
user_choice.set(candidates[0])

for candidate in candidates:
    candidate_radio = tk.Radiobutton(root, text=candidate, value=candidate, variable=user_choice)
    candidate_radio.pack()



# add_label = tk.Label(root, text="Vote for a candidate")
# add_label.pack()
# add_entry = tk.Entry(root)
# add_entry.pack()

add_button = tk.Button(root, text="Vote", command=on_vote_button_click)
add_button.padx = 10
add_button.pady = 10
add_button.background = 'blue'
add_button.pack()


root.mainloop()


# references:
## https://python-course.eu/tkinter/radio-buttons-in-tkinter.php#:~:text=A%20radio%20button%2C%20sometimes%20called,text%20in%20a%20single%20font.