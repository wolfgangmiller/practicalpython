"""
Program: blog_9
Creation Data: 03/03/2023
Revision Date:
Blog Name: Practical Python
Blog URL: https://practicalpythonnow.blogspot.com/
Blog Post: Creating a Tabbed Notebook with Tkinter

Description: Creating tabs in a notebook
            using Python's Tkinter module.
            Based on the single page Tkinter template
            from Blog 4.

Previous code: blog_4 available on github

Changes: 03/03/2023 - Add two notebook tabs to page frame. 

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
        self.TITLE_FONT = ("Helvetica", 12, "bold")

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_notebook(self)

    def create_notebook(self, parent:tk.Frame) -> ttk.Notebook:
        """
        Description: Creates the notebook for the tabbed content
        Param: parent  - Container widget into which frame is placed
        Return: notebook 
        """
        # Create the notebook 
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack( fill='both', expand=True, pady=(10, 0))

        # Create the two tab frames
        tab1 = tk.Frame(self.notebook, width=300, height=290)
        tab2 = tk.Frame(self.notebook, width=300, height=290)
        tab1.pack(fill='both', expand=True)
        tab2.pack(fill='both', expand=True)

        # Add tab frames to notebook
        self.notebook.add(tab1, text='Tab One')
        self.notebook.add(tab2, text='Tab Two')

        # Configure layout proportions for inside each tab frame 
        # One column and two two rows
        self.set_col_proportions(tab1, (1, ))
        self.set_row_proportions(tab1, (1, 1, 1))
        self.set_col_proportions(tab2, (1, ))
        self.set_row_proportions(tab2, (1, 1))

        # Create and place two Label widgets on each tab
        title_lbl = tk.Label(tab1, text = '-- Tab 1 Content Title Here --', font=self.TITLE_FONT)
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)
        content_lbl = tk.Label(tab1, text = '-- Tab 1 Stuff Here --')
        content_lbl.grid(column = 0, row = 1, pady=(30, 20), sticky = tk.EW)

        title_lbl = tk.Label(tab2, text = '-- Tab 2 Content Title Here --', font=self.TITLE_FONT)
        title_lbl.grid(column = 0, row = 0, pady=(10, 0), sticky = tk.EW)
        content_lbl = tk.Label(tab2, text = '-- Tab 2 Stuff Here --')
        content_lbl.grid(column = 0, row = 1, pady=(30, 20), sticky = tk.EW)

        # Create navigation button to tab 2
        tab2_btn = ttk.Button(tab1, text='To Tab 2', command=lambda: self.select_tab(1))
        tab2_btn.grid(column = 0, row = 2, pady=(10, 20), sticky = tk.N)

        return self.notebook

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

    def select_tab(self, tab_id:int) -> None:
        """
        Description: Display tab based on tab id
        Param: tab_id  - Tab id from notebook's tab list
        Return: None
        """
        self.notebook.select(tab_id)

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
