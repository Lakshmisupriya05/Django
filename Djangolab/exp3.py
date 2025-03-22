import tkinter as tk
from tkinter import messagebox
def showmsg():
    user=entry1.get()
    pwd=entry2.get()
    username='23b01a12i1'
    password='abcdef'
    if(username==user and password==pwd):
        messagebox.showinfo("Login Successful",'Welcome Supriya!')
    else:
        messagebox.showwarning("Login Failed",'Invalid Username or Password')
root=tk.Tk()
root.geometry("900x400")
root.title("Login Form")
userlabel=tk.Label(root,text="Enter Username")
userlabel.grid(row=2,column=7,padx=60,pady=10)
entry1=tk.Entry(root,width=20)
entry1.grid(row=3,column=7,padx=60,pady=10)
pwdlabel=tk.Label(root,text="Enter Password")
pwdlabel.grid(row=4,column=7,padx=60,pady=10)
entry2=tk.Entry(root,width=20,show='*')
entry2.grid(row=5,column=7,padx=60,pady=10)
button=tk.Button(root,text="Login",command=showmsg)
button.grid(row=6,column=7,padx=60,pady=10)
root.mainloop()