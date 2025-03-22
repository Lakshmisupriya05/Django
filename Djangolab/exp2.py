import tkinter as tk
root=tk.Tk()
root.title("Basic Tkinter Window")
root.geometry("800x400")
label=tk.Label(root,text="Hello User! Welcome to Tkinter Window",font=("Helvetica",20))
label.pack(pady=25)
root.mainloop()