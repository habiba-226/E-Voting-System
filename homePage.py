import tkinter as tk
from tkinter import *
from tkinter import simpledialog, messagebox
import subprocess



def switch_to_client():
    subprocess.Popen(['python', 'clientGUI.py'])


def check_if_admin():
    admin_password = "admin"
    password = simpledialog.askstring("Input", "Enter password", show='*')
    if password == admin_password:
        subprocess.Popen(['python', 'serverGUI.py'])
    else:
        messagebox.showerror("Error", "Incorrect password!")
    return True




## GUI            
def Home(root, frame1):
    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    root.title("Voting System - Home")
    
    root.configure(bg="#F9E6CF")

    Label(frame1, text="Welcome to the Voting System", font=('Helvetica', 20, 'bold'), bg="#F9E6CF", fg="#69247C").grid(row=0, column=0, columnspan=2, pady=20)

    admin_button = Button(frame1, text="Admin", width=20, height=2, font=('Helvetica', 14), command=check_if_admin, bg="#A888B5", fg="white", relief="raised", bd=5)
    admin_button.grid(row=1, column=0, columnspan=2, pady=15)

    voter_button = Button(frame1, text="Voter", width=20, height=2, font=('Helvetica', 14), command=switch_to_client, bg="#895159", fg="white", relief="raised", bd=5)
    voter_button.grid(row=2, column=0, columnspan=2, pady=15)
  
    frame1.pack(pady=50)
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('500x400')
    frame1 = Frame(root, bg="#F9E6CF")
    Home(root, frame1)


if __name__ == "__main__":
    new_home()
