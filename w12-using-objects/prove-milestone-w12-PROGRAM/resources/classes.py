
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

        # Label Frames
        self.lbl_frame = LabelFrame(self)
        self.lbl_frame.config(text="Simple Tree Output", height=250, width=250)
        self.lbl_frame_content = tk.Label(self.lbl_frame)
        self.lbl_frame_content.config(text='Output')       


        # GRIDS
        self.btn_generate_tree.grid() #1
        self.btn_location.grid() #2
        self.btn_close.grid() #3
        self.lbl_frame.grid()
        self.lbl_frame_content.grid()

    def generate_tree(self):
        dirs_main = []
        files_main = []
        location = filedialog.askdirectory()
        for root, dirs, files in os.walk(location):
            print(root)
            print(dirs)
            dirs_main.append(dirs)
            print(files)
            files_main.append(files)
        tree_string = ''.join(str(e) for e in dirs_main)
        self.lbl_frame_content.config(text=tree_string)


    def current_location(self):
        location = os.path.realpath('.')
        print (location)
        return location


    
