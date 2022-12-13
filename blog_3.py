"""
Program: blog_3
Creation Data: 12/13/2022
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Creating a Class-based Python Tkinter Template - Part 3

Description: Post part of a series on creating a class-based GUI
            using Python's Tkinter module.

Previous code: blog_2 available on github

Changes: 12/13/2022 - This version a frame class to display page content. 
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PageFrm(tk.Frame): # Container frame for page content
    def __init__(self, parent):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Class constant(s)
        TITLE_FONT = ("Helvetica", 16, "bold")

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        # self.rowconfigure(0, weight = 1)

        # Define and place the widget
        screen_frm = tk.LabelFrame(self, text='Screen Frame')
        screen_frm.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)

        #  Configure layout proportions for inside screen_frm 
        screen_frm.columnconfigure(0, weight = 1)
        screen_frm.rowconfigure(0, weight = 1)
        screen_frm.rowconfigure(1, weight = 1)

        # Create and place two Label widgets
        title_lbl = tk.Label(screen_frm, text = '-- Title Here --', font=TITLE_FONT)
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)
        content_lbl = tk.Label(screen_frm, text = '-- Stuff Here --')
        content_lbl.grid(column = 0, row = 1,pady=(30, 20), sticky = tk.EW)



class App(tk.Tk):  # Inheriting from Tk class
    def __init__(self):
        super().__init__()  # Initializing the inherited class

        # Program Info
        WINDOW_WIDTH = 300
        WINDOW_HEIGHT = 300

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate offset to center window on screen
        x_offset = int((screen_width - WINDOW_WIDTH)/2)
        y_offset = int((screen_height - WINDOW_HEIGHT)/2)

        # Define application properties
        self.title('Class Based GUI')
        self.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_offset}+{y_offset}')
        self.iconbitmap(self, default='./wolftrack.ico')
        self.resizable(width = False, height = False)
        
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Add content frame to application
        PageFrm(self).grid(sticky = tk.NSEW)


def main():
    prog_app = App()
    prog_app.mainloop()


if __name__ == '__main__': main()
