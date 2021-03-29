import tkinter as tk
root = tk.Tk()

lbl_message = tk.Label(message_frame,
 text='GUI stands for Graphical\n'
 'User Interface. This is a GUI.',
 font=lbl_font,
 bg='brown', fg='lightyellow')
lbl_message.pack()
root.mainloop()