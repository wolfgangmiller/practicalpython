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
Changes: 04/29/2023 - Update path to favicon after move to templates folder
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

        # Configure style
        self.style = ttk.Style(self)
        self.style.configure('Title.TLabel', font=('Helvetica', 12, 'bold'))

        # Configure layout proportions for frame container
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        # Define and place the widget
        self.create_notebook(self)

        # Places instance in parent using the grid method
        self.grid(column=0, row=0, sticky = tk.NSEW)

    def create_notebook(self, parent:tk.Frame) -> ttk.Notebook:
        """
        Description: Creates the notebook for the tabbed content
        Param: parent  - Container widget into which frame is placed
        Return: notebook 
        """
        # Create the notebook 
        self.notebook = ttk.Notebook(parent)
        self.notebook.place(relx=0, rely=0, relwidth=1, relheight=1, anchor=tk.NW)

        # Create the two tab frames
        tab1 = ttk.Frame(self.notebook)
        tab2 = ttk.Frame(self.notebook)
        tab1.pack(fill=tk.BOTH, expand=True)
        tab2.pack(fill=tk.BOTH, expand=True)

        # Add tab frames to notebook
        self.notebook.add(tab1, text='Tab One')
        self.notebook.add(tab2, text='Tab Two')


        # Create and place two Label widgets on each tab
        title_lbl = ttk.Label(tab1, text = '-- Tab 1 Content Title Here --',
                             style='Title.TLabel')
        title_lbl.pack(side=tk.TOP, pady=(20, 0))
        content_lbl = ttk.Label(tab1, text = '-- Tab 1 Stuff Here --')
        content_lbl.pack(side=tk.TOP, expand=True)

        title_lbl = ttk.Label(tab2, text = '-- Tab 2 Content Title Here --',
                             style='Title.TLabel')
        title_lbl.pack(side=tk.TOP, pady=(20, 0))
        content_lbl = ttk.Label(tab2, text = '-- Tab 2 Stuff Here --')
        content_lbl.pack(side=tk.TOP, expand=True)

        # Create navigation button to tab 2
        tab2_btn = ttk.Button(tab1, text='To Tab 2', command=lambda: self.select_tab(1))
        tab2_btn.pack(side=tk.TOP, expand=True)

        return self.notebook

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
