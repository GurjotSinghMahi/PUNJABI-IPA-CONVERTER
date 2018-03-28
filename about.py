#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *
from PIL import Image, ImageTk

def call_about():
    about = Toplevel()
    about.geometry("500x200")
    about.title("About")
    about_icon = PhotoImage(file=os.path.join('pipalogo.gif'))
    about.tk.call('wm', 'iconphoto', about._w, about_icon)
    about_dialog_box(about)
    about.mainloop()

class about_dialog_box(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        for r in range(10):
            self.master.rowconfigure(r, weight=1)
        for c in range(10):
            self.master.columnconfigure(c, weight=1)
        self.label(master)
        self.image(master)
        self.buttons(master)


    def label(self, master):
        label_text = """IPA  stands  for  International  Phonetic  Alphabet.
        Normally, Alphabets have different sounds in different languages.
        This Punjabi IPA converter converts the Punjabi character or word 
        to corresponding International Phonetic Alphabet."""
        label_area = Label(master, anchor="e", text=label_text)
        label_area.grid(row=1, column=4)

    def image(self, master):
        logo = ImageTk.PhotoImage(Image.open("pipalogo2.gif"))
        logo_area = Label(master, image=logo, height=150, width=150)
        logo_area.image = logo
        logo_area.grid(row=1, column=0)

    def buttons(self, master):
        ok_button = Button(master, text='Ok', width=20, command=master.destroy)
        ok_button.grid(row=4, column=4)
