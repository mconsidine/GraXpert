# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:16:05 2022

@author: Steffen
"""

from tkinter import ttk
from localization import _

class LoadingFrame():
    def __init__(self, widget, toplevel):

        font = ('Verdana', 20, 'normal')

        self.toplevel = toplevel
        self.text = ttk.Label(
            widget, 
            text=_("Calculating..."), 
            font=font
        )
        
    def start(self):
        
        self.text.pack(fill="none", expand=True)
        self.toplevel.update()
        # force update of label to prevent white background on mac
        self.text.configure(background="#313131")
        self.text.update()

    def end(self):
        self.text.pack_forget()
        self.toplevel.update()