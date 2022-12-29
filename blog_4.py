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

"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class PageFrm(tk.Frame): 
    # Container frame for page content
    def __init__(self, parent):
        # constructor allows the use of the same 
        # args as the subclassed tk.Frame
        super().__init__(parent)

        # Class constant(s)
        self.TITLE_FONT = ("Helvetica", 16, "bold")

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_grid_frame(self, 'Screen Frame', 1)

    def create_grid_frame(self, parent:tk.Frame, text:str = '', bdwidth:int = 0) -> tk.Frame:
        """
        Description: Creates grid-based LabelFrame
        Param: parent  - Container widget into which frame is placed
        Param: text    - Label text for frame, default is null (no text)
        Param: bdwidth - Width of frame border, default is 0 (no border)
        Return: frame  - grid-based frame (parent must use grid for geometry manager)
        """
        # Define and place the widget
        frame = tk.LabelFrame(parent, text=text)
        frame.grid(column=0, row=0, padx=10, pady=10, sticky=tk.NSEW)
        frame.configure(borderwidth=bdwidth)

        #  Configure layout proportions for inside frame 
        self.set_col_proportions(frame, (1, ))
        self.set_row_proportions(frame, (1, 1))

        # Create and place two Label widgets
        title_lbl = tk.Label(frame, text = '-- Title Here --', font=self.TITLE_FONT)
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)
        content_lbl = tk.Label(frame, text = '-- Stuff Here --')
        content_lbl.grid(column = 0, row = 1,pady=(30, 20), sticky = tk.EW)

        return frame

    def set_row_proportions(self, parent:tk.Frame, weights:tuple[int]) -> None:
        """
        Description: Create one or more rowconfigure() statements
        Param: parent  - the frame to which the method refers
        Param: weights - The weight value(s) for the row
        Returns: None
        """
        for row, weight in enumerate(weights):
            parent.rowconfigure(row, weight = weight)

    def set_col_proportions(self, parent:tk.Frame, weights:tuple[int]) -> None:
        """
        Description: Create one or more columnconfigure() statements
        Param: parent  - the frame to which the method refers
        Param: weights - The weight value(s) for the column
        Returns: None
        """
        for col, weight in enumerate(weights):
            parent.columnconfigure(col, weight = weight)


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
