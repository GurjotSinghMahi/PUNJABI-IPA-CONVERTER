#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *

def call_help():
    help_window = Toplevel()
    help_window.geometry("500x130")
    help_window.title("Help")
    help_icon = PhotoImage(file=os.path.join('pipalogo.gif'))
    help_window.tk.call('wm', 'iconphoto', help_window._w, help_icon)
    about_dialog_box(help_window)
    help_window.mainloop()

class about_dialog_box(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        for r in range(5):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
        self.label(master)
        self.buttons(master)

    def label(self, master):
        label_text = """
        To Convert the Punjabi Text file to IPA format kindly follow following steps:
        1. Select the Text file using "Upload File" Button or paste the Punjabi Text
         in upper Text Area
        2. Click on "Convert" Button.
        3. The Convert text in IPA format will appear in Below window.
        """
        label_area = Label(master, text=label_text, justify=LEFT)
        label_area.grid(row=0, column=0)

    def buttons(self, master):
        ok_button = Button(master, text='Ok', width=20, command=master.destroy)
        ok_button.grid(row=2, column=0)