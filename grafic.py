

import tkinter as tk
root = tk.Tk()
lbl = tk.Label(root, text='GUI stands for Graphical\n'
 'User Interface. This is a GUI.')
lbl.pack()
btn = tk.Button(root, text='Exit',
 fg='darkred', bg='lightgreen',
 command=quit)
btn.pack()


root.mainloop()
