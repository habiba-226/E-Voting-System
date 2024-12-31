from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Server-Side GUI").grid(column=0, row=1)

## the server should be able to:
## 1. Start the server
## 2. Stop the server
## 3. View the server logs
## 4. Add candidates via IO
## 5. View the list of candidates
## 6. View the list of voters



add_candidate("John Doe")
root.mainloop()