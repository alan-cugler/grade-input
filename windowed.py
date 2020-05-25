#!/usr/bin/python3

import tkinter as tk



def win():
    gui = tk.Tk()

    ge = tk.Entry(gui, font=("Helvetica", 16)).grid(row=0)
    gb = tk.Button(gui, text='select google.csv', font=("Helvetica", 16)).grid(row=0, column=1)

    se = tk.Entry(gui, font=("Helvetica", 16)).grid(row=1)
    sb = tk.Button(gui, text='select skyward.csv', font=("Helvetica", 16)).grid(row=1, column=1)

    cb = tk.Button(gui, text='convert', font=("Helvetica", 16)).grid(row=2, column=1)

    gui.mainloop()

