#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *
import tkinter.font as tkFont
from about import call_about
from help import call_help
from tkinter import filedialog
import tkinter.messagebox as tmb
from conversion_func import ipa_creation

def get_text_function():
    home = os.path.expanduser('~')
    filename = filedialog.askopenfilename(initialdir=home, title="Select file",
                                          filetypes=(("Text Documents", "*.txt"), ("all files", "*.*")))
    with open(filename, 'r', encoding='utf8') as textfile:
        data = textfile.read()
    content_text.delete('1.0', END)
    content_text.insert('1.0', data)

def retrieve_input():
    if content_text.index(INSERT) == '1.0':
        tmb.showerror(title="Error", message="Cannot Convert")
    else:
        input_content = content_text.get("1.0", 'end-1c')
        return input_content

def convert():
    extracted_text = retrieve_input()
    extracted_text = ipa_creation(extracted_text)
    put_text.delete('1.0', END)
    put_text.insert('1.0', extracted_text)

class window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        for r in range(5):
            self.master.rowconfigure(r, weight=1)
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
        self.menu(master)
        self.get_text(master)
        self.put_text(master)
        self.buttons_bar(master)

    def menu(self, master):
        menu_bar = Menu(master)
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='About', menu=file_menu)
        file_menu.add_command(label="About", accelerator='Alt + A', compound='left',
                              underline=0, command=call_about)
        file_menu.add_command(label="Help", accelerator='F1', compound='left',
                             command=call_help)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator='Alt + F4', compound='left',
                              command=quit)
        master.config(menu=menu_bar)
        master.bind('<Alt-a>', lambda event: call_about())
        master.bind('<F1>', lambda event: call_help())

    def get_text(self, master):
        get_text_frame = Frame(master)
        get_text_frame.grid(row=0, column=0, rowspan=2, columnspan=5, sticky=W + E + N + S)
        customFont = tkFont.Font(family='Raavi', size=10)
        global content_text
        content_text = Text(get_text_frame, font=customFont, wrap='word')
        content_text.focus_set()
        scroll_bar = Scrollbar(content_text)
        content_text.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=content_text.yview)
        scroll_bar.pack(side='right', fill='y')
        content_text.pack(expand='yes', fill='both')

    def buttons_bar(self, master):
        get_buttons_frame = Frame(master)
        get_buttons_frame.grid(row=2, column=0, columnspan=5, sticky=W + E + N + S)

        for r in range(3):
            get_buttons_frame.rowconfigure(r, weight=1)

        for c in range(5):
            get_buttons_frame.columnconfigure(c, weight=1)

        convert_button = Button(get_buttons_frame, text='Upload File', width=20, command=get_text_function)
        convert_button.grid(row=1, column=1)
        browse_button = Button(get_buttons_frame, text='Convert', width=20, command=convert)
        browse_button.grid(row=1, column=3)

    def put_text(self, master):
        get_text_frame = Frame(master)
        get_text_frame.grid(row=3, column=0, rowspan=2, columnspan=5, sticky=W + E + N + S)
        customFont = tkFont.Font(family='Raavi', size=12)
        global put_text
        put_text = Text(get_text_frame, font=customFont, wrap='word')
        put_text.focus_set()
        scroll_bar = Scrollbar(put_text)
        put_text.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=put_text.yview)
        scroll_bar.pack(side='right', fill='y')
        put_text.pack(expand='yes', fill='both')