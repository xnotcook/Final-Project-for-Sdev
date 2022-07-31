import tkinter as tk
#from tkinter import messagebox
from projectpart1 import main

#sizing for the GUI
root = tk.Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

#
def execfile(param):
    pass

#This is wear you make the password and if and then statements are used so like if the password and username arent admin 1234 an error shows up
def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        main()
        master = tk.Tk()

        def callback():
            execfile("DahmaniMouadFinalProject2.py")

        b = tk.Button(master, text="OK", command=callback)
        b.pack()
        tk.mainloop()

    elif username != 'admin' and password != '1234':
        tk.messagebox.showerror("Invalid", "invalid username or password")

    elif password != "1234":
        tk.messagebox.showerror("Invalid", "invalid username or password")

    elif username != 'admin':
        tk.messagebox.showerror("Invalid", "invalid username and username")

#this inserts the image inside the GUI
img = tk.PhotoImage(file='login.png')
tk.Label(root, image=img, bg='white').place(x=50, y=50)

#makes limits the GUI screen and how it pops up
frame = tk.Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = tk.Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


###############################################

def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

#so username shows inside the box when I do code insert it puts the word username inside the text box and the code tk.entry removes the border and customizes the box
user = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


###########################################################
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

#so password shows inside the box when I do code insert it puts the word password inside the text box and the code tk.entry removes the border and customizes the box
code = tk.Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#this piece right here edits the size of the sign in button and its color
tk.Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)




root.mainloop()