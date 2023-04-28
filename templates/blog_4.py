"""
Program: blog_4
Creation Data: 12/29/2022
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Creating a Class-based Python Tkinter Template - Part 4

Description: Post part of a series on creating a class-based GUI
            using Python's Tkinter module.

Previous code: blog_3 available on github

Changes: 12/29/2022 - Create three methods to help organize 
                      the page display. 
Changes: 04/29/2023 - Update path to favicon after move to templates folder
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PageFrm(tk.Frame): 
    # Container frame for page content
    def __init__(self, parent):
        super().__init__(parent)

        # Configure style
        self.style = ttk.Style(self)
        self.style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_grid_frame(self, 'Screen Frame', 1)

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_grid_frame(self, parent:ttk.Frame, text:str = '', bdwidth:int = 0) -> ttk.Frame:
        """
        Description: Creates frame for page content
        Param: parent  - Container widget into which frame is placed
        Param: text    - Label text for frame, default is null (no text)
        Param: bdwidth - Width of frame border, default is 0 (no border)
        Return: frame  - grid-based frame (parent must use grid for geometry manager)
        """
        # Define and place the widget
        frame = ttk.LabelFrame(parent, text='Screen Frame')
        frame.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)
        frame.configure(borderwidth=bdwidth)

        # Create and place two Label widgets
        title_lbl = ttk.Label(frame, text = '-- Title Here --', 
                              style='Title.TLabel')
        title_lbl.pack(side=tk.TOP, pady=(20, 0))
        content_lbl = ttk.Label(frame, text = '-- Stuff Here --')
        content_lbl.pack(side=tk.TOP, expand=True, fill=tk.Y)

        return frame


class App(tk.Tk):  
    # Inheriting from Tk class
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
        
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Add content frame to application
        PageFrm(self)


def main():
    prog_app = App()
    prog_app.mainloop()

if __name__ == '__main__': main()
