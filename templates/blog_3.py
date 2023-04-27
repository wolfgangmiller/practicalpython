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
Changes: 04/29/2023 - Update path to favicon after move to templates folder
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PageFrm(ttk.Frame): # Container frame for page content
    def __init__(self, parent):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Configure style
        self.style = ttk.Style(self)
        self.style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        screen_frm = ttk.LabelFrame(self, text='Screen Frame')
        screen_frm.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)

        # Create and place two Label widgets
        title_lbl = ttk.Label(screen_frm, text = '-- Title Here --', 
                              style='Title.TLabel')
        title_lbl.pack(side=tk.TOP, pady=(20, 0))
        content_lbl = ttk.Label(screen_frm, text = '-- Stuff Here --')
        content_lbl.pack(side=tk.TOP, expand=True, fill=tk.Y)


        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)



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
        self.iconbitmap(self, default='./templates/wolftrack.ico')
        self.resizable(width = False, height = False)

        # Creates a grid with one column and row    
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Add content frame to application
        PageFrm(self)


def main():
    prog_app = App()
    prog_app.mainloop()


if __name__ == '__main__': main()
