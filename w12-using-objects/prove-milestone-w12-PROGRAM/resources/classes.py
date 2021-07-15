
import tkinter as tk
from tkinter import LabelFrame, PanedWindow, Variable, filedialog
import os
from typing import Text


class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    # frm: a frame (window) widget
    # lbl: a label widget that displays text for the user to see
    # ent: an entry widget where a user will type text or numbers
    # btn: a button widget that the user will click
    def create_widgets(self):

        # BUTTONS
        self.btn_generate_tree = tk.Button(self, text='Generate Tree', command=self.generate_tree) #1
        self.btn_location = tk.Button(self, text='Current Location', command=self.current_location) #2
        self.btn_close = tk.Button(self, text='Close', command=self.quit) #3

        # Labels
        self.lbl_current_location = tk.Label(text='Label')
        self.lbl_current_location.pack()

        # Label Frame
        self.lbl_frame = LabelFrame(self)
        self.lbl_frame.config(text="Simple Tree Output", height=250, width=250)
        # Text
        self.lbl_frame_content = tk.Text(self.lbl_frame)   
        
           


        # GRIDS
        self.btn_generate_tree.pack()
        self.btn_location.pack()
        self.lbl_frame.pack()
        self.btn_close.pack()
        self.lbl_frame_content.pack()

    def generate_tree(self):
        dirs_main = []
        files_main = []
        location = filedialog.askdirectory()
        for root, dirs, files in os.walk(location):
            dirs_main.append(dirs)
            files_main.append(files)
        tree_string = ''.join(str(e) for e in dirs_main)
        tree_string = ''.join(str(e) for e in files_main)
        self.format_tree(tree_string)

    def format_tree(self, tree):
        self.insert_tree(tree)

    def insert_tree(self, tree):
        self.lbl_frame_content.insert("1.0", tree)

    def current_location(self):
        location = os.path.realpath('.')
        print (location)
        return location


    
