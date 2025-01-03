import tkinter as tk
from tkinter import *
import subprocess

def switch_to_server():
    subprocess.Popen(['python', 'serverGUI.py'])

def switch_to_client():
    subprocess.Popen(['python', 'clientGUI.py'])


def is_server_running():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((" localhost", 12345))
        s.close()
        return True
    except Exception as e:
        return False
    
                   
def Home(root, frame1):
    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    root.title("Voting System - Home")
    root.configure(bg="#f0f0f0")

    Label(frame1, text="Welcome to the Voting System", font=('Helvetica', 24, 'bold'), bg="#f0f0f0", fg="#333333").grid(row=0, column=0, columnspan=2, pady=20)

    admin_button = Button(frame1, text="Admin", width=20, height=2, font=('Helvetica', 14), command=switch_to_server, bg="#374375", fg="white", relief="raised", bd=5)
    admin_button.grid(row=1, column=0, columnspan=2, pady=15)


# This voter button will be used to switch to the client GUI
#it is initially disabled
    voter_button = Button(frame1, text="Voter", width=20, height=2, font=('Helvetica', 14), command=switch_to_client, bg="#895159", fg="white", relief="raised", bd=5)
    voter_button.grid(row=2, column=0, columnspan=2, pady=15)
    if is_server_running():
            voter_button.config(state=NORMAL)

    frame1.pack(pady=50)
    root.mainloop()

def new_home():
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root, bg="#f0f0f0")
    Home(root, frame1)

if __name__ == "__main__":
    new_home()
